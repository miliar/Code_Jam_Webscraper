// Standing Ovation.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream f("A-large.in");
ofstream g("output.txt");

int S, T, S_m, ct;
string st;

int _tmain(int argc, _TCHAR* argv[])
{
	f >> T;

	for (int i = 1; i <= T; i++)
	{
		f >> S_m;
		f >> st;
		ct = 0;
		S = 0;
		
		for (int j = 0; j <= S_m; j++)
		{
			if (j > S)
			{
				ct++;
				S++;
			}
			S += st[j] - 48;
		}
		g << "Case #" << i << ": " << ct << endl;
	}

	f.close();
	g.close();
	return 0;
}

