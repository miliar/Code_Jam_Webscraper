#include <functional>
#include <algorithm>
#include <strstream>
#include <iostream>
#include <numeric>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <cstdio>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <cmath>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

const int maxn = 110;

char c[maxn][maxn];
int n, m;

bool check_dir(int i, int j, int dx, int dy)
{
	int ii = i + dx, jj = j + dy;
	while (ii >= 0 && ii < n && jj >= 0 && jj < m)
	{
		if (c[ii][jj] != '.')
			return true;
		ii += dx;
		jj += dy;
	}
	return false;
}

void solve()
{
	cin >> n >> m;
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			cin >> c[i][j];

	int ans = 0, t;
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			if (c[i][j] != '.')
			{
				bool good = false;
				if (c[i][j] == '>')
					good = check_dir(i, j, 0, 1);
				
				if (c[i][j] == '<')
					good = check_dir(i, j, 0, -1);
				
				if (c[i][j] == 'v')
					good = check_dir(i, j, 1, 0);
				
				if (c[i][j] == '^')
					good = check_dir(i, j, -1, 0);
				
				if (!good)
				{
					if (check_dir(i, j, 0, 1) || check_dir(i, j, 0, -1) || check_dir(i, j, 1, 0) || check_dir(i, j, -1, 0))
						++ans;
					else
					{
						cout << "IMPOSSIBLE" << endl;
						return;
					}
				}
			}
	cout << ans << endl;
}

int main()
{
	ios_base::sync_with_stdio(0);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
		solve();
	}

	return 0;
}