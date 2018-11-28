#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int n, m;
int a[101][101];

inline int max_row(int row)
{
	int r = 0;
	for (int j = 0; j < m; ++j)
		r = max(r, a[row][j]);
	return r;
}

inline int max_col(int col)
{
	int r = 0;
	for (int i = 0; i < n; ++i)
		r = max(r, a[i][col]);
	return r;
}

inline string solve()
{
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			scanf("%d", &a[i][j]);
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			if (max_row(i) != a[i][j] && max_col(j) != a[i][j]) return "NO";
	return "YES";
}

int main()
{
	int tt;
	scanf("%d", &tt);
	for (int t = 0; t < tt; ++t)
		printf("Case #%d: %s\n", t + 1, solve().c_str());
	return 0;
}
