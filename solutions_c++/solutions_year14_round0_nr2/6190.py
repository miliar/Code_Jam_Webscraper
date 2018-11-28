// GCJ.cpp : Defines the entry point for the console application.
//
#include <cstdio>
#include <iostream>
using namespace std;

int main()
{
	// First let's read the file
	freopen("gcj.in", "r", stdin);
	freopen("gcj.out", "w", stdout);

	int k, Ncases;

	cin >> Ncases;

	double cost, addtl, goal;
	double baseRate = 2.0, currRate, nextRate, remAtRate, remAtNextRate;
	double accruedCost = 0.0;
	char blah[100];

	// Outer loop is the number of cases
	for (k=0; k<Ncases; k++)
	{
		cin >> cost >> addtl >> goal;

		currRate = baseRate;
		nextRate = currRate + addtl;
		remAtRate = goal / currRate;
		remAtNextRate = (goal / nextRate) + (cost / currRate);
		accruedCost = 0.0;
		memset(blah, 0x00, 100);

		while(remAtRate > remAtNextRate)
		{
			accruedCost += cost / currRate;
			currRate = nextRate;
			nextRate = currRate + addtl;
			remAtRate = goal / currRate;
			remAtNextRate = (goal / nextRate) + (cost / currRate);
		}
		accruedCost += goal / currRate;
		sprintf(blah, "%.7f", accruedCost);
		cout << "Case #" << k+1 << ": " << blah << endl;
	}

	return 0;
}

