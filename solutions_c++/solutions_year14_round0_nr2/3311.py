// MagicTrickGCJ2014.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <iomanip>     
#include <string>

using namespace std;

double findTime(double C, double F, double X);

int _tmain(int argc, _TCHAR* argv[])
{
	int testCount;//number of test cases
	double C, F, X;//input variables
	int i;//

	ifstream inputfile("B-small-attempt0.IN");
	ofstream outputFile("Output.OUT");

	outputFile.precision(7);
	outputFile.setf(ios::fixed, ios::floatfield);

	if (inputfile.is_open() && outputFile.is_open())
	{
		inputfile >> testCount;

		for (i = 0; i < testCount; i++)
		{
			inputfile >> C >> F >> X;
			outputFile << "Case #" << i + 1 << ": " << findTime(C, F, X) << "\n";
		}
	}

	inputfile.close();
	outputFile.close();

	system("PAUSE");

	return 0;
}

double findTime(double C, double F, double X)
{
	double prod(2.0); //cookies per second
	double totalTime(0), curTime(0), prevTime(0);//all time
	bool found = false;//true if soved

	prevTime = X / prod;

	do
	{
		totalTime += C / prod;
		prod += F;
		curTime = X / prod + totalTime;
		if (curTime < prevTime)
			prevTime = curTime;
		else
			found = true;

	} while (!found);
		
	return prevTime;
}