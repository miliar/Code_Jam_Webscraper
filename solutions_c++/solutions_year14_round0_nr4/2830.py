#include "stdafx.h"
//basic file operations
#include <iostream>
#include <fstream>
#include <windows.h> ///sleep
#include <string>
#include <list>

using namespace std;

struct TestCase {
	list<double> Naomi;
	list<double> Ken;
};

list<double> parseLineToArgs(string line) {
	list<double> result;
	string currentNumber = "";
	for (int i = 0; i < line.length(); i++){
		if (line[i] != ' ') {
			currentNumber += line[i];
		}
		else {
			result.push_back(atof(currentNumber.c_str()));
			currentNumber = "";
		}
	}
	result.push_back(atof(currentNumber.c_str()));
	return result;
}

int solveDeceitfulWar(TestCase aTestCase){
	/* strategy:
	If Naomi has a number which is bigger than Ken minmum number. She chose the smallest number which is bigger 
	than Kens minimum and says Kens maximum plus an epsilon. So that Ken chose his minimum. Naomi wins the round.
	If Naomi has no number which is bigger than Kens minimum number, she loose all rounds, so return her current wins.
	*/
	int nwins = 0;

	while (aTestCase.Naomi.size() > 0) {
		double n;
		bool exits = false;
		for (int i = 0; i < aTestCase.Naomi.size(); i++){
			// get i-th element of Naomis list
			std::list<double>::iterator it = aTestCase.Naomi.begin();
			std::advance(it, i);
			n = *&*it;

			if (n > aTestCase.Ken.front()) {
				aTestCase.Naomi.remove(n);
				aTestCase.Ken.pop_front();
				nwins++;
				exits = true;
				break;
			};			
		}

		if (!exits) return nwins;
	}

	return nwins;
}

int solveWar(TestCase aTestCase){
	/* strategy
	Naomi chose biggest number. Ken takes smallest number which is bigger than Naomis number. 
	If he don't have that number he takes his smallest one.
	*/
	int nwin = 0;
	while (aTestCase.Naomi.size() > 0) {
		double n = aTestCase.Naomi.front();
		aTestCase.Naomi.pop_front();
		bool found = false;
		for (int i = 0; i < aTestCase.Ken.size(); i++){
			//get i-th element of Kens list
			std::list<double>::iterator it = aTestCase.Ken.begin();
			std::advance(it, i);
			double k = *&*it;
			if (n < k) {
				aTestCase.Ken.remove(k);
				found = true;
				break;
			}
		}
		if (!found){
			aTestCase.Ken.pop_front();
			nwin++;
		}
	}
	return nwin;
}

int main()
{
	int numberOfTestCases;

	ifstream inputfile;
	ofstream outputFile;
	string line;
	inputfile.open("input.in");
	outputFile.open("output.out");
	TestCase* aTestCase;

	if (inputfile.is_open()){
		//reading and parse input
		getline(inputfile, line);
		numberOfTestCases = atoi(line.c_str());
		aTestCase = new TestCase[numberOfTestCases];

		for (int i = 0; i < numberOfTestCases; i++){
			getline(inputfile, line);
			// no need to save N

			getline(inputfile, line); 
			aTestCase[i].Naomi = parseLineToArgs(line);
			aTestCase[i].Naomi.sort();

			getline(inputfile, line);
			aTestCase[i].Ken = parseLineToArgs(line);
			aTestCase[i].Ken.sort();

			//solve problem
			outputFile << "Case #" << i + 1 << ": " << solveDeceitfulWar(aTestCase[i]) << " " << solveWar(aTestCase[i]);

			if (i + 1 != numberOfTestCases)
				outputFile << "\n";
		};
		inputfile.close();
		outputFile.close();
	}
	else {
		cout << "unable to open file";
	}
	return 0;
}