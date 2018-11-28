#pragma comment(linker, "/STACK:268435456")
#include<cstdio>
#include<iostream>
using namespace std;
const int MAX_N = 10;

int sm[MAX_N][MAX_N];
int b, m;
int flag = 1;
int used[MAX_N];
int xd[MAX_N];
int glob_mask = 0;

void dfs1(int v)
{
	used[v] = 1;
	for (int i = 0; i < b; i++)
		if (sm[v][i])
			if (used[i] == 1)
			{
				flag = 0;
				return;
			}
			else if (used[i] == 0)
				dfs1(i);
	used[v] = 2;
}

int dfs2(int v)
{
	if (xd[v] == 0)
	{
		for (int i = 0; i < b; i++)
			if (sm[i][v] == 1)
			{
				if (xd[i] == 0)
				{
					int x = dfs2(i);
					xd[i] = x;
				}
				xd[v] += xd[i];
			}
	}
	return xd[v];
}

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int q = 0; q < t; q++)
	{
		cin >> b >> m;
		cout << "Case #" << (q + 1) << ": ";

		int f = 0;
		for (int mask = 0; mask < (1 << b * b - b - (b - 1)); mask++)
		{
			glob_mask = mask;
			for (int i = 0; i < b; i++)
				for (int j = 0; j < b; j++)
					sm[i][j] = 0;
			int x = 0, y = 0;
			int d = mask;
			while (d > 0)
			{
				if (x == y)
					y++;
				if (y == b)
				{
					x++;
					y = 0;
				}
				sm[x][y] = d % 2;
				d /= 2;
				y++;
			}

			flag = 1;
			for (int i = 0; i < b; i++)
				used[i] = xd[i] = 0;
			dfs1(0);
			if (flag && used[b - 1])
			{
				for (int i = 0; i < b; i++)
					if (used[i] == 0)
						dfs1(i);
				if (flag)
				{
					xd[0] = 1;
					int ans = dfs2(b - 1);
					if (ans == m)
					{
						cout << "POSSIBLE\n";
						f = 1;
						for (int i = 0; i < b; i++)
						{
							for (int j = 0; j < b; j++)
								cout << sm[i][j];
							cout << "\n";
						}
						break;
					}
				}
			}
		}
		if (f == 0)
			cout << "IMPOSSIBLE\n";
	}
	return 0;
}
