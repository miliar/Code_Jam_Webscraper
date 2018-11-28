// gcj_d.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <vector>
#include <fstream>

using namespace std;

struct size
{
	size(int ww, int hh) : w(ww), h(hh)
	{		
	}
	int w;
	int h;
};

int min(int X, int Y)
{
	return X < Y ? X : Y;
}

int max(int X, int Y)
{
	return X > Y ? X : Y;
}

bool ProcessTestCase(int X, int R, int C)
{
	bool result = true;
	if (X > 6 || X <= 0)
		result = false;
	else	
	{
		if ((R*C) % X != 0)
		{
			result = false;
		}
		else
		{
			if (X <= max(R, C))
			{
				{
					int minSQ = min(R, C);
					int XX = (X + 1) / 2;
					if (XX > minSQ)
						result = false;
					if (X > 3 && XX >= min(R, C))
						result = false;
				}
			}
			else
			{
				result = false;
			}
		}
	}
	return result;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream input("input.txt");
	ofstream output("output.txt");
	int T = 0;
	input >> T;
	for (int counter = 0; counter < T; ++counter)
	{
		int X = 0, R = 0, C = 0;
		input >> X;
		input >> R;
		input >> C;
		output << "Case #" << counter + 1 << ": " << (ProcessTestCase(X, R, C) ? "GABRIEL" : "RICHARD") << "\r\n";
	}
	input.close();
	output.flush();
	output.close();
	return 0;
}

