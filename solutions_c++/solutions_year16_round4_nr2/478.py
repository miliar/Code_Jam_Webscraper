#define _USE_MATH_DEFINES
#include <algorithm>
#include <cstdio>
#include <functional>
#include <iostream>
#include <cfloat>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <queue>
#include <random>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <time.h>
#include <vector>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> i_i;
typedef pair<ll, int> ll_i;
typedef pair<double, int> d_i;
typedef pair<ll, ll> ll_ll;
typedef pair<double, double> d_d;
struct edge { int u, v; ll w; };

int INF = INT_MAX / 2;
ll MOD = 1000000007;
ll _MOD = 1000000009;
double EPS = 1e-10;

int main() {
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		int N, K; cin >> N >> K;
		vector<double> p(N);
		for (double& x: p) cin >> x;
		sort(p.begin(), p.end());
		double ma = 0;
		for (int l = 0; l <= K; l++) {
			int r = K - l;
			vector<double> a;
			for (int i = 0; i < l; i++)
				a.push_back(p[i]);
			for (int i = N - r; i < N; i++)
				a.push_back(p[i]);
			vector<double> dp(K + 1);
			dp[0] = 1;
			for (double x: a) {
				vector<double> _dp(K + 1);
				for (int k = 0; k < K; k++) {
					_dp[k + 1] += dp[k] * x;
					_dp[k] += dp[k] * (1 - x);
				}
				dp = _dp;
			}
			ma = max(ma, dp[K / 2]);
		}
		printf("Case #%d: %.15f\n", t, ma);
	}
}
