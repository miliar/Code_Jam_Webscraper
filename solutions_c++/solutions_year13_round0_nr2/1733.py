#include <iostream>
#include <cstdio>
#include <algorithm>

#define maxn 500

using namespace std;

int t, n, m;
int a[maxn][maxn];
int row[maxn], col[maxn];
const char yes[] = "YES", no[] = "NO";

int proc(const int &id) {
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			scanf("%d", &a[i][j]);
	for (int i = 0; i < n; ++i)
		row[i] = 0;
	for (int j = 0; j < m; ++j)
		col[j] = 0;
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			row[i] = max(row[i], a[i][j]), col[j] = max(col[j], a[i][j]);
	bool canReach = true;
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			if (a[i][j] < min(row[i], col[j])) canReach = false;
	printf("Case #%d: %s\n", id, (canReach) ? yes : no);
	return 0;
}

int main() {
	scanf("%d", &t);
	for (int i = 0; i < t; ++i) {
		proc(i + 1);
	}
	return 0;
}
