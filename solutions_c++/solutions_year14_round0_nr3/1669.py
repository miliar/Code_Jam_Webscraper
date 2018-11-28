#include <algorithm>
#include <cassert>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

typedef long double lf;

const int maxn = 5;
const int dx[] = {1, 1, 1, 0, -1, -1, -1, 0};
const int dy[] = {1, 0, -1, -1, -1, 0, 1, 1};

int n, m, k, field[maxn][maxn], cnt[maxn][maxn], zx, zy;
char used[maxn][maxn];
int ansmsk = -1;

void dfs(int x, int y)
{
	if (used[x][y]) return;
	used[x][y] = 1;
	if (cnt[x][y] != 0) return;
	for (int d = 0; d < 8; ++d)
	{
		int nx = x + dx[d], ny = y + dy[d];
		if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
		dfs(nx, ny);
	}
}

bool stupid()
{
	for (int i = 0; i < (1 << (n * m)); ++i)
	{
		memset(used, 0, sizeof(used));
		if (__builtin_popcount(i) != k) continue;
		for (int j = 0; j < n; ++j)
			for (int z = 0; z < m; ++z)
				field[j][z] = (i >> (j * m + z)) & 1;
		zx = -1, zy = -1;
		for (int j = 0; j < n; ++j)
			for (int z = 0; z < m; ++z)
			{
				if (field[j][z])
				{
					cnt[j][z] = -1;
					continue;
				}
				
				cnt[j][z] = 0;
				for (int d = 0; d < 8; ++d)
				{
					int nx = j + dx[d], ny = z + dy[d];
					if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
					cnt[j][z] += field[nx][ny];
				}
				if (!cnt[j][z]) zx = j, zy = z;
			}
		if (n * m - k <= 1) 
		{
			ansmsk = i;
			for (int j = 0; j < n; ++j)
				for (int z = 0; z < m; ++z)
					if (!field[j][z])
						zx = j, zy = z;
			return true;
		}
		if (zx == -1 && zy == -1)
			continue;
		dfs(zx, zy);
		bool ok = true;
		for (int j = 0; j < n; ++j)
			for (int z = 0; z < m; ++z)
				ok &= field[j][z] || used[j][z];
		if (ok)
		{
			ansmsk = i;
			return true;
		}
	}
	return false;
}

void solve()
{
	cin >> n >> m >> k;
	assert(n <= 5 && m <= 5);
	cout << endl;
	if (stupid())
	{
		for (int i = 0; i < n; ++i, cout << endl)
			for (int j = 0; j < m; ++j)
				if (i == zx && j == zy)
					cout << "c";
				else
					cout << ".*"[(ansmsk >> (i * m + j)) & 1];
	}
	else cout << "Impossible" << endl;
}

int main() 
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	cout.precision(7);
	cout << fixed;
	int t;
    cin >> t;
    for (int i = 0; i < t; ++i) 
		cout << "Case #" << i + 1 << ": ", solve();
    return 0;
}

