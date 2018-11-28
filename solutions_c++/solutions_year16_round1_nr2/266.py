#include <bits/stdc++.h>
using namespace std;

int T;
int n, s, t;
int h[2560];

int main() {
	scanf("%d", &T);
	for (int test = 1; test <= T; ++test) {
		printf("Case #%d:", test);
		scanf("%d", &n);
		memset(h, 0, sizeof(h));
		for (int i = 1; i < n * 2; ++i) {
			for (int j = 0; j < n; ++j) {
				scanf("%d", &t);
				h[t]++;
			}
		}
		for (int i = 1; i <= 2500; ++i) {
			if (h[i] % 2 == 1) {
				printf(" %d", i);
			}
		}
		printf("\n");
	}
	return 0;
}