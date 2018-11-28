// GCJ.cpp : Defines the entry point for the console application.
//
#include <cstdio>
#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <string>
#include <math.h>

//#define verbose

using namespace std;

int main()
{
	// First let's read the file
	freopen("gcj.in", "r", stdin);
	freopen("gcj.out", "w", stdout);

	int i, j, k, Ncases, maxShy, poss;
	vector <short> cars;

	cin >> Ncases;

	// Test cases
	for (i=0; i<Ncases; i++)
	{
		cin >> maxShy;
		for (j = 0; j<maxShy+1; j++)
		{
			short tmpPeeps;
			char oneChar;
			cin >> oneChar;
			tmpPeeps = atoi(&oneChar);
			cars.push_back(tmpPeeps);
		}

		// Ok so we have the data in, now what is the algorithm to solve the problem?
		//  For each shyness level, there needs to be right number of predecessors
		//    If there are no zeros, then it must work.  For each zero, one peep must 
		//    be added (it can't be that simple).  The trick is to keep a running total
		//    as you iterate through the list, as you may have extras.  So what is the
		//    criteria?  Add up the peeps as you go and whenever peeps are needed, add 
		//    the shortfall to the running total.
		//cout << "  Peeps:";
		short addedPeeps = 0, shyLevel = 0, runningTot = 0;
		for each (short peep in cars)
		{
			if (runningTot < shyLevel)
			{
				short tmpDiff = shyLevel - runningTot;
				addedPeeps += tmpDiff;
				runningTot += peep + tmpDiff;
			}
			else
			{
				runningTot += peep;
			}
			shyLevel++;
		}
		cout << "Case #" << i + 1 << ": " << addedPeeps << endl;
		cars.clear();
	}

	return 0;
}

