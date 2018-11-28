#include <iostream>

using namespace std;

int n, m;
int a[100][100];
int r[100], c[100];

void solve()
{
	for (int i = 0; i < n; i++)
		r[i] = 0;
	for (int j = 0; j < m; j++)
		c[j] = 0;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
		{
			if (a[i][j] > r[i])
				r[i] = a[i][j];
			if (a[i][j] > c[j])
				c[j] = a[i][j];
		}
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			if (a[i][j] < r[i] && a[i][j] < c[j])
			{
				cout << "NO" << endl;
				return;
			}
	cout << "YES" << endl;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		cin >> n >> m;
		for (int x = 0; x < n; x++)
			for (int y = 0; y < m; y++)
				cin >> a[x][y];
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
	return 0;
}
