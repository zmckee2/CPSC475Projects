'''
Team Member 1: Zach McKee
Team Member 2: N/A
Zagmail address for team member 1: zmckee@zagmail.gonzaga.edu
Project 2: This project asks for a file and substring, then prints
		   how many instances of the substring it finds in the file
Due: September 5th, 2018
'''
import re

'''
openFile()
This function opens up the file with whatever
name the user inputed as long as the files exists.
It will return the file object
'''
def openFile():
	print("\n\nPlease enter a file name of an existing file")
	print("Please include quotes around the file name")
	while(True):
		userIn = input('Please enter a file name\n')
		try:
			fileIn = open(userIn, 'r')
			break
		except:
			print("Invalid file name, please try again")
	return fileIn

'''
getSubstring()
This function gets the substring that the user
wants to look for.
'''
def getSubstring():
	print("\n\nPlease include quotes around your substring")
	return input('Please enter a substring to search for\n')

'''
findSubInFile(fileObject, stringObject)
This function searches the file passed in
for the substring passed in.
It will return the number of occurrences of
the substring it finds in the file.
'''
def findSubInFile(fileIn, substring):
	numberOfOccurances = 0;
	#To search the file, I decided to split each line up
	for line in fileIn:
		#Once the lines were split, I broke every word appart into a list
		#using re.findAll. This makes sure the list only includes the words
		#and omits any punctuation
		listOfLine = re.findall(r"\w+", line)
		for word in listOfLine:
			if(word == substring):
				numberOfOccurances += 1
	return numberOfOccurances
	
'''
main()
This function is the main function.
It only calls the other functions and prints
the number of occurances at the end
'''
def main():
	fileIn = openFile()
	substring = getSubstring()
	numberOfOccurances = findSubInFile(fileIn, substring)
	print("I found " + str(numberOfOccurances) + " occurrences of " + substring)
	
main()