#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
#define MAXN (1 << 15)
using namespace std;

int n, cap;
int a[MAXN];
int used[MAXN];

inline void read() {
	cin >> n >> cap ;
	for (int i=0; i < n; ++i)
		cin >> a[i];
}

inline void solve() {
	sort(a, a+n);
	memset(used, 0, sizeof used);

	int ans = 0;
	for (int i=0; i < n; ++i) { // steps
		int mi = -1, ma = -1;
		for (int j=0; j < n; ++j) if (!used[j]) { mi = j; break; }
		for (int j=0; j < n; ++j) if (!used[j]) { ma = j; }

		if (mi == -1 && ma == -1) break;

		if (a[mi] + a[ma] > cap) {
			ans ++;
			used[ma] = 1;
		} else {
			ans ++;
			used[mi] = used[ma] = 1;
		}
	}

	printf("%d\n", ans);
}

int main() {
	int brt;
	scanf("%d", &brt);

	for (int test=0; test < brt; ++test) {
		printf("Case #%d: ", test+1);
		read();
		solve();
	}
	return 0;
}