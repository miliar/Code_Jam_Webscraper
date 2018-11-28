#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <cmath>
#include <queue>
#include <map>
#include <algorithm>

using namespace std;

#define X first
#define Y second

int n, m;
int a[100][100];

bool test(int x, int y) {
	int val = a[x][y];
	bool v = 1, h = 1;
	for (int i = 0; i < n; ++i)
		v = v && (a[i][y] <= val);
	for (int i = 0; i < m; ++i)
		h = h && (a[x][i] <= val);
	return v || h;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int TT = 1; TT <= T; ++TT) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				scanf("%d", &a[i][j]);
		bool q = 1;
		for (int i = 0; i < n && q; ++i)
			for (int j = 0; j < m && q; ++j)
				if (!test(i, j))
					q = 0;
		printf("Case #%d: %s\n", TT, q ? "YES" : "NO");
	}
	return 0;
}