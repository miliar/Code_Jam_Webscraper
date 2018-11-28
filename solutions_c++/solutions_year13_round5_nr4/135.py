#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

double dp[1 << 20];
bool v[1 << 20];
char s[30];
int N;

double gao(int msk) {
	if (v[msk]) return dp[msk];
	v[msk] = 1;
	double &ret = dp[msk];
	ret = 0;
	for (int i = 0; i < N; i++) {
		int k = N;
		// printf("i = %d\n", i);
		for (int j = i; ; ) {
			// printf("j = %d\n", j);
			if ((1 << j) & msk) {
				ret += 1.0 / N * (k + gao(msk - (1 << j)));
				break;
			}
			j++;
			k--;
			if (j >= N) j -= N;
		}
	}
	// printf("%d %f\n", msk, ret);
	return ret;
}

int main() {
	int T;
	freopen("x.txt", "r", stdin); freopen("w.txt", "w", stdout); 
	scanf("%d", &T);
	for (int re = 1; re <= T; re++) {
		scanf("%s", s);
		N = strlen(s);
		memset(v, 0, sizeof(v));
		int msk = 0;
		for (int i = 0; i < N; i++) {
			if (s[i] == '.') {
				msk |= 1 << i;
			}
		}
		v[0] = 1;
		dp[0] = 0;
		double ans = gao(msk);
		printf("Case #%d: %.15f\n", re, ans);
	}
}
