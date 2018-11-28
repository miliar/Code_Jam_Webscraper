//be naame khodaa

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

char a[105][105];

int main()
{
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	for (int it = 1; it <= t; it++)
	{
		int n, m, ans = 0;
		cin >> n >> m;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				cin >> a[i][j];
		bool imp = false;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
			{
				if (a[i][j] == '.') continue;
				ans++;
				bool lose = true;
				for (int k = j-1; k >= 0; k--)
					if (a[i][k] != '.')
					{
						lose = false;
						if (a[i][j] == '<')
							ans--;
						break;
					}
				for (int k = j+1; k < m; k++)
					if (a[i][k] != '.')
					{
						lose = false;
						if (a[i][j] == '>')
							ans--;
						break;
					}
				for (int k = i-1; k >= 0; k--)
					if (a[k][j] != '.')
					{
						lose = false;
						if (a[i][j] == '^')
							ans--;
						break;
					}
				for (int k = i+1; k < n; k++)
					if (a[k][j] != '.')
					{
						lose = false;
						if (a[i][j] == 'v')
							ans--;
						break;
					}
				imp |= lose;
			}
		if (imp)
			cout << "Case #" << it << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << it << ": " << ans << endl;
	}
	return 0;
}
