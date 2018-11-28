// GCJ.cpp : Defines the entry point for the console application.
//
#include <cstdio>
#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <string>
#include <math.h>
#include <functional>

//#define verbose

using namespace std;

int main()
{
	// First let's read the file
	freopen("gcj.in", "r", stdin);
	freopen("gcj.out", "w", stdout);

	int i, j, k, Ncases, intervals;
	vector <short> theIntervals;

	cin >> Ncases;

	// Test cases
	for (i=0; i<Ncases; i++)
	{
		long min1 = 0, min2 = 0;
		short maxGap = 0, lastShrooms = 0;
		cin >> intervals;
		for (j = 0; j<intervals; j++)
		{
			short shrooms;
			cin >> shrooms;
			theIntervals.push_back(shrooms);

			// We can figure the method 1 straight away
			if ((lastShrooms - shrooms) > 0)
			{
				min1 += (lastShrooms - shrooms);
			}
			// While we are here, lets find the max gap for method 2
			if ((lastShrooms - shrooms) > maxGap)
			{
				maxGap = lastShrooms - shrooms;
			}
			lastShrooms = shrooms;
		}

		// Ok so we have the data in, now what is the algorithm to solve the problem
		//   Go through and see the min eaten by the rate
		for (j = 0; j < intervals-1; j++)
		{
			if (theIntervals[j] >= maxGap)
			{
				min2 += maxGap;
			}
			else
			{
				min2 += theIntervals[j];
			}
		}

		cout << "Case #" << i + 1 << ": " << min1 << " " << min2 << endl;
		theIntervals.clear();
	}

	return 0;
}

