#include <stdio.h>

int n;
char S[1010];

int main() {
	int T;

	scanf("%d", &T);
	for (int cases=1;cases <= T; ++cases) {
		scanf("%d", &n);
		scanf("%s", S);

		int ans = 0;
		int count = S[0] - '0';
		for (int i = 1; i <= n; ++i) {
			int x = S[i] - '0';
			if (x == 0)	continue;
			if (count < i) {
				//printf("add %d people in %d\n", i - count, i);
				ans += i - count;
				count += i - count;
			}
			count += x;
		}

		printf("Case #%d: %d\n", cases, ans);
	}

	return 0;
}
