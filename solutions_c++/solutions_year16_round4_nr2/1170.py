#include <stdio.h>
#include <algorithm>
using namespace std;



int en, ek, k2;
double ep[200];
double ans;
double choose[200];

double max(double a, double b) {
	if (a > b)
		return a;
	return b;
}

void dfs(int level, int c) {
	if (level == en && c == ek) {
		double dp[20][20][20];
		for (int i = 0; i <= ek; i++)
			for (int j = 0; j <= k2; j++)
				for (int k = 0; k <= k2; k++)
					dp[i][j][k] = 0.0;
		dp[0][0][0] = 1.0;
		for (int i = 0; i < ek; i++) {
			for (int j = 0; j <= k2; j++)
				for (int k = 0; k <= k2; k++) {
					dp[i+1][j+1][k] += dp[i][j][k] * choose[i];
					dp[i+1][j][k+1] += dp[i][j][k] * (1.0 - choose[i]);
					//printf("%d %d %d %lf  (ori=%lf, t=%lf)\n", i, j, k, dp[i][j][k], dp[i-1][j][k], t);
				}

		}
		//double curP = dp[ek][k2][k2];
		//printf("curP = %lf\n", curP);
		if (dp[ek][k2][k2] > ans)
			ans = dp[ek][k2][k2];
	}
	else {
		if (en - level - 1 >= ek - c)
			dfs(level+1, c);
		if (c < ek) {
			choose[c] = ep[level];
			dfs(level+1, c+1);
		}
	}
}

int main(int argc, char *argv[]) {
	int ecase, ecount;
	int caseStart = -1, caseEnd = 9999999;
	scanf("%d", &ecase);

	if (argc > 1) {
		if (sscanf(argv[1], "%d", &caseStart) == 1) {
			if (argc > 2)
				sscanf(argv[2], "%d", &caseEnd);
		}
		if (caseEnd < caseStart)
			caseEnd = caseStart;
		if (caseEnd != 9999999 && caseEnd >= 1 && caseStart <= 0)
			caseStart = 1;
		if (caseStart > 0)
			fprintf(stderr, "....................DEBUG MODE ENABLED (FROM CASE %d to %d)\n", caseStart, caseEnd);
	}

	for (ecount = 1; ecount <= ecase; ecount++) {
		if (ecount < caseStart || ecount > caseEnd)
			continue;
	
		if (caseStart > 0)
			fprintf(stderr, "....................CASE %d START\n", ecount);

		scanf("%d%d", &en, &ek);
		k2 = ek / 2;
		for (int i = 0; i < en; i++)
			scanf("%lf", &ep[i]);

		ans = 0.0;
		dfs(0, 0);

		printf("Case #%d: %.10lf\n", ecount, ans);
		

		if (caseStart > 0)
			fprintf(stderr, "....................CASE %d END\n", ecount);
	}

	return 0;
}
