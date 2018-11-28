// QualProblemB.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <stdio.h>
#include <iostream>

using namespace std;

int P[1000];
int main(int argc, char* argv[])
{
//	freopen("B-small-attempt0.in", "r", stdin);
	//freopen("in.txt", "r", stdin);
//	freopen("Bsmall.out", "w", stdout);

	freopen("B-large.in", "r", stdin);
	freopen("BLarge.out", "w", stdout);
	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test)
	{
		int D;
		cin >> D;
		for (int i = 0; i < D; ++i)
			cin >> P[i];
		int res = 1000;
		for (int val = 1; val <= 1000; ++val)
		{
			int cutcount = 0;
			for (int i = 0; i < D; ++i)
				cutcount += (P[i] - 1) / val;
			if (val + cutcount < res)
				res = val + cutcount;
			if (cutcount == 0)
				break;
		}
		cout << "Case #" << test << ": " << res << endl;
	}
	return 0;
}

