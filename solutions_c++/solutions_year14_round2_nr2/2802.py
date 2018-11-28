// Round1B.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

using namespace std;

bool Lottery()
{
	ifstream fin("B-small-attempt0 (1).in");
	ofstream fout("outb.txt");

	int T = 0;
	fin >> T;

	for (int t = 0; t < T; t++)
	{
		unsigned long A, B, K;
		fin >> A >> B >> K;

		unsigned long n = 0;

		for (unsigned long i = 0; i < A; i++)
		{
			for (unsigned long j = 0; j < B; j++)
			{
				unsigned long num = i & j;
				if (num < K)
				{
					n++;
				}
			}
		}

		cout << "Case #" << t + 1 << ": " << n << endl;
		fout << "Case #" << t + 1 << ": " << n << endl;

	}

	return true;
}

int _tmain(int argc, _TCHAR* argv[])
{
	Lottery();

	return 0;
}

