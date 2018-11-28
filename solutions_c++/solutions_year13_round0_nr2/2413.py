#include <iostream>

using namespace std;

int test; int t; int n; int m; int a[300][300]; bool ok = true; int maxi[300]; int maxj[300];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> test;
	for (int t = 1; t <= test; t++)
	{
		ok = true;
		cout << "Case #" << t << ": ";
		cin >> n >> m;
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
				cin >> a[i][j];
		for (int i = 1; i <= n; i++)
		{
			maxi[i] = 0;
			for (int j = 1; j <= m; j++)
				maxi[i] = max(maxi[i], a[i][j]);
		}
		for (int j = 1; j <= m; j++)
		{
			maxj[j] = 0;
			for (int i = 1; i <= n; i++)
				maxj[j] =max(maxj[j], a[i][j]);
		}
		for (int i = 1; i <= n; i++) if (ok)
			for (int j = 1; j <= m; j++)
				if (maxi[i] > a[i][j] && maxj[j] > a[i][j])
				{
					ok = false;
					break;
				}
		if (ok) cout << "YES" << endl;
		else	cout << "NO" << endl;
	}
}