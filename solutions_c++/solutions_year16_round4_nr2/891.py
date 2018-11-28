#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

using std::max;
using std::sort;
using std::vector;

double dp[300][300];
double in[300];
bool sel[300];
vector<double> in2;

int T, N, K;
double ans;

void dfs(int n, int k) {
	if(n==N) {
		if(k==K) {
			in2 = vector<double>();
			in2.push_back(0.0);
			for(int i=0; i<n; i++) {
				if(sel[i]) in2.push_back(in[i]);
			}
			memset(dp, 0, sizeof(dp));
			dp[0][0] = 1.0;
			for(int ki=1; ki<=K; ki++) {
				for(int yi=0; yi<=ki; yi++) {
					dp[ki][yi] += dp[ki-1][yi]*(1-in2[ki]);
					if(yi > 0) {
						dp[ki][yi] += dp[ki-1][yi-1]*in2[ki];
					}
				}
			}
			ans = max(ans, dp[K][K/2]);
		}
		return;
	}
	dfs(n+1, k);
	sel[n] = true;
	dfs(n+1, k+1);
	sel[n] = false;
}

int main() {
	scanf("%d", &T);
	for(int tc=1; tc<=T; tc++) {
		scanf("%d%d", &N, &K);
		memset(sel, 0, sizeof(sel));
		ans = 0.0;
		for(int i=0; i<N; i++) {
			scanf("%lf", &in[i]);
		}
		dfs(0, 0);
		printf("Case #%d: %f\n", tc, ans);
	}
	return 0;
}
