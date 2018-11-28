//============================================================================
// Name        : cj_B.cpp
// Author      : huangxs139
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

int a[110][110];
bool r[110], c[110];
bool ans;
int n, m;
int cnt;

int main() {
	int t;
	freopen("B-small-attempt3.in", "r", stdin);
	freopen("data.out", "w", stdout);
	while (~scanf("%d", &t)) {
		for (int cas = 1; cas <= t; cas++) {
			scanf("%d %d", &n, &m);
			memset(r, 0, sizeof(r));
			memset(c, 0, sizeof(c));
			cnt = 0;
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					scanf("%d", &a[i][j]);
					if (a[i][j] == 2) {
						r[i] = c[j] = 1;
						cnt++;
					}
				}
			}
            ans = 1;
			for (int i = 0; i < n && ans; i++) {
				for (int j = 0; j < m && ans; j++) {
					if (r[i] && c[j] && a[i][j] == 1)
                        ans = 0;
				}
			}
			if (ans)
				printf("Case #%d: YES\n", cas);
			else
				printf("Case #%d: NO\n", cas);
		}
	}
	return 0;
}
