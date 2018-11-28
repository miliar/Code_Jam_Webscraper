#include <iostream>
#include <algorithm>
#include <fstream>
#include <queue>
#include <cstdio>
using namespace std;

const int inf = (int)1e9;
const int MAXN = 103;

int a[MAXN][MAXN];
int n, m;

bool can(int x, int y)
{
	bool higher = true;
	for (int i = 0; i < n; ++i) {
		if (a[x][y] < a[i][y]) higher = false;
	}
	if (higher) return true;
	
	higher = true;
	for (int i = 0; i < m; ++i) {
		if (a[x][y] < a[x][i]) higher = false;
	}
	if (higher) return true;
	
	return false;
}

int main()
{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		cin >> n >> m;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				cin >> a[i][j];
			}
		}
		int res = 1;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				res = res & can(i, j);
			}
		}
		printf("Case #%d: %s\n", t + 1, (res ? "YES" : "NO"));
	}
	
	return 0;
}
