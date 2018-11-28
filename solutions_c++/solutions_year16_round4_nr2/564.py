#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

const int MAXN = 205;

int T, N, K;
double P[MAXN];
double dp[MAXN][MAXN];

double gao(int now){
	//printf("%d\n", sta);
	vector<double> tmp;
	for(int i = 0; i < now; ++i)
		tmp.push_back(P[i]);
	for(int i = 0; i < (K - now); ++i)
		tmp.push_back(P[N - i - 1]);
	memset(dp, 0, sizeof(dp));
	dp[0][0] = 1;
	for(int i = 1; i <= K; ++i)
		for(int j = 0; j <= i; ++j){
			dp[i][j] = dp[i - 1][j] * (1 - tmp[i - 1]);
			if(j > 0) dp[i][j] += dp[i - 1][j - 1] * tmp[i - 1];
		}
	return dp[K][K / 2];
}

int main(){
	scanf("%d", &T);
	for(int xx = 1; xx <= T; ++xx){
		scanf("%d%d", &N, &K);
		for(int i = 0; i < N; ++i)
			scanf("%lf", &P[i]);
		double ans = -1;
		sort(P, P + N);
		for(int i = 0; i <= K; ++i)
			ans = max(ans, gao(i));
		printf("Case #%d: %.10lf\n", xx, ans);
	}
}
