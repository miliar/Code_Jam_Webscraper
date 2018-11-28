// Revenge of the Pancakes

#include <cstdio>

#define min(a, b) (((a) < (b)) ? (a) : (b))

void calc() {
	char pc[101];
	int i, j;
	int dp[100][2]; // [index][0: + / 1: -]

	scanf("%s", pc);

	for (i = 0; pc[i]; i++) {
		if (i == 0) {
			dp[i][0] = (pc[i] == '+') ? 0 : 1;
			dp[i][1] = (pc[i] == '-') ? 0 : 1;
		} else {
			if (pc[i] == '+') {
				dp[i][0] = min(
					dp[i - 1][0],
					dp[i - 1][1] + 1
				);
			} else {
				dp[i][0] = min(
					dp[i - 1][0] + 2,
					dp[i - 1][1] + 1
				);
			}

			if (pc[i] == '-') {
				dp[i][1] = min(
					dp[i - 1][1],
					dp[i - 1][0] + 1
				);
			} else {
				dp[i][1] = min(
					dp[i - 1][1] + 2,
					dp[i - 1][0] + 1
				);
			}
		}
	}

	printf("%d\n", dp[i - 1][0]);
}

int main() {
	int i, tc;

	scanf("%d", &tc);
	for (i = 1; i <= tc; i++) {
		printf("Case #%d: ", i);
		calc();
	}

	return 0;
}