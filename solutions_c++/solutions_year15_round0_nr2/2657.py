#include <stdio.h>
#include <string.h>

const int MAXN = 1010;

int p[MAXN];
int D;


int main() {
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		scanf("%d", &D);
		int ans = MAXN;
		for (int i = 0; i < D; i++) {
			scanf("%d", p + i);
		}
		for (int t = 1; t < MAXN; t++) {
			int tmp = t;
			for (int i = 0; i < D; i++) {
				tmp += (p[i] - 1) / t;
			}
			if (tmp < ans) ans = tmp;
		}
		printf("Case #%d: %d\n", cas, ans);
	}
}