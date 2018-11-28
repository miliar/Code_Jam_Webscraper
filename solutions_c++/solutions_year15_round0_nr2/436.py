#include <fstream>

using namespace std;

ifstream fin ("B.in");
ofstream fout ("B_.out");

int UpperDivide (int x, int y)
{
	if (x % y > 0) return x / y + 1;
	return x / y;
}

main ()
{
	int T;
	int D, P[2000];
	fin >> T;
	for (int t = 1; t <= T; t++)
	{
		fin >> D;
		for (int i = 1; i <= D; i++) fin >> P[i];
		int ans, bestAns = 1000;
		for (int i = 1; i <= 1000; i++)
		{
			ans = 0;
			for (int j = 1; j <= D; j++)
				ans += (UpperDivide (P[j], i) - 1);
			if (bestAns > ans + i) bestAns = ans + i;
		}
		fout << "Case #" << t << ": " << bestAns << endl;
	}
}
