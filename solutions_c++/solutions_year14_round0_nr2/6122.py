// CookieClicker.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <iomanip>

using namespace std;

double Solve(double costOfFarm, double farmBoost, double target)
{
	double time = 0.0;
	double num = 0.0;
	double rate = 2.0;

	while (num < target)
	{
		double timeToCost = (costOfFarm - num) / rate;
		double timeToTarget = (target - num) / rate;
		double timeAfterFarm = timeToCost + target / (rate + farmBoost);
		if (timeToTarget <= timeAfterFarm)
		{
			num = target;
			time += timeToTarget;			
		}
		else
		{
			num = 0;
			time += timeToCost;
			rate += farmBoost;
		}
	}

	return time;
}

int _tmain(int argc, _TCHAR* argv [])
{
	ifstream ifs;
	ofstream ofs;
	ifs.open("c:\\GCJ_Inputs\\CookieClicker\\input.in", ifstream::in);
	ofs.open("c:\\GCJ_Inputs\\CookieClicker\\output.out", ifstream::out);

	if (!ifs)
	{
		cout << "Error reading input" << endl;
		return 0;
	}

	if (!ofs)
	{
		cout << "Error opening output" << endl;
		return 0;
	}

	cout << "STARTING" << endl;

	unsigned int numTests = 0;
	ifs >> numTests;

	for (int i = 0; i < numTests; ++i)
	{
		cout << "..";

		double C, F, X = 0.0;
		ifs >> C;
		ifs >> F;
		ifs >> X;

		double sol = Solve(C, F, X);
		ofs << "Case #" + std::to_string(i + 1) + ": ";
		ofs << std::fixed << std::setprecision(7) << sol << endl;
	}

	cout << endl;
	cout << "COMPLETE" << endl;

	ofs.close();
	ifs.close();

	return 0;
}

