#include <bits/stdc++.h>

template<typename T> T gcd(T a, T b) {
    if(!b) return a;
    return gcd(b, a % b);
}
template<typename T> T lcm(T a, T b) {
    return a * b / gcd(a, b);
}

template<typename T> void chmin(T& a, T b) { a = (a > b) ? b : a; }
template<typename T> void chmax(T& a, T b) { a = (a < b) ? b : a; }
int in() { int x; scanf("%d", &x); return x; }

using namespace std;

typedef long long Int;
typedef unsigned uint;

const int MAXN = 100005;
const double INF = 99999999999999999.0;

int T;
double C, F, X;
map<double, map<int, double> > dp;

int cnt = 0;

double func(double cookie, double clicks) {
	if (cookie < 0.0 || cookie > X || clicks > 9990.0) return INF;
	if (abs(cookie -X) < 1e-6) {		
		return 0.0;
	} else {
		if (dp[cookie][clicks] != 0.0) return dp[cookie][clicks];
		dp[cookie][clicks] = INF;

		double tans = (X - cookie) / (2.0 + F * clicks) + func(X, clicks);

		if (cookie >= C) {
			tans = min(tans, (C - cookie) / (2 + F * clicks) + func(cookie - C, clicks + 1));
		}
		tans = min(tans, (C - cookie) / (2 + F * clicks) + func(C, clicks));
		
		return dp[cookie][clicks] = tans;
	}
}

int main(void) {
	cin >> T;
	freopen("o.ot", "w", stdout);

	for (int t = 1; t <= T; t++) {
		cin >> C >> F >> X;

		dp.clear();
		printf("Case #%d: %.7lf\n", t, func(0.0, 0));
	}
    return 0;
}
