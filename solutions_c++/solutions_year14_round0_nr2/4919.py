// ConsoleApplication2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <iomanip>
#include <algorithm>

using namespace std;

const double defaultCookieRate = 2;

double calculateBest(double currentRate, double farmCost, double farmRate, double neededCookies)
{
	if ((farmCost + neededCookies) / (currentRate + farmRate) > neededCookies / currentRate)
	{
		return neededCookies / currentRate;
	}
	else
	{
		return min(neededCookies / currentRate, (farmCost / currentRate) + calculateBest(currentRate + farmRate, farmCost, farmRate, neededCookies));
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int numCases;
	int totalTime;
	int remainingTime;
	double farmCost;
	double farmRate;
	double neededCookies;

	in >> numCases;

	for (int i = 1; i <= numCases; i++)
	{
		in >> farmCost;
		in >> farmRate;
		in >> neededCookies;
		double time = calculateBest(defaultCookieRate, farmCost, farmRate, neededCookies);
		out << "Case #" << i << ": " << fixed << setprecision(7) << time << endl;
	}
	return 0;
}

