#include <stdio.h>

int n, a[1000];
bool t1(int m) {
	for (int i = 0; i < m; ++i) {
		int l = m - i;
		int ii = i;
		for (int j = 0; j < n; ++j) {
			ii -= (a[j] - 1) / l;
		}
		if (ii >= 0) return true;
	}
	return false;
}

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; ++tt) {
		scanf("%d", &n);
		int ma = 1, mi = 1;
		for (int i = 0; i < n; ++i) {
			scanf("%d", a+i);
			if (ma < a[i]) ma = a[i];
			if (mi > a[i]) mi = a[i];
		}
		while (mi < ma) {
			int m = (mi + ma) / 2;
			if (t1(m)) ma = m;
			else mi = m + 1;
		}
		printf("Case #%d: %d\n", tt, mi);
	}
}
