#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <map>
#include <vector>
using namespace std;
int a[201][201] = {0};
int b[202][202] = {0};
int mh[202] = {0}, ml[202] = {0};
int check(int n, int m)
{
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++)
			if (a[i][j] != b[i][j])
				return 0;
	return 1;
}
int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int tot;
	cin >> tot;
	for (int tt = 1; tt <= tot; tt++)
	{
		int n, m;
		memset(mh, 0, sizeof(mh));
		memset(ml, 0, sizeof(ml));
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= m; j++)
				scanf("%d", &a[i][j]);
		}
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
				mh[i] = max(mh[i], a[i][j]), ml[j] = max(ml[j], a[i][j]);
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
				b[i][j] = min(mh[i], ml[j]);
		if(check(n, m))
			printf("Case #%d: YES\n", tt);
		else
			printf("Case #%d: NO\n", tt);
	}
	return 0;
}
