#include <algorithm>
#include <assert.h>
#include <complex>
#include <ctype.h>
#include <functional>
#include <iostream>
#include <limits.h>
#include <locale.h>
#include <map>
#include <math.h>
#include <queue>
#include <set>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <vector>
#include <unordered_set>
#include <unordered_map>

#pragma warning(disable:4996)
using namespace std;

#define mp make_pair
typedef long long ll;
typedef unsigned long long ull;
typedef double db;
typedef long double ldb;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;
typedef pair <ll, int> pli;
typedef pair <ldb, ldb> pdd;

int IT_MAX = 1 << 17;
const int MOD = 10007;
const int INF = 1034567890;
const ll LL_INF = 1234567890123456789ll;
const db PI = acos(-1);
const ldb ERR = 1E-10;

ldb in[205];
vector <ldb> tin;
ldb dp[205][205];
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int tc = 1; tc <= T; tc++) {
		int N, K, i, j, k;
		scanf("%d %d", &N, &K);
		for (i = 1; i <= N; i++) {
			db t;
			scanf("%lf", &t);
			in[i] = t;
		}
		sort(in + 1, in + N + 1);

		ldb ans = 0;
		for (i = 0; i <= K; i++) {
			tin.push_back(0);
			for (j = 1; j <= i; j++) tin.push_back(in[j]);
			for (j = N; j > N - (K - i); j--) tin.push_back(in[j]);

			dp[0][0] = 1;
			for (j = 1; j <= K; j++) {
				for (k = 0; k <= j; k++) {
					dp[j][k] = 0;
					if (k != 0) dp[j][k] += dp[j - 1][k - 1] * tin[j];
					if (k != j) dp[j][k] += dp[j - 1][k] * (1 - tin[j]);
				}
			}
			ans = max(ans, dp[K][K / 2]);

			tin.clear();
		}
		printf("Case #%d: %.20lf\n", tc, (db)ans);
	}
	return 0;
}
//*/