// codeJamMagician.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
//basic file operations
#include <iostream>
#include <fstream>
#include <windows.h> ///sleep
#include <string>
using namespace std;


struct TestCase {
	int firstDecision, secondDecision;
	int firstCards[4][4];
	int secondCards[4][4];
};

int * parseRowToArray(string line) {
	int result[4];
	int currentResultIndex = 0;
	string currentNumber = "";
	for (int i = 0; i < line.length(); i++){
		if (line[i] != ' ') {
			currentNumber += line[i];
		}
		else {
			result[currentResultIndex] = atoi(currentNumber.c_str());
			currentResultIndex++;
			currentNumber = "";
		}
	}
	result[currentResultIndex] = atoi(currentNumber.c_str());
	return result;
}

int solve(TestCase aTestCase){
	int solution = 0;
	int* row1 = aTestCase.firstCards[aTestCase.firstDecision - 1];
	int* row2 = aTestCase.secondCards[aTestCase.secondDecision - 1];
	for (int rowIndex = 0; rowIndex < 4; rowIndex++) {
		for (int columnIndex = 0; columnIndex < 4; columnIndex++){
			if (row1[rowIndex] == row2[columnIndex]){
				if (solution == 0) solution = row2[columnIndex];
				else solution = -1;
			}
		}
	}
	return solution;
}

int _tmain(int argc, char* argv[])
{
	//input variables
	int numberOfTestCases;
	

	ifstream myfile;
	ofstream outputFile;
	string line;
	myfile.open("test.txt");
	outputFile.open("output.txt");
	TestCase * aTestCase;

	if (myfile.is_open()){
		cout << "open file \n";
		int currentLine = 0;

		//reading input
		getline(myfile, line);
		if (currentLine == 0) numberOfTestCases = atoi(line.c_str());
		aTestCase = new TestCase[numberOfTestCases];

		for (int i = 0; i < numberOfTestCases; i++){
			cout << i << "\n";
			getline(myfile, line);
			aTestCase[i].firstDecision = atoi(line.c_str());
			
			// read 4 rows
			for (int row = 0; row < 4; row++){
				getline(myfile, line);
				int * tmp = parseRowToArray(line);
				for (int column = 0; column < 4; column++)
					aTestCase[i].firstCards[row][column] = tmp[column];
			};

			getline(myfile, line);
			aTestCase[i].secondDecision = atoi(line.c_str());

			for (int row = 0; row < 4; row++){
				getline(myfile, line);
				int * tmp = parseRowToArray(line);
				for (int column = 0; column < 4; column++)
					aTestCase[i].secondCards[row][column] = tmp[column];
			};


			//solve problem
			int numberOfSolution = solve(aTestCase[i]);
			switch (numberOfSolution)
			{
			case 0: outputFile << "Case #" << i + 1 << ": Volunteer cheated!";
				break;
			case -1: outputFile << "Case #" << i + 1 << ": Bad magician!";
				break;
			default: outputFile << "Case #" << i + 1 << ": " << numberOfSolution;
				break;
			}
			if (i + 1 != numberOfTestCases)
				outputFile << "\n";
		};
		myfile.close();
	}
	else {
		cout << "unable to open file";
	}
	Sleep(2000);
	return 0;
}

