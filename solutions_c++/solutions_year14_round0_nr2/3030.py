#include "stdafx.h"
//basic file operations
#include <iostream>
#include <fstream>
#include <windows.h> ///sleep
#include <string>
#include <iomanip>
using namespace std;

struct TestCase {
	double C, F, X;
};

double* parseLineToArgs(string line) {
	double result[3];
	int currentResultIndex = 0;
	string currentNumber = "";
	for (int i = 0; i < line.length(); i++){
		if (line[i] != ' ') {
			currentNumber += line[i];
		}
		else {
			result[currentResultIndex] = atof(currentNumber.c_str());
			currentResultIndex++;
			currentNumber = "";
		}
	}
	result[currentResultIndex] = atof(currentNumber.c_str());
	return result;
}

double solve(TestCase aTestCase){
	double totalTime = 0;
	double cookiesPerSecond = 2;
	while (true) {
		double timeToEnd = aTestCase.X / cookiesPerSecond;
		double timeToFarm = aTestCase.C / cookiesPerSecond;
		if (timeToEnd <= timeToFarm) {
			totalTime += timeToEnd;
			return totalTime;
		}
		if ( timeToEnd - timeToFarm > aTestCase.C / aTestCase.F) {
			//buy a farm
			cookiesPerSecond += aTestCase.F;
			totalTime += timeToFarm;
		}
		else {
			totalTime += timeToEnd;
			return totalTime;
		}
	}
	return -1;
}

int _tmain(int argc, char* argv[])
{
	int numberOfTestCases;

	ifstream myfile;
	ofstream outputFile;
	string line;
	myfile.open("input.in");
	outputFile.open("output.out");
	TestCase* aTestCase;

	if (myfile.is_open()){
		int currentLine = 0;

		//reading and parse input
		getline(myfile, line);
		if (currentLine == 0) numberOfTestCases = atoi(line.c_str());
		aTestCase = new TestCase[numberOfTestCases];

		for (int i = 0; i < numberOfTestCases; i++){
			cout << i << "\n";
			getline(myfile, line);
			double* arguments = parseLineToArgs(line);
			aTestCase[i].C = arguments[0];
			aTestCase[i].F = arguments[1];
			aTestCase[i].X = arguments[2];

			//solve problem
			double time = solve(aTestCase[i]);
			outputFile << "Case #" << i + 1 << ": "; 
			outputFile.setf(ios::fixed, ios::floatfield);
			outputFile.precision(7);
			outputFile << time;

			if (i + 1 != numberOfTestCases)
				outputFile << "\n";
		};
		myfile.close();
	}
	else {
		cout << "unable to open file";
	}
	return 0;
}

