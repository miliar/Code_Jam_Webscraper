/*
 * Google Code Jam 2014 - Qualification Round - B: Cookie Clicker Alpha
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
#include <iomanip>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

// global constants
const int kErrorCode = -999;
const float kCookiePerSecond = 2.0f;

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

double ReadFlNumber()
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
	return strtod(temp.c_str(), NULL);
	

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
			// read in the input values
			double c_FarmCost = ReadFlNumber();
			double f_FarmProduction = ReadFlNumber();
			double x_WinScore = ReadFlNumber();

			// prepare begining of output string
			string outMessage = "Case #" + to_string(caseN) + ": ";

			int farmCount = 1; // indicate how many farms to use
			double currentProduction = f_FarmProduction + kCookiePerSecond; // calculate production rate
			double farmTimeCost = c_FarmCost / kCookiePerSecond; // how much did it cost to build this farm
			double costOfPreviousFarms = 0; // cost of all farms build before

			// calculate the first 2 posibilities
			double previousProduction = x_WinScore / kCookiePerSecond;
			double nextProduction = farmTimeCost + x_WinScore / currentProduction;



			// find lower production
			while (nextProduction < previousProduction)
			{
				previousProduction = nextProduction; // save the lower production time as previous
				costOfPreviousFarms += farmTimeCost; // save cost of previous farm

				farmCount++; // buy new farm;
				farmTimeCost = c_FarmCost / currentProduction; // calculate time it takes to get a new farm
				currentProduction = currentProduction + f_FarmProduction; // calcualte production after adding new farm
				nextProduction = costOfPreviousFarms + farmTimeCost + (x_WinScore / currentProduction);
			}

			// save the message
			stringstream tempStr;
			tempStr << fixed << setprecision( 7 ) << previousProduction;
			outputFile << outMessage << tempStr.str() << endl;

		}
		

		// close the file
		inputFile.close();
	}

}