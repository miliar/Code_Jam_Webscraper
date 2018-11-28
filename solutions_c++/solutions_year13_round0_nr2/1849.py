#include <iostream>

using namespace std;

int a[100][100];
int h[100], v[100];
int t, n, m;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		cin >> n >> m;
		for (int j = 0; j < n; j++)
		{
			for (int k = 0; k < m; k++)
			{
				cin >> a[j][k];
			}
		}
		for (int j = 0; j < n; j++)
		{
			h[j] = 0;
			for (int k = 0; k < m; k++)
			{
				h[j] = max(h[j], a[j][k]);
			}
		}
		for (int j = 0; j < m; j++)
		{
			v[j] = 0;
			for (int k = 0; k < n; k++)
			{
				v[j] = max(v[j], a[k][j]);
			}
		}
		bool f = true;
		for (int j = 0; j < n; j++)
		{
			for (int k = 0; k < m; k++)
			{
				if (a[j][k] != h[j] && a[j][k] != v[k])
				{
					f = false;
					break;
				}
			}
			if (!f)
			{
				break;
			}
		}
		if (f)
		{
			cout << "Case #" << i + 1 << ": YES" << endl;
		}
		else
		{
			cout << "Case #" << i + 1 << ": NO" << endl;
		}
	}
	return 0;
}
