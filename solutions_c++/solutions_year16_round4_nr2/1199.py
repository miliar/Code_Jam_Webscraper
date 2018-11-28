#include <cassert>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
#include <utility>

using namespace std;

int N, K;
long double P[205];
int selected[205];
long double dp[205];

long double dfs(int count)
{
	if (count < K) {
		long double ans = 0.0;
		int last = count > 0 ? selected[count-1] : -1;
		for (int i = last+1; i < N; i++) {
			selected[count] = i;
			ans = max(ans, dfs(count+1));
		}
		return ans;
	}

	dp[0] = 1.0;
	for (int i = 1; i < count; i++) {
		dp[i] = 0.0;
	}
	for (int i = 0; i < count; i++) {
		int index = selected[i];
		for (int j = count; j >= 0; j--) {
			dp[j] = (1 - P[index]) * dp[j] + P[index] * dp[j-1];
		}
	}
	return dp[count/2];
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		scanf("%d%d", &N, &K);
		for (int i = 0; i < N; i++) {
			scanf("%Lf", &P[i]);
		}
		long double ans = dfs(0);
		printf("%Lf\n", ans);
	}
	return 0;
}
