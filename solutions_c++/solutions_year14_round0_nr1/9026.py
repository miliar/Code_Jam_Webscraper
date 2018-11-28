/*
 * Google Code Jam 2014 - Qualification Round - A: Magic Trick
 *
 * Copyright reserved to:
 *
 * Krszytof (Kris Rogo) Rogozinski 
 * rogozinski13@gmail.com
 * www.KrisRogo.co.uk
 *
 */

// include standard template libries
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

// global constants
const int kErrorCode = -999;

// prepare file variables
ifstream inputFile;
string inputPath = "input.txt";

ofstream outputFile;
string outputPath = "output.txt";

// open a file used for input, return -999 if failed
int OpenInputFile(string filePath)
{
	// open
	inputFile = ifstream (filePath);

	// make sure it exists
	if (!inputFile)
	{
		cout << "Error! Can't open file called " << filePath << endl;
		system( "pause" );
		return kErrorCode;
	}

	// give the file back to the main method
	return 1;
}

// open a file used for input, return -999 if failed
int OpenOutputFile(string filePath)
{
	// open
	outputFile = ofstream (filePath);

	// make sure it exists
	if (!outputFile)
	{
		cout << "Error! Can't open file called " << filePath << endl;
		system( "pause" );
		return kErrorCode;
	}

	// give the file back to the main method
	return 1;
}

int ReadInNumber()
{
	// read in single character
	char ch = inputFile.get();

	// temporary string 
	string temp = "";

	while (!inputFile.eof() && ch != ' ' && ch != '\n')
	{
		temp += ch; // append character to the temporary string
		ch = inputFile.get(); // get next character
	}

	// convert string to the number
	return atoi(temp.c_str());
	

}

void ReadArrangment(int vlues[4])
{
	// get the line of intrest in this arrangment
	int chosenLine = ReadInNumber();

	// get to the line of intrest and save it;
	for (int a1 = 1; a1 <= 4; a1++)
	{
		if (a1 == chosenLine) // if this is a chosen line, save it
		{
			for (int v = 0; v < 4; v++)
			{
				vlues[v] = ReadInNumber();
			}
		}
		else // discard the rest
		{
			for (int v = 0; v < 4; v++)
			{
				int notImportant = ReadInNumber();
			}
		}
	}
}

int main()
{
	// open files
	if(OpenInputFile(inputPath) != kErrorCode && OpenOutputFile(outputPath) != kErrorCode)
	{
		inputFile >> noskipws; // make sure all characters are being read

		int nOfCases = ReadInNumber();	 // get the nuber of cases in this input file

		// go through all the input files
		for (int caseN = 1; caseN <= nOfCases; caseN++)
		{
			// prepare holding values
			int firstArr[4];
			int secondArr[4];
			string outMessage = "Case #" + to_string(caseN) + ": ";

			// get the arragnments
			ReadArrangment(firstArr);
			ReadArrangment(secondArr);

			int match = kErrorCode;
			int nOfMatches  = 0;

			// scan for matches
			for (int a1 = 0; a1 < 4; a1++)
			{
				for (int a2 = 0; a2 < 4; a2++)
				{
					// is there a match
					if (firstArr[a1] == secondArr[a2])
					{
						match = firstArr[a1]; // save matched number
						nOfMatches ++;
					}

				}
			}

			// determin the result
			if (nOfMatches < 1)
			{
				outMessage += "Volunteer cheated!";
			}
			else if (nOfMatches > 1)
			{
				outMessage += "Bad magician!";
			}
			else
			{
				outMessage += to_string(match);
			}

			// save the message
			outputFile << outMessage << endl;

		}
		

		// close the file
		inputFile.close();
	}

}