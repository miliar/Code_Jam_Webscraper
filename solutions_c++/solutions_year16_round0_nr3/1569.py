//============================================================================
// Name        : 2016_gcj_c.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

#define RUN

int a[40], n, i, j;

void dfs(int cur, int &cnt) {
	if (cnt >= j)
		return;
	if (cur >= n-3) {
		for (i = n-1; i > 0; i--)
			printf("%d", a[i]+a[i-1]);
		printf("%d", a[0]);
		for (i = 3; i <= 11; i++)
			printf(" %d", i);
		printf("\n");
		cnt += 1;
		return;
	}
	dfs(cur+1, cnt);
	a[cur] = 1;
	dfs(cur+2, cnt);
	a[cur] = 0;
	return;
}

int main() {

#ifdef RUN
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
#endif

	int t;
	int cnt;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; cas++) {
		printf("Case #%d:\n", cas);
		scanf("%d%d", &n, &j);
		memset(a, 0, sizeof(a));
		cnt = 0;
		a[0] = a[n-2] = 1;
		dfs(2, cnt);
	}
	return 0;
}
