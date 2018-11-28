// StandingOvation.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int computeValue(int Smax, string S)
{
	int currentNeed = 0;
	int currentSum = S[0] - '0';
	for (int i = 1; i <= Smax; i++)
	{			
		if (currentSum < i && S[i] != '0')
		{
			currentNeed += i - currentSum;
			currentSum +=  i - currentSum;
		}

		currentSum += (int)(S[i] - '0');
	}

	return currentNeed;
}


int main()
{
	ifstream input;
	ofstream output;

	input.open("standinOvationL.in");
	output.open("standinOvationL.txt");

	int Tests = 0;
	int Smax;
	string S;
	input >> Tests;

	for (int i = 1; i <= Tests; i++)
	{
		input >> Smax;
		input >> S;

		int result = computeValue(Smax, S);
		output << "Case #" << i << ": " << result << "\n";
	}
	
	cin >> S;

	input.close();
	output.close();
	return 0;
}

