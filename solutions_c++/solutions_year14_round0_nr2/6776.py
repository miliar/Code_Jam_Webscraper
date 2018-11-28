#include <windows.h>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace::std;

int main(int argc, char* argv[])
{
	ifstream cin(argv[1]);

	int nCount, numCase = 1;
	cin >> nCount;

	while (numCase <= nCount)
	{
		double C, F, X;
		double dx = 2.0, S = 0, t = 0;

		cin >> C >> F >> X;

		while (true)
		{
			double tNoFarm = (X - S) / dx;
			if (S < C)
			{
				double tToFarm = C / dx;
				if (tNoFarm <= tToFarm)
				{
					t += tNoFarm;
					break;
				}
				S += C;
				t += tToFarm;
			}
			else
			{
				double tFarm = (X - (S - C)) / (dx + F);
				if (tNoFarm <= tFarm)
				{
					t += tNoFarm;
					break;
				}
				S -= C;
				dx += F;
			}
		}

		cout << "Case #" << numCase << ": ";
		char s[32];
		sprintf(s, "%.7f", t);
		cout << s;
		cout << "\n";

		numCase++;
	}
	return 0;
}
