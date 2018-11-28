#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>
#include <stdlib.h>
#include <sstream>
#include <iomanip>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{

	ifstream inputFile;
	ofstream outputFile;
	unsigned int numCases, i, seconds;
	string testString;

	//
	// Prepare I/O
	//
	outputFile.open("output.txt");
	if (outputFile.is_open() == false) {
		cout << "Shenanigans, can't open the output" << endl;
		return -1;
	}

	inputFile.open("input.txt");
	if (inputFile.is_open() == false) {
		cout << "Disaster, we couldn't open the input file" << endl;
		return -1;
	}

	getline(inputFile, testString);
	numCases = atoi(testString.c_str());

	for (i = 0; i < numCases; i++) {

		getline(inputFile, testString);
		istringstream iss(testString);
		string subStr;
		double farmCost, farmProfit, goal, prevBest, cookieProfit = 2.0, timePenalty = 0, newBest = 0;

		iss >> subStr;
		farmCost = atof(subStr.c_str());
		iss >> subStr;
		farmProfit = atof(subStr.c_str());
		iss >> subStr;
		goal = atof(subStr.c_str());

		//
		// Basic greedy algorithm
		//
		newBest = goal/2.0;
		do {
			prevBest = newBest;
			//
			// Assume we buy each factory as soon as possible
			//
			timePenalty += farmCost / cookieProfit;
			cookieProfit += farmProfit;
			newBest = goal / cookieProfit + timePenalty;

		} while (newBest < prevBest);

		outputFile << "Case #" << (i + 1) << ": " << std::setprecision(9) << prevBest << endl;

	}
	return 0;
}

