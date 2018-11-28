#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
using namespace std;

int n, k;
double ps[16], cur[16];
double ans;

double calc() {
	vector<double> dp(k / 2 + 1, 0);
	dp[0] = 1;
	for (int i = 0; i < k; ++i) {
		vector<double> newdp(k / 2 + 1, 0);
		newdp[0] = (1 - cur[i]) * dp[0];
		for (int j = 1; j <= k / 2; ++j) newdp[j] = cur[i] * dp[j - 1] + (1 - cur[i]) * dp[j];
		dp = move(newdp);
	}
	return dp[k / 2];
}

void dfs(int at, int pos) {
	if (pos == k) {
		double t = calc();
		if (t > ans) ans = t;
		return;
	}
	for (int i = at; i < n; ++i) {
		cur[pos] = ps[i];
		dfs(i + 1, pos + 1);
	}
}

int main() {
	FILE *fp = fopen("B-small-attempt0.in", "r");
	FILE *fout = fopen("out.txt", "w");
	int T;
	fscanf(fp, "%d", &T);
	for (int iii = 0; iii < T; ++iii) {
		fscanf(fp, "%d%d", &n, &k);
		for (int i = 0; i < n; ++i) fscanf(fp, "%lf", &ps[i]);
		ans = 0;
		dfs(0, 0);
		fprintf(fout, "Case #%d: %lf\n", iii + 1, ans);
	}
	fclose(fp);
	fclose(fout);
	return 0;
}