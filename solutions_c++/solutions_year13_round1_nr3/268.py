#include <cstdio>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#define MAXN (1 << 7)
#define MAXAM (1 << 10)
using namespace std;

int r, n, m, k, bestk;
int v[MAXN][8];

int cur[5];
int ans[5];

int am[MAXAM];
int now;

void go(int pos) {
	if (pos == n) {
		memset(am, 0, sizeof(am));
		
		for (int mask=0; mask < (1 << n); ++mask) {
			int prod = 1;
			for (int i=0; i < n; ++i) if (mask & (1 << i))
				prod *= cur[i];
			
			am[prod] ++;
		}
		
		int koef = 0;
		for (int i=0; i < k; ++i)
			if (am[ v[now][i] ] == 0) return;
			else {
				koef += am[ v[now][i] ];
			}
		
		if (koef > bestk) {
			bestk = koef;
			memcpy(ans, cur, sizeof(ans));
		}
		
		return;
	}
	
	for (int i=2; i <= m; ++i) {
		cur[pos] = i;
		go(pos+1);
	}
}

inline void solve() {
	for (now=0; now < r; ++now) {
		bestk = -1;
		go(0);
		for (int i=0; i < n; ++i)
			printf("%d", ans[i]);
		printf("\n");
	}
}

inline void read() {
	scanf("%d%d%d%d", &r, &n, &m, &k);
	for (int i=0; i < r; ++i)
		for (int j=0; j < k; ++j)
			scanf("%d", &v[i][j]);
}

int main() {
	int brt = 0;
	scanf("%d", &brt);
	
	printf("Case #1:\n");
	while (brt --) {
		read();
		solve();
	}
	return 0;
}