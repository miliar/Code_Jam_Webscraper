#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <map>
using namespace std;
typedef long long lld;

char S[128];
int D[128][2];

void input() {
	scanf("%s", S);
}

int min(int x, int y) { return x < y ? x : y; }

int dp(int n, int p) { // min cost for 1..n => p{1:+, 0:-}
	if (n < 0) return 0;
	if (D[n][p] != -1) return D[n][p];

	int r;
	if (p == 1) {
		if (S[n] == '+') r = dp(n - 1, p);
		else {
			r = dp(n - 1, 0) + 1;
		}
	}
	else if (p == 0) {
		if (S[n] == '-') r = dp(n - 1, p);
		else {
			r = dp(n - 1, 1) + 1;
		}
	}
	return D[n][p] = r;
}

void solve(int icase) {
	int ans = 0;
	memset(D, -1, sizeof D);
	ans = dp(strlen(S) - 1, 1);
	printf("Case #%d: %d\n", icase, ans);
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		input();
		solve(i);
	}
}