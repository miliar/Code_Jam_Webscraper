// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <algorithm>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin("B.in");
	ofstream fout("B.out");

	fout.precision(15);

	int T;
	fin >> T;

	for (int t = 1; t <= T; t++)
	{
		fout << "Case #" << t << ": ";

		long double C, F, X;
		fin >> C >> F >> X;

		long double Res = LDBL_MAX;

		long double Cookies = 0l;
		long double CPS = 2.0;
		long double Time = .0;

		for (;;CPS += F)
		{
			if (Res > Time + (X - Cookies) / CPS)
				Res = Time + (X - Cookies) / CPS;
			else
				break;
			
			Cookies -= C;
			if (Cookies < 0)
			{
				Time += -1*Cookies/CPS;
				Cookies = 0;
			}
		}

		fout << Res << endl;
	}

	return 0;
}

