#include <cstdio>
#include <cstring>
int main() {
	FILE *fp, *fp2;
	fp = fopen("B-large.in", "r");
	fp2 = fopen("B-large.out", "w");
	int T, Tpie;
	int dp[101];
	char cake[101];
	fscanf(fp, "%d\n", &T);
	Tpie = T;
	while (Tpie--) {
		fscanf(fp, "%s\n", cake);
		int length = strlen(cake);
		memset(dp, 0, sizeof(dp));
		for (int i = 0; i < length; i++) {
			if (i == 0 && cake[0] == '-') {
				dp[0] = 1;
				continue;
			}
			if (i == 0 && cake[0] == '+') {
				dp[0] = 0;
				continue;
			}
			dp[i] = dp[i - 1];
			if (cake[i] == '-' && cake[i - 1] == '+')
				dp[i] += 2;
			//else if (cake[i] == '+' && cake[i - 1] == '-')
			//	dp[i] += 1;
		}
		fprintf(fp2, "Case #%d: %d\n", T - Tpie, dp[length - 1]);
	}
	fclose(fp);
	fclose(fp2);
	return 0;
}