// codejam2015_r1_q1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	fstream fs; fs.open("A-large.in");
	int n;
	fs >> n;

	fstream fout; fout.open("A-large.out", ios::out);

	for (int i = 0; i < n; i++)
	{
		int sMax;
		char audiences[2000];
		fs >> sMax;
		char c;
		fs.get(c);
		fs.getline(audiences, 2000);
				
		int currentStandUp = audiences[0] - '0';
		int need = 0;
		for (int i = 1; i <= sMax; i++)
		{
			if (currentStandUp < i)
			{
				int t = i - currentStandUp;
				currentStandUp = i;
				need += t;
			}
			currentStandUp += (audiences[i] - '0');
		}

		if (i + 1 != n)
			fout << "Case #" << i + 1 << ": " << need << endl;
		else
			fout << "Case #" << i + 1 << ": " << need;
	}

	fs.close();
	fout.close();
	return 0;
}

