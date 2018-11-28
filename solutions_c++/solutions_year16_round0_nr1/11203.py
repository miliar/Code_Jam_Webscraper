#include <vector>
#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include <algorithm>
#include "functions.h"

using namespace std;

void countingSheep() {
	ifstream inputFile("A-large.in");
	ofstream outputFile("sheepResult.txt");
	if (inputFile.is_open() && outputFile.is_open()) {
		int numOfCases;
		inputFile >> numOfCases;
		for (int caseIndex = 1; caseIndex <= numOfCases; caseIndex++) {
			long long inputNumber;
			inputFile >> inputNumber;
			if (inputNumber == 0) {
				outputFile << "Case #" << caseIndex << ": INSOMNIA" << endl;
			}
			else {
				long long currNumber = inputNumber;
				int multiple = 0;
				int seenCount = 0;
				int numberCheck[10] = { 0 };
				while (seenCount != 10) {
					++multiple;
					currNumber = (long long)inputNumber * multiple;
					while (currNumber > 0){
						int lastDigit = currNumber % 10;
						
						if (numberCheck[lastDigit] == 0) {
							numberCheck[lastDigit] = 1;
							seenCount++;
						}
						currNumber /= 10;
					}
				}
				outputFile << "Case #" << caseIndex << ": " << (multiple*inputNumber) << endl;
			}	
		}
	}
}

int main() {
	countingSheep();




	system("PAUSE");
}