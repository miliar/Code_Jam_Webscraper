// ConsoleApplication3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;




int _tmain(int argc, _TCHAR* argv[])
{
	int round;
	ifstream testfile("B-large.in");
	testfile >> round;
	ofstream outputfile("result.out");

	double C, F, X;
	
	for (int i = 1; i <= round; i++)
	{
		testfile >> C;
		testfile >> F;
		testfile >> X;
		double rate = 2;

		double totalCost = 0;
		while (true)
		{
			float originalTime = X / rate;
			float alterTime = C / rate + X / (rate + F);

			if (originalTime < alterTime)
				break;
			//buy a farm
			totalCost += C / rate;
			rate += F;
		}

		totalCost += X / rate;
		outputfile << "Case #" << i << ": " << fixed<< setprecision(7)<< totalCost << endl;
	}

	testfile.close();
	outputfile.close();

}


