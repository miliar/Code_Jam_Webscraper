#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
using namespace std;

bool toBuyNewFarm(double farmCost, double cookiesPerFarm, double cookiesToWin, double* curCPS, double* totalTime)
{
	double noBuy;
	double yesBuy;

	noBuy = (cookiesToWin - farmCost) / *curCPS;
	yesBuy = cookiesToWin / (*curCPS + cookiesPerFarm);

	if(noBuy < yesBuy)
	{
		*totalTime += cookiesToWin / *curCPS;
		return false;
	}
	else
	{
		*totalTime += farmCost / *curCPS; 
		*curCPS += cookiesPerFarm;
		return true;
	}
}

int main(int argc, char *argv[])
{
	ifstream input(argv[1]);
	//input.open("test.txt");
	if(!input.is_open())
	{
		cout << "Error Opening";
		return 0;
	}

	int total;
	input >> total;

	double farmCost;
	double cookiesPerFarm;
	double cookiesToWin;
	double totalTime = 0;
	double curCPS = 2;

	for(int count = 0; count < total; count++)
	{
		cout << "Case #" << count + 1 << ": ";
		
		input >> farmCost;
		input >> cookiesPerFarm;
		input >> cookiesToWin;

		while(toBuyNewFarm(farmCost, cookiesPerFarm, cookiesToWin, &curCPS, &totalTime))
		{
			continue;
		}

		cout << fixed << showpoint << setprecision(7); 
		cout << totalTime << endl;
		curCPS = 2;
		totalTime = 0;
	}
	return 0;
}