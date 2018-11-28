#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;
int getIntFromFile(ifstream &input);
double getFloatFromFile(ifstream &input);
double timeToCollectXCookiesWithRate(double X, double F);

int main () {
	ifstream input;
	input.open ("B-large.in.txt");
	if (!input.is_open()) {
		return 1;
	}

	// FILE *pFile;
	// pFile = fopen("test.in", "w+");
	// float test;
	// fscanf (pFile, "%f", &test );
	// printf("TEST: %f\n", test);


	ofstream output;
	output.open("clicker_res_large0.txt");
	//output << setprecision(8);
	output << std::fixed;
	int testsCount = getIntFromFile(input);
	//printf("Test counts: %d\n", testsCount);
	 for (int i = 0; i < testsCount; ++i) {

		//printf ("***\n\nCASE #%d:\n", i);
		output << "Case #" << i+1 << ": ";

		double C, F, X;
		C = getFloatFromFile(input);
		//printf("C = %f\n", C );
		F = getFloatFromFile(input);
		//printf("F = %f\n", F );
		X = getFloatFromFile(input);
		//printf("X = %f\n", X );


		double currentCR, newCR;
		currentCR = newCR = 2.0;

		double noFactory, factory, withFactory, factoriesBuildingTime = 0.0f;

		do {
			//построили фабрику
			currentCR = newCR;

			//надо строить еще одну?
			noFactory = timeToCollectXCookiesWithRate(X, currentCR) + factoriesBuildingTime;
			//printf("no factory: %f, rate: %f\n", noFactory, currentCR);

			factory = timeToCollectXCookiesWithRate(C, currentCR);
			factoriesBuildingTime += factory;
			newCR += F;
			withFactory = timeToCollectXCookiesWithRate(X, newCR) + factoriesBuildingTime;

			// printf("time to build a factory : %f\n", factory);
			// printf("new rate : %f\n", newCR);
			// printf("With factory:%f\n", withFactory);

		}	
		while (noFactory > withFactory);

		output << noFactory;
		output << "\n";	
		// printf("Time: %f\n", noFactory);
	 }

	output.close();
	input.close();
	return 0;
}
double timeToCollectXCookiesWithRate(double X, double F) {
	if (F != 0) {
		double res = X / F;
		//printf("res = %f\n", res);
		return res;
	}
	return 0.0;
}

int getIntFromFile(ifstream &input) {
	string answer;
	getline (input, answer);
	return stoi(answer);
	return 0;
}

double getFloatFromFile(ifstream &input) {
	// string answer;
	// input >> answer;
	// // getline (input, answer);
	// float f = stof(answer);
	double f;
	input >> f; 
	return f;
}