// test.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <sstream>
#include <string>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
 
using namespace std;

std::ifstream infile("E:\\maye\\test4\\Debug\\in.txt");
std::ofstream outfile("E:\\maye\\test4\\Debug\\out.txt");

int T;

void doit()
{
	infile >> T;
	cout << "T = " << T << endl;
	double delta = 1e-8;
	for (int i = 0; i < T; ++i)
	{
		int N;
		infile >> N;

		vector<double> s1(N, 0);
		vector<double> s2(N, 0);

		for (int j = 0; j < N; ++j)
			infile >> s1[j];

		for (int j = 0; j < N; ++j)
			infile >> s2[j];

		sort(s1.begin(), s1.end());
		sort(s2.begin(), s2.end());

		int r1 = 0;
		int r2 = 0;

		int x = 0; 
		int y = 0;
		int high = N - 1;

		while (x < N && y <= high)
		{
			if (s1[x] - s2[y] > delta)
			{
				++r1;
				++x;
				++y;
			}
			else
			{
				++x;
				--high;
			}
		}

		x = N - 1;
		y = N - 1;
		int low = 0;

		while (x >= 0 && y >= low)
		{
			if (s1[x] - s2[y] >  delta)
			{
				++r2;
				--x;
				++low;
			}
			else
			{
				--x;
				--y;
			}
		}
		 
		
		outfile << "Case #" << i + 1 << ": ";
		outfile << r1 <<" "<< r2 << endl;
	}
}


int _tmain(int argc, _TCHAR* argv[])
{
	doit();
	return 0;
}

