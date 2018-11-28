// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fi("a.in");
	ofstream fo("a.out");

	int t;
	fi >> t;

	for (int i = 0; i < t; i++)
	{
		int smax = 0;
		string str;
		fi >> smax;
		getline(fi, str);

		int cnt = 0;
		int cur_standed = 0;
		for (int j = 1; j < str.length() - 1; j++)
		{
			cur_standed += str[j] - 48;
			if (cur_standed < j)
			{
				cnt += j - cur_standed;
				cur_standed = j;
			}
		}
		fo << "Case #" << i+1 << ": " << cnt << endl;
	}

	fi.close();
	fo.close();

	return 0;
}

