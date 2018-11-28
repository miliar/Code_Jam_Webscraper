#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <complex>
#include <vector>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <string.h>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

const int maxn = 1111;
int ans[maxn];
int vis[maxn];
int num[maxn];
int ok (int x) {
	int cnt = 0;
	while (x) {
		num[cnt ++] = x % 10;
		x /= 10;
	}
	for (int i = 0; i < cnt / 2; ++ i) {
		if (num[i] != num[cnt-i-1]) return 0;
	}
	return 1;
}
int main () {
	freopen ("C-small-attempt0.in", "r", stdin);
	freopen ("C-small-attempt0.out", "w", stdout);
	for (int i = 0; i * i < maxn; ++ i) vis[i*i] = i;
	for (int i = 1; i < maxn; ++ i) {
		if (vis[i] && ok (i) && ok (vis[i])) ans [i] = ans[i-1] + 1;
		else ans[i] = ans[i-1];
	}
	int T;
	scanf ("%d", &T);
	for (int cas = 1; cas <= T; ++ cas) {
		int a, b;
		scanf ("%d%d", &a, &b);
		if (a > b) swap (a, b);
		printf ("Case #%d: %d\n", cas, ans[b] - ans[a-1]);
	}
	return 0;
}