// GoogleCodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

const char* MULTICARD  = "Bad magician!";
const char* NOCARD = "Volunteer cheated!";

string Solve(int ans1, int grid1[4][4], int ans2, int grid2[4][4])
{
	string result = NOCARD;
	int numMatch = 0;
	int lastMatch = 0;
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			if (grid1[ans1][i] == grid2[ans2][j])
			{
				++numMatch;
				lastMatch = grid1[ans1][i];
			}
		}
	}
	
	if (numMatch > 1)
	{
		result = MULTICARD;
	}
	else if (numMatch == 1)
	{
		result = std::to_string(lastMatch);
	}

	return result;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream ifs;
	ofstream ofs;
	ifs.open("c:\\GCJ_Inputs\\MagicTrick\\input.in", ifstream::in);
	ofs.open("c:\\GCJ_Inputs\\MagicTrick\\output.out", ifstream::out);

	if (!ifs)
	{
		cout << "Error reading input" << endl;
		return 0;
	}

	cout << "STARTING" << endl;

	unsigned int numTests = 0;
	ifs >> numTests;
	
	for (int i = 0; i < numTests; ++i)
	{
		cout << "..";

		int ans1 = -1;
		int grid1[4][4] = { 0, };
		int ans2 = -1;
		int grid2[4][4] = { 0, };

		ifs >> ans1;
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				ifs >> grid1[i][j];
			}
		}

		ifs >> ans2;
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				ifs >> grid2[i][j];
			}
		}

		string sol = Solve(ans1-1, grid1, ans2-1, grid2);

		ofs << "Case #" + std::to_string(i + 1) + ": " + sol << endl;
	}

	cout << endl;
	cout << "COMPLETE" << endl;

	ofs.close();
	ifs.close();

	return 0;
}

