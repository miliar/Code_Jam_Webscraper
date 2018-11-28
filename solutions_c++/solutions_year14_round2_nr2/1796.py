/*
 * Google Code Jam 2014 - Round 1 B - A: XXX
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
#include <bitset>

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

// read a single word from the file
string ReadInStr()
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
	return temp.c_str();
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

struct KChar
{
	char value;
	int count;
	bool changeMade;

	KChar(char ch, int co)
	{
		value = ch;
		count = co;
		changeMade = false;
	}
};

struct KWord
{
	vector <KChar> chars;

	KWord(string word)
	{
		for (int i = 0; i < word.size(); i++)
		{
			if (i != 0 && chars.back().value == word[i])
			{
				chars.back().count++;
			}
			else
			{
				chars.push_back(KChar(word[i], 1));
			}
		}
	}
};

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
			vector <KWord> words;
			string outMessage = "Case #" + to_string(caseN) + ": ";
			long A = ReadInNumber();
			long B = ReadInNumber();
			long K = ReadInNumber();

			int wins = 0;

			for (long a = 0; a < A; a++)
			{
				for (long b = 0; b < B; b++)
				{
					long test = a & b;
					if (test < K)
					{
						wins++;
					}
				}
			}

			// determin the result

			outMessage += to_string(wins);

			// save the message
			outputFile << outMessage << endl;

		}
		

		// close the file
		inputFile.close();
	}

}