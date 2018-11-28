#include <fstream>

using namespace std;

ifstream fin ("C.in");
ofstream fout ("C.out");

int F[2000];

int main ()
{
	int T;
	int N;
	fin >> T;
	for (int t = 1; t <= T; t++)
	{
		fin >> N;
		for (int i = 1; i <= N; i++)
		{
			fin >> F[i];
//			if (t == 37) fout << F[i] << endl;
		}
		int ans = 0;
		int Lans[2000] = {0};
		for (int i = 1; i <= N; i++)
		{
			int MT[2000] = {0};
			int l = 1;
			MT[i] = l;
			int p = F[i];
			while (MT[p] == 0)
			{
				l++;
				MT[p] = l;
				p = F[p];
			}
			int CC = l - MT[p] + 1;
			if (CC == 2)
			{
				if (Lans[p] < l) Lans[p] = l;
			}
			if (ans < CC) ans = CC;
		}
		int tt = 0;
		for (int i = 1; i <= N; i++)
			if (F[F[i]] == i)
				tt += Lans[i] + Lans[F[i]] - 2;
		if (ans < tt / 2) ans = tt / 2;
		fout << "Case #" << t << ": " << ans << endl;
	}
}

