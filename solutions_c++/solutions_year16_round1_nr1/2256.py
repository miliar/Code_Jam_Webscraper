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

	int i, j, Ncases;
	string theString;

	cin >> Ncases;

	for (i = 1; i <= Ncases; i++)
	{
		string sortString;
		cin >> theString;
		char prevChar = theString[0];
		sortString.append(1, prevChar);

		for (j = 1; j < theString.length(); j++)
		{
			char nxtChr = theString[j];
			if (nxtChr >= sortString[0])
			{
				sortString.insert(sortString.begin(), 1, nxtChr);
			}
			else
			{
				sortString.append(1, nxtChr);
			}
		}

		cout << "Case #" << i << ": " << sortString << endl;
	}

	return 0;
}

