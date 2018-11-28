// GCJ.cpp : Defines the entry point for the console application.
//
#include <cstdio>
#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <math.h>

//#define verbose

using namespace std;

int main()
{
	// First let's read the file
	freopen("gcj.in", "r", stdin);
	freopen("gcj.out", "w", stdout);

	int i, j, k, Ncases, oldWay, newWay, tixLim, numPairs=0;

	cin >> Ncases;

	// Test cases
	for (i=0; i<Ncases; i++)
	{
		cin >> oldWay >> newWay >> tixLim;
		numPairs = 0;
		for(j=0; j<oldWay; j++)
		{
			for(k=0; k<newWay; k++)
			{
				int tmp = k&j;
				if( (tmp) < tixLim )
				{
					numPairs++;
					//cout << j << ":" << k << ":" << tmp << "-";
				}
			}
		}
		//cout << endl;
		cout << "Case #" << i+1 << ": " << numPairs << endl;
	}

	return 0;
}

