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
			int N = ReadInNumber();
			bool felgaWon = false;
			int correctionCount = 0;

			// read words in
			for (int wordN = 0; wordN < N; wordN++)
			{
				words.push_back(KWord(ReadInStr()));
			}

			// check if all words are the same size
			for (int wordN = 1; wordN < N && !felgaWon; wordN++)
			{
				if (words[wordN - 1].chars.size() != words[wordN].chars.size())
				{
					felgaWon = true;
				}
			}

			int shortWordIndx = 0;

			// find the shortest
			for (int wordN = 1; wordN < N && !felgaWon; wordN++)
			{
				if (words[wordN].chars.size() < words[shortWordIndx].chars.size())
				{
					shortWordIndx = wordN;
				}
			}

			// correct the words
			for (int wordN = 1; wordN < N && !felgaWon; wordN++)
			{
				// count diferences in word size to the first word
				for (int charN = 0; charN < words[wordN].chars.size(); charN++)
				{
					// if chars are differnet - felga won
					if (words[shortWordIndx].chars[charN].value != words[wordN].chars[charN].value)
					{
						felgaWon = true;
					}
					// if first word has more
					else if (words[shortWordIndx].chars[charN].count > words[wordN].chars[charN].count && !words[shortWordIndx].chars[charN].changeMade)
					{
						correctionCount += words[shortWordIndx].chars[charN].count - words[wordN].chars[charN].count;
						words[shortWordIndx].chars[charN].changeMade = true;
					}
					else if (words[shortWordIndx].chars[charN].count < words[wordN].chars[charN].count && !words[shortWordIndx].chars[charN].changeMade)
					{
						correctionCount += words[wordN].chars[charN].count - words[shortWordIndx].chars[charN].count;
						words[shortWordIndx].chars[charN].changeMade = true;
					}
				}
			}

			// determin the result
			if (felgaWon)
			{
				outMessage += "Fegla Won";
			}
			else
			{
				outMessage += to_string(correctionCount);
			}

			// save the message
			outputFile << outMessage << endl;

		}
		

		// close the file
		inputFile.close();
	}

}