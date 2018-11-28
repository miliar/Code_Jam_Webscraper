// D.cpp : Defines the entry point for the console application.
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
	ifstream fi("d.in");
	ofstream fo("d.out");

	int t;
	fi >> t;

	for (int i = 0; i < t; i++)
	{
		int x, r, c;
		fi >> x >> r >> c;
		bool gabriel = false;
		if (x == 1)
		{
			gabriel = true;
		}
		else if (x == 2)
		{
			if ((r*c) % 2 == 0)
			{
				gabriel = true;
			}
		}
		else if (x == 3)
		{
			if (((r == 3) || (c == 3)) && (r*c > 3))
			{
				gabriel = true;
			}
		}
		else
		{
			if (r*c >= 12)
			{
				gabriel = true;
			}
		}

		fo << "Case #" << i + 1 << ": " << ((gabriel) ? "GABRIEL" : "RICHARD") << endl;
	}

	fi.close();
	fo.close();

	return 0;
}

