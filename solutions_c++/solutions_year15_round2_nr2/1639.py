#include<bits/stdc++.h>
using namespace std;
int ans = 100000;
void check(int r,int c,int m[17][17])
{
	int i, j, k, a = 0;
	for (i = 0; i < r; ++i)
	{
		for (j = 0; j < c; ++j)
		{
			if (m[i][j] == 1)
			{
				if (i>0)
				{
					if (m[i - 1][j] == 1)
						++a;
				}
				if (j < c - 1)
				{
					if (m[i][j + 1] == 1)
						++a;
				}
			}
		}
	}
	if (a < ans)
		ans = a;
}
void solve(int n,int r,int c,int m[17][17],int now,int x,int y)
{
	int i, j;
	if (now>n)
		return;
	if (n == now)
	{
		check(r,c,m);
		/*for (i = 0; i < r; ++i)
		{
			cout << endl;
			for (j = 0; j < c; ++j)
				cout << m[i][j] << " ";
		}
		cout << endl;*/
	}
	else
	{
		if (x < r && y<c)
		{
			m[x][y] = 1;
			solve(n, r, c, m, now + 1, x + 1, y);
			m[x][y] = 0;
			solve(n, r, c, m, now, x + 1, y);
		}
		else if (y < c)
		{
			solve(n, r, c, m, now, 0, y + 1);
		}
	}
}
int main()
{
	int i, j, k, t, n, x, r, c;
	cin >> t;
	for (x = 1; x <= t; ++x)
	{
		ans = 100000;
		cin >> r >> c >> n;
		int m[17][17] = { { 0 } };
		memset(m, 0, sizeof(m));
		solve(n, r, c, m, 0, 0, 0);
		cout << "Case #" << x << ": " << ans << endl;
	}
	return 0;
}