#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

const int MAXN = 110;

int a[MAXN][MAXN], n, m, maxr[MAXN], maxc[MAXN];

void init()
{
	scanf("%d%d", &n, &m);
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= m; ++j)
			scanf("%d", &a[i][j]);
}
int id, test;
void solve()
{
	memset(maxr, 0, sizeof(maxr));
	memset(maxc, 0, sizeof(maxc));
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= m; ++j)
			maxr[i] = max(maxr[i], a[i][j]),
			maxc[j] = max(maxc[j], a[i][j]);
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= m; ++j)
			if (maxr[i] > a[i][j] && maxc[j] > a[i][j])
			{
				printf("Case #%d: NO\n", id);
				return ;
			}
	printf("Case #%d: YES\n", id);
}
int main()
{
#ifndef ONLINE_JUDGE
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
#endif
	scanf("%d", &test);
	while (test)
		++id,
		init(),
		solve(),
		--test;
	fclose(stdin);
	fclose(stdout);
	return 0;
}
