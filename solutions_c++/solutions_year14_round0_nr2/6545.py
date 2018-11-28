#include <stdio.h>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>

using namespace std;

void main() {
	ifstream myFile;
	myFile.open("data.txt");

	//ofstream outFile;
	//outFile.open("out.txt");
	FILE * outFile;
	outFile = fopen("out.txt","w");

	int numCases = 0;
	double C, F, X;
	double currentProduction = 2;
	double totalTime = 0.000000;
	bool goalReached = false;
	int curCase = 1;

	myFile >> numCases;

	while (numCases--) {
		currentProduction = 2;
		totalTime = 0;
		goalReached = false;

		myFile >> C >> F >> X;

		while (!goalReached) {
			if ((X/currentProduction) > ((C/currentProduction) + (X/(currentProduction+F)))) {
				//buy a farm
				totalTime += ( C/  currentProduction);
				currentProduction += F;
				//cout << "Farm bought" << endl;
				//cout << "Added Time: " << ( C/ ( currentProduction - F)) << endl;
			} else {
				// don't buy, and done
				totalTime += ( X/  currentProduction);
				goalReached = true;
				//cout << "Goal Reached" << endl;
				//cout << "Added Time: " << ( X/  currentProduction) << endl;
			}
			//cout << "Total Time: " << totalTime << endl;
		}

		fprintf(outFile, "Case #%d: %.7f\n", curCase++, totalTime);
		//outFile << "Case #" << curCase++ << ": " << totalTime;

		//system("pause");
	}

}