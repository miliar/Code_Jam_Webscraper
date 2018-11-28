// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <string>
#include <iostream>
#include <fstream>
#include <stdio.h>      /* printf, fgets */
#include <stdlib.h>     /* atoi */

using namespace std;

int main() {
	std::ifstream input("A-small-attempt3.in");
	std::string line;
	std::getline(input, line); // skip the first line
	const int numlines = atoi(line.c_str());
	const std::string emptyString = "";
	std::ofstream outputFile;
	outputFile.open("output.txt");
	for (int rowNumber = 1; std::getline(input, line) && line.compare(emptyString) != 0; ++rowNumber) {
		const int numElements = (line[0] - '0') + 1;
		int rowOutput = 0;
		int numPeopleClapping = 0;
		for (int column = 0; column < numElements; ++column)
		{
			char charValue = line[column + 2];
			int numberOfPeopleInColumn = charValue - '0';
			if (column > numPeopleClapping) {
				const int diff = column - numPeopleClapping;
				rowOutput += diff;
				numPeopleClapping += diff;
				//if(numPeopleClapping != column) {
				//  cout << "error 1";
				//}
			}
			numPeopleClapping += numberOfPeopleInColumn;
		}
		outputFile << "Case #" << rowNumber << ": " << rowOutput << endl;
		cout << "Case #" << rowNumber << ": " << rowOutput << endl;
	}
	outputFile.close();
	return 0;
}
