//============================================================================
// Name        : 2016_gcj_a.cpp
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

int n;
int a[30], b[30];
int tn;
bool vis[10];
int cnt, c;

int main() {

#ifdef RUN
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif

	int t;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; cas++) {
		printf("Case #%d: ", cas);
		scanf("%d", &n);
		if (n == 0) {
			printf("INSOMNIA\n");
			continue;
		}
		memset(vis, 0, sizeof(vis));
		cnt = 0;
		tn = 0;
		memset(a, 0, sizeof(a));
		while (n) {
			a[tn++] = n%10;
			n /= 10;
		}
		memset(b, 0, sizeof(b));
		while (cnt < 10) {
			c = 0;
			for (int i = 0; i < tn; i++) {
				b[i] += (a[i]+c);
				c = b[i] / 10;
				b[i] %= 10;
				if (!vis[b[i]]) {
					vis[b[i]] = 1;
					cnt += 1;
				}
			}
			while (c) {
				b[tn++] = c%10;
				c /= 10;
				if (!vis[b[tn-1]]) {
					vis[b[tn-1]] = 1;
					cnt += 1;
				}
			}
		}
		for (int i = tn-1; i >= 0; i--) {
			printf("%d", b[i]);
		}
		printf("\n");
	}
	return 0;
}
