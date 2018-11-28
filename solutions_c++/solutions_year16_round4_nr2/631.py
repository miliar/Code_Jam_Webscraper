



#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <queue>
#include <math.h>
#include <string.h>
#include <algorithm>

#define si()        (scanf("%d", &TEMP), TEMP)
#define pii         pair<int, int>
#define fi          first
#define se          second
#define pin(X)      printf("%d\n", (X))
#define pis(X)      printf("%d ", (X))
#define pil()       printf("\n");
#define pb          push_back
#define sz(X)       ((int)(X).size())
#define loop(X, Y)  for (int X = 0 ; X < (Y) ; X++)
#define loopi(X, Y) for (int X = 1 ; X <= (Y) ; X++)

using namespace std;

int TEMP;

double li[500];
double list[500];
double dp[210][210];
int N, K;

double val() {
	memset(dp, 0, sizeof(dp));
	dp[1][0] = 1 - list[0];
	dp[1][1] = list[0];

	for (int i = 2; i <= K; i++) {
		dp[i][0] = (1 - list[i - 1]) * dp[i - 1][0];
		for (int j = 0; j <= i; j++) {
			dp[i][j] = (1 - list[i - 1]) * dp[i - 1][j] + list[i - 1] * dp[i - 1][j - 1];
		}
	}
	
	return dp[K][K / 2];
}

void solve() {
	N = si(), K = si();

	loop(i, N) {
		scanf("%lf", li + i);
	}

	sort(li, li + N);

	double mv = -1;
	for (int i = 0; i <= K; i++) {
		int top = 0;
		for (int j = 0; j < i; j++) list[top++] = li[j];
		for (int j = 0; j < K - i; j++) list[top++] = li[N - 1 - j];
		mv = max(mv, val());
	}
	printf("%lf\n", mv);
}

int main(void) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t = si();
	loopi(i, t) {
		printf("Case #%d: ", i); solve();
	}
}