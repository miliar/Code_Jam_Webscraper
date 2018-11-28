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

	int i, j, k, Ncases;
	int row, col, width;
	//vector <short> theDenoms;

	cin >> Ncases;

	// Test cases
	for (i=0; i<Ncases; i++)
	{
		cin >> row >> col >> width;

		// For the small input, this should be straightforward, with only 1 row
		short find = ((col / width) + (width - 1)) * row;
		if ((width > 1) && ((col % width) > 0))
			find++;

		cout << "Case #" << i + 1 << ": " << find << endl;
		//theDenoms.clear();
	}

	return 0;
}

