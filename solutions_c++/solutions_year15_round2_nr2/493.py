#include <bits/stdc++.h>

using namespace std;

int a[1111][111];
int n,m,c;
int ans;
int test;

void rec(int x, int y, int sum)
{
	if (sum > c)
		return;
	if (x == n)
	{
		int tmp = 0;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
			{
				if (a[i][j] + a[i + 1][j] == 2)
					tmp++;
				if (a[i][j] + a[i][j + 1] == 2)
					tmp++;
			}
		int u = 0;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				u += a[i][j];
		if (u != c)
			return;
		ans = min(ans, tmp);
		return;
	}
	a[x][y] = 1;
	if (y + 1 < m)
		rec(x, y + 1, sum + 1);
	else
		rec(x + 1, 0, sum + 1);

	a[x][y] = 0;

	if (y + 1 < m)
		rec(x, y + 1, sum);
	else
		rec(x + 1, 0, sum);

}

int solve()
{
	cin >> n >> m >> c;
		for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			a[i][j] = 0;
	ans = 1000000;

	rec(0, 0, 0);
	return ans;
}

int main()
{
	cin >> test;
	for (int i = 1; i <= test; i++)
	{
		cout << "Case #" << i <<": " << solve() << endl;
	}

	return 0;
}