#include <bits/stdc++.h>
using namespace std;

int T;
int n, ans = 0;
int fr[1024];
int ap[1024];
bool dst[1024];
int mx[1024];

int main() {
	scanf("%d", &T);
	for (int test = 1; test <= T; ++test) {
		ans = 0;
		printf("Case #%d: ", test);
		scanf("%d", &n);
		memset(ap, 0, sizeof(ap));
		memset(dst, false, sizeof(dst));
		memset(mx, 0, sizeof(mx));
		for (int i = 1; i <= n; ++i)
			scanf("%d", fr + i);
		for (int i = 1; i <= n; ++i) {
			int now = i, cnt = 0;
			do {
				ap[now] = i;
				now = fr[now];
				cnt ++;
			} while (ap[now] != i);
			if (now == i)
				ans = max(ans, cnt);
		}
		for (int i = 1; i <= n; ++i) {
			if (fr[fr[i]] == i)
				dst[i] = true;
		}
		memset(ap, 0, sizeof(ap));
		for (int i = 1; i <= n; ++i) {
			if (!dst[i]) {
				int cnt = 0, now = i;
				do {
					cnt ++;
					ap[now] = i;
					now = fr[now];
				} while (ap[now] != i && !dst[now]);
				if (dst[now]) {
					mx[now] = max(mx[now], cnt);
				}
			}
		}
		int sum = 0;
		for (int i = 1; i <= n; ++i) {
			if (dst[i])
				sum += mx[i] + 1;
		}
		ans = max(ans, sum);
		printf("%d\n", ans);
	}
	return 0;
}