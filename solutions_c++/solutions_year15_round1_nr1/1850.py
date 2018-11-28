// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fi("a.in");
	ofstream fo("a.out");

	int t;
	fi >> t;

	for (int i = 0; i < t; i++)
	{
		int n;
		fi >> n;
		int m[10000];
		int min1 = 0, min2 = 0;
		int max_eaten = 0;
		for (int j = 0; j < n; j++)
		{
			fi >> m[j];

			if (j > 0)
			{
				if (m[j] < m[j - 1])
				{
					if (m[j - 1] - m[j] > max_eaten)
					{
						max_eaten = m[j - 1] - m[j];
					}
					min1 += m[j - 1] - m[j];
				}
			}
		}

		for (int j = 1; j < n; j++)
		{
			min2 += min(m[j - 1], max_eaten);
		}

		fo << "Case #" << i + 1 << ": " << min1 << " " << min2 << endl;
	}

	fi.close();
	fo.close();

	return 0;
}

