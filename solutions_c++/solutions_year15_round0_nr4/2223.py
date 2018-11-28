#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;
ifstream fin("t.txt");
ofstream fout("out.txt");
int l;
int x,maxim;
char s[10005];
int  t[5][5];
int sol[10005];
int main()
{
	t[1][1] = 1;  t[1][2] = 2;  t[1][3] = 3;  t[1][4] = 4;
	t[2][1] = 2;  t[2][2] = -1; t[2][3] = 4;  t[2][4] = -3;
	t[3][1] = 3;  t[3][2] = -4; t[3][3] = -1; t[3][4] = 2;
	t[4][1] = 4;  t[4][2] = 3;  t[4][3] = -2;  t[4][4] = -1;
	int T;
	fin >> T;
	for (int k = 1; k <= T; k++)
	{
		 maxim = 0;
		fout << "Case #" << k << ": ";
		fin >> l >> x;
		fin >> s;
		for (int i = 0; i < l; i++)
		{
			if (s[i] == 'i') sol[i] = 2;
			if (s[i] == 'j') sol[i] = 3;
			if (s[i] == 'k') sol[i] = 4;
		}
		int n=l;
		for (int i = 1; i < x;i++)
			for (int j = 0; j < l; j++)
				sol[n++] = sol[j];
			bool ok = 0;
		for (int i = 0; i < n - 1; i++)
		{
			for (int j = i + 1; j < n; j++)
			{
				int ans = 1;
				for (int k = 0; k <= i; k++) ans = t[ans][sol[k]];
				if (ans == 2)
				{
					ans = 1;
					for (int k = i+1; k <= j; k++) ans = t[ans][sol[k]];
					if (ans == 3)
					{
						ans = 1;
						for (int k = j + 1; k <n; k++) ans = t[ans][sol[k]];
						if (ans == 4) { ok = 1; break; }
					}
				}
			}
			if (ok == 1) break;

		}
		if (ok == 1) fout << "YES" << "\n";
		else fout << "NO" << "\n";
	}
}