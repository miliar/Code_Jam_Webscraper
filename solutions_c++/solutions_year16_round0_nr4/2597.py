// prob3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include <cassert>
#include <bitset>
#include <cmath>
#include <vector>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	FILE* in = NULL;
	FILE* out = NULL;
	errno_t fin = freopen_s(&in, "D-small-attempt0.in", "r", stdin);
	assert(0x0 == fin);
	errno_t fout = freopen_s(&out, "D-small.out", "w", stdout);
	assert(0x0 == fout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": ";
		unsigned int K, C, S;
		cin >> K >> C >> S;
		if (K != S)
		{
			cout << "*************************** ERROR ************************************\n";
		}
		else
		{
			for (unsigned int i = 1; i <= S; ++i)
			{
				cout << i << " ";
			}
			cout << endl;
		}
	}
	return 0;
}
