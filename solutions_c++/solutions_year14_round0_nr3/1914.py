#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;
const int MAX = 7;
int a[MAX][MAX], d[MAX][MAX];
char ans[MAX][MAX];
bool mark[MAX][MAX];
int dx[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dy[8] = {-1, 0, 1, -1, 1, -1, 0, 1};
void dfs(int x, int y)
{
	mark[x][y] = true;
	if (d[x][y])
		return;
	for (int k = 0; k < 8; k++)
	{
		int i = x + dx[k];
		int j = y + dy[k];
		if (!mark[i][j])
			dfs(i, j);
	}
}
int main()
{
	ifstream fin("C.in");
	ofstream fout("cs.out");
	int t;
	fin >> t;
	for (int k = 1; k <= t; k++)
	{
		for (int i = 0; i < MAX; i++)
			for (int j = 0; j < MAX; j++)
				d[i][j] = 1;
		int r, c, m;
		fin >> r >> c >> m;
		cout << k << " :  " << r << " " << c << " " << m << endl;
		int ansm = -1, ansx = -1, ansy = -1;
		for (int mask = 0; mask < (1 << (r * c)); mask++)
			if (__builtin_popcount(mask) == m)
			{
				memset(a, 0, sizeof(a));
				for (int i = 1; i <= r; i++)
					for (int j = 1; j <= c; j++)
						if ((1 << ((i - 1) * c + j - 1)) & mask)
							a[i][j] = 1;
				for (int i = 1; i <= r; i++)
					for (int j = 1; j <= c; j++)
					{
						d[i][j] = 0;
						for (int k = 0; k < 8; k++)
							d[i][j] += a[i + dx[k]][j + dy[k]];
						d[i][j] += a[i][j];
					}
				for (int i = 1; i <= r; i++)
					for (int j = 1; j <= c; j++)
						if (!a[i][j])
						{
							memset(mark, false, sizeof(mark));
							dfs(i, j);
							bool good = true;
							for (int x = 1; x <= r; x++)
								for (int y = 1; y <= c; y++)
									if (!mark[x][y] && !a[x][y])
										good = false;
							if (good == true)
							{
								ansm = mask;
								ansx = i;
								ansy = j;
							}
						}
				if (ansm != -1)
					break;
			}
		fout << "Case #" << k << ":" << endl;
		if (ansm == -1)
			fout << "Impossible" << endl;
		else
		{
			memset(a, 0, sizeof(a));
			for (int i = 1; i <= r; i++)
				for (int j = 1; j <= c; j++)
					if ((1 << ((i - 1) * c + j - 1)) & ansm)
						a[i][j] = 1;
			for (int i = 1; i <= r; i++)
				for (int j = 1; j <= c; j++)
					if (a[i][j])
						ans[i][j] = '*';
					else
						ans[i][j] = '.';
			ans[ansx][ansy] = 'c';
			for (int i = 1; i <= r; i++)
			{
				for (int j = 1; j <= c; j++)
					fout << ans[i][j];
				fout << endl;
			}
		}
	}
	return 0;
}
/*
..
..
.c
..
*.
*/
