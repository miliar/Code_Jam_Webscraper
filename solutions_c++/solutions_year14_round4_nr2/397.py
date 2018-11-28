#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

const int MAXN = 1005;

int N, cases;
int T[MAXN];
pair<int, int> A[MAXN];
int dp[MAXN][MAXN];	

int main(){
	scanf("%d", &cases);
	for(int xx = 1; xx <= cases; ++xx){
		scanf("%d", &N);
		for(int i = 0; i < N; ++i){
			scanf("%d", &A[i].first);
			A[i].second = i;
			T[i] = A[i].first;
		}
		sort(A, A + N);
		memset(dp, 127, sizeof(dp));
		int ans = dp[0][0];
		dp[0][0] = 0;
		for(int i = 0; i < N + 1; ++i)
			for(int j = 0; i + j <= N; ++j){
				if(i == 0 && j == 0) continue;
				int l = 0, r = 0;
				int now = A[i + j - 1].second;
				for(int k = now; k >= 0; --k)
					if(T[k] > T[now]){
						++l;
					}
				for(int k = now; k < N; ++k)
					if(T[k] > T[now]){
						++r;
					}
				if(i > 0){
					dp[i][j] = min(dp[i][j], dp[i - 1][j] + l);
				}
				if(j > 0){
					dp[i][j] = min(dp[i][j], dp[i][j - 1] + r);
				}
				if(i + j == N){
					ans = min(ans, dp[i][j]);
				}
			}
		printf("Case #%d: %d\n", xx, ans);
	}
}
