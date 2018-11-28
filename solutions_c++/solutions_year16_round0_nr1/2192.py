#include <cstdio>
#include <cstring>

int n, ans, cnt;
bool b[10];

void add(int x) {
	while (x) {
		int d = x%10;
		if (!b[d]) {
			b[d] = 1;
			cnt++;
		}
		x /= 10;
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		scanf("%d", &n);
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", cas);
			continue;
		}
		memset(b, 0, sizeof(b));
		cnt = 0; ans = 0;
		while (cnt < 10) {
			ans += n;
			add(ans);
		}
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}
