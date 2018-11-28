#include <fstream>

using namespace std;

ifstream fin ("C.in");
ofstream fout ("C.out");

long long calc[5][5] = {
				{0, 0, 0, 0, 0},
				{0, 1, 2, 3, 4},
				{0, 2, -1, 4, -3},
				{0, 3, -4, -1, 2},
				{0, 4, 3, -2, -1}};

long long Abs (long long x)
{
	if (x < 0) return -x;
	return x;
}

long long Calc (long long i, long long j)
{
	if (i < 0 && j < 0) return calc[-i][-j];
	if (i < 0) return -calc[-i][j];
	if (j < 0) return -calc[i][-j];
	return calc[i][j];
}

main ()
{
	long long T;
	char str[1000000];
	fin >> T;
	for (long long t = 1; t <= T; t++)
	{
		long long L, X;
		fin >> L >> X;
		long long s = 1;
		for (long long i = 0; i < L; i++)
		{
			fin >> str[i];
			s = Calc (s, str[i] - 'i' + 2);
		}
		long long k = X, p = s, ans = 1;
		while (k > 0)
		{
			if (k % 2 == 1)
				ans = Calc (ans, p);
			k /= 2;
			p = Calc (p, p);
		}
		if (ans != -1)
		{
			fout << "Case #" << t << ": NO" << endl;
			continue;
		}
		long long tot = 1, ch = 2;
		long long Len = (256 * L < X * L) ? 16 * L : L * X;
		for (long long i = 0; i < Len; i++)
		{
			tot = Calc (tot, str[i % L] - 'i' + 2);
			if (tot == ch)
			{
				if (ch == 2)
				{
					ch++;
					tot = 1;
					continue;
				}
				if (ch == 3)
				{
					fout << "Case #" << t << ": YES" << endl;
					goto LoopEnd;
				}
			}
		}
		fout << "Case #" << t << ": NO" << endl;
		LoopEnd:;
	}
}
