// MagicShow.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

vector<int> getVectorFromString(string inString)
{
	vector<int> aVectorOfInt;
	istringstream iss(inString);
	do
    {
        string sub;
        iss >> sub;
		if ( sub.size() != 0 )
			aVectorOfInt.push_back(  atoi(sub.c_str()) );
    } while (iss);
	return aVectorOfInt;
}

int getResultFromVectors( vector<int> inVec1,  vector<int> inVec2 )
{
	vector<int> Common;
	for ( int i = 0; i < inVec1.size(); i++ ) {
		for ( int j = 0; j < inVec2.size(); j++ ) {
			if ( inVec1[i] == inVec2[j] )
				Common.push_back( inVec1[i] );
		}
	}
	if ( Common.size() == 0 )
		return 0;
	if ( Common.size() > 1 )
		return 99;
	return Common[0];
}

int _tmain(int argc, _TCHAR* argv[])
{
	int NumberOfCases;

	cout << "Magic Show." << endl;
	
	string aLine;
	ifstream infile("MagicShowInput.txt");

	getline( infile, aLine );
	NumberOfCases = atoi(aLine.c_str());

	int FirstRow = 0;
	int SecondRow = 0;
	vector<int> FirstRowVector;
	vector<int> SecondRowVector;
	vector<int> Result;

	while( infile.eof() == false ) {
		getline( infile, aLine );
		FirstRow = atoi(aLine.c_str());
		for ( int i = 0; i < 4; i++ ) {
			getline( infile, aLine );
			if ( (i + 1) == FirstRow ) {
				FirstRowVector = getVectorFromString( aLine );
			}
		}
		getline( infile, aLine );
		SecondRow = atoi(aLine.c_str());
		for ( int i = 0; i < 4; i++ ) {
			getline( infile, aLine );
			if ( (i + 1) == SecondRow ) {
				SecondRowVector = getVectorFromString( aLine );
			}
		}
		Result.push_back(getResultFromVectors( FirstRowVector, SecondRowVector ) );
		cout << aLine << endl;
	}

	ofstream myFile;
	myFile.open("MagicShowOutput.txt");

	for ( int i = 0; i < Result.size(); i++ ) {
		if ( Result[i] == 99 ) {
			myFile << "Case #" << (i+1) << ": Bad magician!" << endl;
		} else if ( Result[i] == 0 ) {
			myFile << "Case #" << (i+1) << ": Volunteer cheated!" << endl;
		} else {
			myFile << "Case #" << (i+1) << ": " << Result[i] << endl;
		}
	}

	cout << "Number of cases is " << NumberOfCases << endl;

	myFile.close();

	return 0;
}

