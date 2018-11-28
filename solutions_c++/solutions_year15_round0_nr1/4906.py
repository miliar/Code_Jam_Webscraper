#include <cstdio>

int solve() {
	int s_max;
	int s[10001] = {0, };

	scanf("%d", &s_max);

	int sum = 0;
	int f = 0;

	for (int i=0; i<=s_max; i++) {
		scanf("%1d", s+i);

		if (sum < i) {
			f += (i-sum);
			sum += (i-sum);
//			printf("[%d] f : %d\n", i, f);
		}
		sum += s[i];
//		printf("[%d] sum : %d, s[%d] : %d\n", i, sum, i, s[i]);
	}

	return f;
}

int main() {

	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int i=1; i<=T; i++) {
		printf("Case #%d: %d\n", i, solve());
	}

	fclose (stdout);
	fclose (stdin);

	return 0;
}
