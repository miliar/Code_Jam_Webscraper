// gcj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <vector>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream ifstr("B-large.in");
	ofstream ofstr("B-large.out");
	int T;
	ifstr >> T;
	for (int t = 0; t < T; ++t)
	{
		int N, M;
		ifstr >> N >> M;
		vector<vector<int>> lawn(N, vector<int>(M));
		for (int n = 0; n < N; ++n)
			for (int m = 0; m < M; ++m)
				ifstr >> lawn[n][m];
		bool f = true;
		for (int n = 0; n < N; ++n)
			for (int m = 0; m < M; ++m)
			{
				int value = lawn[n][m];
				bool f1 = false;
				for (int i = 0; i < N; ++i)
					if (lawn[i][m] > value)
					{
						f1 = true;
						break;
					}
				bool f2 = false;
				for (int i = 0; i < M; ++i)
					if (lawn[n][i] > value)
					{
						f2 = true;
						break;
					}
				if (f1 && f2)
				{
					f = false;
					goto output;
				}
			}
output:
			ofstr << "Case #" << t + 1 << ": " << (f ? "YES" : "NO") << endl;
	}

	return 0;
}

