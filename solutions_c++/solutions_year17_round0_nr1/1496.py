#include <bits/stdc++.h>

using namespace std;

const int maxn = 1003;

int n, k;
char a[maxn];

int sovA() {
	scanf("%s%d", a, &k);
	n = strlen(a);
	int ans(0);
	for (int i = 0; i < n; ++ i) {
		if (a[i] == '-') {
			if (i + k > n) {
				return -1;
			}
			for (int j = 0; j < k; ++ j) {
				if (a[i + j] == '-') {
					a[i + j] = '+';
				} else {
					a[i + j] = '-';
				}
			}
			++ ans;
		}
	}
	return ans;
}

int main() {
	freopen(".in", "r", stdin);
	int t;
	scanf("%d", &t);
	for (int i = 1, s; i <= t; ++ i) {
		printf("Case #%d: ", i);
		if ((s = sovA()) >= 0) {
			printf("%d\n", s);
		} else {
			puts("IMPOSSIBLE");
		}
	}
}
