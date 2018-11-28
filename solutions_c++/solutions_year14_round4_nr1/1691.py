/*
*   Copyright (C) 2014 All rights reserved.
*   
*   filename: a.cpp
*   author: doublehh
*   e-mail: sserdoublehh@foxmail.com
*   create time: 2014-05-31
*   last modified: 2014-05-31 22:13:27
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<int, int> pii;
#define mp(x, y) make_pair(x, y)
#define X first
#define Y second
#define pb(x) push_back(x)
#define FOR(i, n) for (int i = 0; i < (n); i++)
#define foreach(it, s) for (__typeof((s).begin()) it = (s).begin(); it != (s).end(); it++)

const int maxn = 1e4;
int n, m;
int a[maxn];

int main()
{
//	freopen("out", "w", stdout);
	int T;
	scanf("%d", &T);
	FOR (Case, T)
	{
		scanf("%d%d", &n, &m);
		FOR (i, n)
			scanf("%d", &a[i]);
		sort(a, a+n);
		int ans = 0, i, j;
		for (i = 0, j = n-1; i < j; )
		{
			if (a[i]+a[j] <= m)
			{
				ans++;
				i++;
				j--;
			}
			else
			{
				ans++;
				j--;
			}
		}
		if (i == j)
			ans++;
		printf("Case #%d: %d\n", Case+1, ans);
	}
}
