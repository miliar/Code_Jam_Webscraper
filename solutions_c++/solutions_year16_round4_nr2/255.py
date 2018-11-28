#include <cstdio>
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

typedef long double ld;

const int Maxn = 205;

int t;
int n, k;
ld prob[Maxn];
ld col[Maxn];
int clen;
ld dp[Maxn][Maxn];

ld getResult()
{
	fill((ld*)dp, (ld*)dp + Maxn * Maxn, 0.0);
	dp[0][0] = 1;
	for (int i = 0; i < k; i++)
		for (int j = 0; j < k; j++) {
			dp[i + 1][j] += dp[i][j] * (1 - col[i]);
			dp[i + 1][j + 1] += dp[i][j] * col[i];
		}
	return dp[k][k / 2];
}

int main()
{
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		cin >> n >> k;
		for (int i = 0; i < n; i++)
			cin >> prob[i];
		sort(prob, prob + n);
		ld res = 0;
		for (int i = 0; i <= k; i++) {
			int j = k - i;
			clen = 0;
			for (int l = 0; l < i; l++)
				col[clen++] = prob[l];
			for (int l = 0; l < j; l++)
				col[clen++] = prob[n - 1 - l];
			res = max(res, getResult());
		}
		printf("Case #%d: ", tc);
		cout << fixed << setprecision(15) << res << endl;
	}
	return 0;
}