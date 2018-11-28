#include <fstream>

using namespace std;

ifstream fin ("A.in");
ofstream fout ("A.out");

int UDiv (int a, int b)
{
	if (a % b == 0) return a / b;
	return a / b + 1;
}

int main ()
{
	int T;
	int N, M[10000];
	fin >> T;
	for (int t = 1; t <= T; t++)
	{
		fin >> N;
		int ans1 = 0, ans2 = 0, maxd = 0;
		for (int i = 1; i <= N; i++)
			fin >> M[i];
		for (int i = 2; i <= N; i++)
		{
			if (M[i - 1] - M[i] > 0)
			{
				ans1 += M[i - 1] - M[i];
				if (maxd < M[i - 1] - M[i])
					maxd = M[i - 1] - M[i];
			}
		}
//		int inv = UDiv (maxd, 10);
		for (int i = 2; i <= N; i++)
		{
			if (M[i - 1] < maxd)
				ans2 += M[i - 1];
			else
				ans2 += maxd;
		}
		fout << "Case #" << t << ": " << ans1 << " " << ans2 << endl;
	}
	return 0;
}
