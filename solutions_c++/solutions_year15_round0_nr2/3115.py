#include <stdio.h>

int n;
int P[1010];

int reduceNum(int x, int base) {
	if (x % base == 0)	return (x / base) - 1;
	return x / base;
}

int main() {
	int T;

	scanf("%d", &T);
	for(int cases=1; cases <= T; ++cases) {
		scanf("%d", &n);

		int maxi = 0;
		int ans = 10010;
		for (int i = 0;i < n;++i) {
			scanf("%d", &P[i]);
			if (maxi < P[i]) {
				maxi = P[i];
			}
		}

		for (int i = 1;i <= maxi; ++i) {
			int count = i;
			for (int j = 0;j < n; ++j) {
				count = count + reduceNum(P[j], i);
			}
			if (count < ans)	ans = count;
		}

		printf("Case #%d: %d\n", cases, ans);
	}

	return 0;
}