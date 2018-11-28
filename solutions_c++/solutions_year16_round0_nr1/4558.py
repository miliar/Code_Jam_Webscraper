#include <stdio.h>

const int MAXN = 1000011;

int f[MAXN];

int func(int x) {
	bool vist[10] = {0};
	for (int i = 1; i <= 10000; ++i) {
		int tmp = i * x;
		while (tmp > 0) {
			vist[tmp % 10] = true;
			tmp /= 10;
		}
		int cnt = 0;
		for (int j = 0; j < 10; ++j) {
			if (vist[j]) {
				++cnt;
			}
		}
		if (cnt == 10) {
			return i * x;
		}
	}
	return -1;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A_output.txt", "w", stdout);
	for (int i = 1; i < MAXN; ++i) {
		f[i] = func(i);
	}
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; ++cas) {
		printf("Case #%d: ", cas);
		int n;
		scanf("%d", &n);
		if (n == 0) {
			printf("INSOMNIA\n");
		} else {
			printf("%d\n", f[n]);
		}
	}
	return 0;
}
