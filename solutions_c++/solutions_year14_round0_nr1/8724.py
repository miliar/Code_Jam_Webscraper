#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>
#include <stdlib.h>
#include <sstream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{

	ifstream inputFile;
	ofstream outputFile;
	unsigned int numCases, i, cardOne, cardTwo, k, j;
	unsigned int boardOne[4][4], boardTwo[4][4];
	string testString;
	int answer;

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
		cardOne = atoi(testString.c_str());
		cardOne--;

		for (k = 0; k < 4; k++) {
			getline(inputFile, testString);
			istringstream iss(testString);
			string subStr;

			//
			// Not thread safe, but let's not try and be needlessly fancy
			// (and this is only possible since we know the input is good
			// otherwise NULLs would lead to undefined behaviour with
			// atoi())
			//
			for (j = 0; j < 4; j++) {
				iss >> subStr;
				boardOne[k][j] = atoi(subStr.c_str());
			}
		}

		getline(inputFile, testString);
		cardTwo = atoi(testString.c_str());
		cardTwo--;

		for (k = 0; k < 4; k++) {
			getline(inputFile, testString);
			istringstream iss(testString);
			string subStr;

			//
			// Not thread safe, but let's not try and be needlessly fancy
			// (and this is only possible since we know the input is good
			// otherwise NULLs would lead to undefined behaviour with
			// atoi())
			//
			for (j = 0; j < 4; j++) {
				iss >> subStr;
				boardTwo[k][j] = atoi(subStr.c_str());
			}
		}

		//
		// Brute force our answer.
		// -1:    No Answer
		//  0:    Multiple answers
		//  1-16: Valid answer
		//
		answer = -1;

		for (k = 0; k < 4; k++) {
			for (j = 0; j < 4; j++) {
				if (boardOne[cardOne][k] == boardTwo[cardTwo][j]) {
					if (boardOne[cardOne][k] == answer) {
						continue;
					}
					else if (answer == -1) {
						answer = boardOne[cardOne][k];
					}
					else {
						answer = 0;
					}
				}
			}
		}

		switch (answer) {
		case -1:
			cout << "Case #" << (i+1) << ": Volunteer cheated!" << endl;
			outputFile << "Case #" << (i + 1) << ": Volunteer cheated!" << endl;
			break;
		case 0:
			cout << "Case #" << (i + 1) << ": Bad magician!" << endl;
			outputFile << "Case #" << (i + 1) << ": Bad magician!" << endl;
			break;
		default:
			cout << "Case #" << (i + 1) << ": " << answer << endl;
			outputFile << "Case #" << (i + 1) << ": " << answer << endl;
			break;
		}

	}
	return 0;
}

