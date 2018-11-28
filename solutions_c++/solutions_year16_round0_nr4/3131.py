// D.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fi("d.in");
	ofstream fo("d.out");

	int t;
	fi >> t;
	for (int i = 0; i < t; i++)
	{
		int k, c, s;
		fi >> k >> c >> s;
		fo << "Case #" << i + 1 << ": ";
		if (k == s)
		{
			for (int j = 0; j < s - 1; j++)
			{
				fo << j+1 << " ";
			}
			fo << s << endl;
		}
		else
		{
			fo << "IMPOSSIBLE" << endl;
		}
	}

	fi.close();
	fo.close();

	return 0;
}

