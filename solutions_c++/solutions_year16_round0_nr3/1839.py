#include <string>
#include <stdio.h>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <queue>
#pragma warning(disable:4996)

using namespace std;
#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))
#define rep(i,n) for (int i=0; i<n; i++)
#define FOR(i,a,b) for (int i=a; i<b; i++)
#define ll long long
#define N 101

int n, m, t, a[33];

void dfs(int d) {
	if (m == 0) return;
	if (d >= n-3) {
		rep(i, n) printf("%d", a[i]);
		FOR(i, 3, 12) printf(" %d", i);
		printf("\n");
		m--;
		return;
	}
	dfs(d + 1);
	a[d] = a[d + 1] = 1;
	dfs(d + 2);
	a[d] = a[d + 1] = 0;
}

int main() {
	freopen("try.in", "r", stdin);
	freopen("try.out", "w", stdout);

	scanf("%d", &t);
	rep(tt, t) 
	{
		scanf("%d%d", &n, &m);
		printf("Case #%d:\n", tt + 1);
		memset(a, 0, sizeof(a));
		a[0] = a[1] = a[n - 1] = a[n - 2] = 1;
		dfs(2);
	}
}