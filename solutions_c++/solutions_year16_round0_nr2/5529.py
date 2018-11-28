// TEST2.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <map>
#include <vector>
#include <math.h>

using namespace std;

char z_Value[200];
int iNoOfSteps = 0;

void flip(int iUpTo)
{
	iNoOfSteps++;
}

void process(int iUpTo, char cExpected)
{
	if (iUpTo < 0)
		return;

	for (int i = iUpTo; i >= 0; --i)
	{
		if (z_Value[i] != cExpected)
		{
			if (cExpected == '+')
				process(i - 1, '-');
			else
				process(i - 1, '+');

			flip(i);
			return;
		}
	}
}

int main()
{
	ifstream oFileIn("aa.in");
	ofstream oFileOut("bb.out");

	int iT = 0;
	oFileIn >> iT;

	for (int i = 1; i <= iT; ++i)
	{
		string sValue;
		oFileIn >> sValue;

		strncpy(z_Value, sValue.c_str(), 199);
		iNoOfSteps = 0;

		process(sValue.length() - 1, '+');


		oFileOut << "Case #" << i << ": " << iNoOfSteps << "\n";

	}

	oFileIn.close();
	oFileOut.close();

	return 0;
}

