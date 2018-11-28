//
//  main.cpp
//  MagicTrick
//
//  Created by Patrick Burns on 4/12/14.
//  Copyright (c) 2014 Bl4ckSun. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <unistd.h>
using namespace std;

#if 0
string filename = "sample.in";
string resultsFile = "codeJamResults-sample.out";
#elif 1
string filename = "small.in";
string resultsFile = "codeJamResults-small.out";
#elif 0
string filename = "large.in";
string resultsFile = "codeJamResults-large.out";
#endif

ifstream inFile;
ofstream outFile;

// T = Test Cases

typedef enum {
	messUp		= 0,
	one			= 1 << 0,
	two			= 1 << 1,
	three		= 1 << 2,
	four		= 1 << 3,
	five		= 1 << 4,
	six			= 1 << 5,
	seven		= 1 << 6,
	eight		= 1 << 7,
	nine		= 1 << 8,
	ten			= 1 << 9,
	eleven		= 1 << 10,
	tweleve		= 1 << 11,
	thriteen	= 1 << 12,
	fourteen	= 1 << 13,
	fifteen		= 1 << 14,
	sixteeen	= 1 << 15,
}answers;

int numberOfTest;

int currentCard;

int firstAnswer;
int cardsFromFirstRow;

int secondAnswer;
int cardsFromSeondRow;

int result;
char *resultString;


int main(int argc, const char * argv[])
{
	chdir("/Users/p8burns/Development/GoogleCodeJam/2014/QualificationRound/MagicTrick/MagicTrick");
	inFile.open(filename);
	outFile.open(resultsFile);
	
	cout << "Hello world" << endl;
	
	inFile >> numberOfTest;
	for(int testNumber = 1; testNumber <= numberOfTest; testNumber++)
	{
		inFile >> firstAnswer;
		cardsFromFirstRow = 0;
		
		// Go through rows
		for (int i = 1; i < 5; i ++)
		{
			for(int j = 1; j <5; j++)
			{
				inFile >> currentCard;
				if(i == firstAnswer)
				{
					cardsFromFirstRow += 1 << (currentCard -1);
				}
			}
		}
		
		inFile >> secondAnswer;
		cardsFromSeondRow = 0;
		
		for (int i = 1; i < 5; i ++)
		{
			for(int j = 1; j <5; j++)
			{
				inFile >> currentCard;
				if(i == secondAnswer)
				{
					cardsFromSeondRow += 1 << (currentCard -1);
				}
			}
		}
		
		result = cardsFromFirstRow & cardsFromSeondRow;
		resultString = "Bad magician!";
		switch (result) {
			case messUp:
				resultString = "Volunteer cheated!";
				break;
				
			case one:
				resultString = "1";
				break;
				
			case two:
				resultString = "2";
				break;
				
			case three:
				resultString = "3";
				break;
				
			case four:
				resultString = "4";
				break;
				
			case five:
				resultString = "5";
				break;
				
			case six:
				resultString = "6";
				break;

			case seven:
				resultString = "7";
				break;
				
			case eight:
				resultString = "8";
				break;
				
			case nine:
				resultString = "9";
				break;
				
			case ten:
				resultString = "10";
				break;
				
			case eleven:
				resultString = "11";
				break;
				
			case tweleve:
				resultString = "12";
				break;
				
			case thriteen:
				resultString = "13";
				break;
				
			case fourteen:
				resultString = "14";
				break;
				
			case fifteen:
				resultString = "15";
				break;
				
			case sixteeen:
				resultString = "16";
				break;
				
			default:
				break;
		}
		
		
		
		
		cout << "Case #" << testNumber << ": " << resultString << endl;
		outFile << "Case #" << testNumber << ": " << resultString << endl;
	}
	outFile << endl;
    return 0;
}
