#include <algorithm>
#include <iostream>
#include <cstring>
#include <vector>
#include <cstdio>
using namespace std;

#define MAXN 150
#define MAXM 150

int n, m, a[MAXN][MAXM];

string solve_slow()
{
	for (int d = 1; d < 100; ++d) {
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j) {
				if (a[i][j] == d) {
					int v = 0, h = 0;
					for (int k = 0; k < n; ++k)
						v += a[k][j] <= d;
					for (int k = 0; k < m; ++k)
						h += a[i][k] <= d;
					if (v != n && h != m) return "NO";
				}
			}
	}

	return "YES";
}

vector < pair <int, int> > pos[110];
bool was[MAXN][MAXM];

string solve_fast()
{
	for (int i = 0; i < 110; ++i)
		pos[i].clear();
	memset(was, 0, sizeof was);

	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j) {
			pos[a[i][j]].push_back(make_pair(i, j));
		}

	for (int d = 1; d < 100; ++d) {
		for (size_t i = 0; i < pos[d].size(); ++i) {
			int x = pos[d][i].first, y = pos[d][i].second;
			if (was[x][y]) continue;	
			int v = 0, h = 0;
			for (int k = 0; k < n; ++k)
				v += a[k][y] <= d,
				was[k][y] == 1;
			for (int k = 0; k < m; ++k)
				h += a[x][k] <= d,
				was[x][k] == 1;
			if (v != n && h != m) return "NO";
		}
	}

	return "YES";
}


int main()
{
	freopen("input", "r", stdin);

	int T;
	scanf("%d\n", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d %d\n", &n, &m);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				scanf("%d", &a[i][j]);
		printf("Case #%d: %s\n", t, solve_fast().data());
	}

	return 0;
}
