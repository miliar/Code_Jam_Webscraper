//============================================================================
// Name        : B.cpp
// Author      : kangaroo
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

const int maxn = 200;
int row[maxn], column[maxn], a[maxn][maxn];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int casenum = 1; casenum <= T; ++casenum)
	{
		int n, m;
		scanf("%d %d", &n, &m);
		memset(row, 0, sizeof(row));
		memset(column, 0, sizeof(column));
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j){
				scanf("%d", &a[i][j]);
				row[i] = max(row[i], a[i][j]);
				column[j] = max(column[j], a[i][j]);
			}

		bool ans = true;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				if (a[i][j] != row[i] && a[i][j] != column[j])
					ans = false;
		if (ans)
			printf("Case #%d: YES\n", casenum);
		else printf("Case #%d: NO\n", casenum);
	}
	return 0;
}
