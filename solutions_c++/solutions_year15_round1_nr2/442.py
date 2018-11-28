#include <fstream>

using namespace std;

ifstream fin ("B.in");
ofstream fout ("B.out");

long long UDiv (long long a, long long b)
{
	if (a <= 0) return 0;
	if (a % b == 0) return a / b;
	return a / b + 1;
}

int main ()
{
	int T;
	long long N, B;
	long long M[10000];
	fin >> T;
	for (int t = 1; t <= T; t++)
	{
		fin >> B >> N;
		for (long long i = 1; i <= B; i++)
			fin >> M[i];
		long long TMin = 0, TMax = 100000000000000000ll;
		while (TMin + 1 < TMax)
		{
			long long m = (TMin + TMax) / 2;
			long long avl = 0;
			for (long long i = 1; i <= B; i++)
				avl += UDiv (m, M[i]);
			if (avl >= N)
				TMax = m;
			else
				TMin = m;
		}
		long long svd = 0;
		for (long long i = 1; i <= B; i++)
			svd += UDiv (TMax - 1, M[i]);
		for (long long i = 1; i <= B; i++)
		{
			if (TMax % M[i] == 1 || M[i] == 1)
			{
				svd++;
				if (svd == N)
				{
					fout << "Case #" << t << ": " << i << endl;
					break;
				}
			}
		}
	}
}
