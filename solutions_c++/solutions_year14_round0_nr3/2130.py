#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int a[7][7];
bool used[7][7];
int r, c, m;
int cnt;


bool prr (int x, int y)
{
	if (!used[x][y] && a[x][y] == 0)
		cnt++;
	bool f = true;
	used [x][y] = true;
	for (int i = x - 1; i <= x + 1; i++)
		for (int j = y - 1; j <= y + 1; j++)
			if (a[i][j] == 1)
				f = false;
	if (f)
		for (int i = x - 1; i <= x + 1; i++)
			for (int j = y - 1; j <= y + 1; j++)
				if (!used[i][j] && a[i][j] == 0)
					prr (i, j);
}

bool pr ()
{
	for (int i = 0; i < (1 << (r * c)); i++)
	{
		for (int ii = 0; ii < 7; ii++)
			for (int jj = 0; jj < 7; jj++)
			{
				used[ii][jj] = false;
				a[ii][jj] = 2;
			}
		if (__builtin_popcount (i) == m)
		{
			int dd = i;
			for (int ii = 1; ii <= r; ii++)
			{
				for (int jj = 1; jj <= c; jj++)
				{
					if (dd % 2 == 0)
						a[ii][jj] = 0;
					else
						a[ii][jj] = 1;
					dd /= 2;
				}
			}
			cnt = 0;
			prr (1, 1);
			if (cnt == r * c - m)
				return true;
		}
	}
	return false;
}

int main()
{
	for (int i = 0; i < 7; i++)
		for (int j = 0; j < 7; j++)
			a[i][j] = 2;
	int t;
	scanf ("%d", &t);
	for (int k = 0; k < t; k++)
	{
		scanf ("%d%d%d", &r, &c, &m);
		printf ("Case #%d:\n", k + 1);
		if (pr())
		{
			a[1][1] = 2;
			for (int i = 1; i <= r; i++)
			{
				for (int j = 1; j <= c; j++)
				{
					if (a[i][j] == 0)
						printf (".");
					if (a[i][j] == 2)
						printf ("c");
					if (a[i][j] == 1)
						printf ("*");
				}
				printf ("\n");
			}
		}
		else
			printf ("Impossible\n");
	}
}
