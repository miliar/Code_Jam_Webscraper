// codeJame2013_1A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include "vector"
#include "string"
#include "set"
#include "sstream"
#include "algorithm"
#include "cmath"
#include "cassert"
#include "iostream"
#include <fstream>

using namespace std;

#define int64 long long

const double PI = 3.14159265359;

int _tmain(int argc, _TCHAR* argv[])
{
	ofstream fout("out.txt");
	ifstream fin("in.txt");
	int T;
	fin >> T;

	for (int t = 0; t < T; ++t)
	{
		int64 r, paintT;

		fin >> r >> paintT;
		int64 paintUsed = 0;
		int64 currentWhiteR = r;
		int64 drawRings = 0;
		//double n = paintT * 2 / (2 + )

		while (true)
		{
			int64 area = 2 * currentWhiteR + 1;
			paintUsed += area;
			currentWhiteR +=2;
			if (paintUsed > paintT)
			{
				break;
			}
			drawRings++;
		}
		
		fout << "Case #" << t + 1 <<": " << drawRings << endl;
	}

	return 0;
}

