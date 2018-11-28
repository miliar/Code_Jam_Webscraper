// Mushroom Monster.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

ifstream f("A-large (1).in");
ofstream g("output.txt");

int T, n;
long S, x, most;


int _tmain(int argc, _TCHAR* argv[])
{
	f >> T;
	vector <long> M;

	for (int i = 1; i <= T; i++)
	{
		S = 0;
		most = 0;
		f >> n;
		f >> x;
		M.push_back(x);
		for (int j = 1; j < n; j++)
		{
			f >> x;
			M.push_back(x);
			if (x < M[j - 1])
			{
				S += M[j - 1] - x;
				if (M[j - 1] - x > most)
					most = M[j - 1] - x;
			}
		}
		g << "Case #" << i << ": " << S << " ";

		S = 0;

		for (int j = 0; j < n-1; j++)
		{
			if (M[j] < most)
				S += M[j];
			else
				S += most;
		}

		g << S << endl;

		M.clear();
		M.shrink_to_fit();
	}

	f.close();
	g.close();
	return 0;
}

