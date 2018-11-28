#line 1 "B.cpp"
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <string>
#include <cassert>
#include <cmath>
#include <cstring>
#include <functional>
#include <random>
using namespace std;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef long long ll;
#define REP(i,a,n) for (int i = (a); i < (n); i++)

template<class T> T& setmin(T &a, const T &b) {return a = min(a, b);}
template<class T> T& setmax(T &a, const T &b) {return a = max(a, b);}
template<class T> T MODD(const T &a, const T &b) {T r = a%b; if (r < 0) r += b; return r;}

int N, K;

void bla(const vector<double> &p, vector<vector<double> > &dp) {
	dp[0][0] = 1;
	REP(i,1,N) {
		REP(s,0,i+1) {
			if (s > 0)
				dp[i][s] += dp[i-1][s-1]*p[i-1];
			if (s < i)
				dp[i][s] += dp[i-1][s]*(1-p[i-1]);
		}
	}
}

void docase() {
	scanf("%d%d", &N, &K);
	vector<double> p(N);
	REP(i,0,N) {
		scanf("%lf", &p[i]);
	}
	sort(p.begin(), p.end());
	vector<vector<double> > dp1(N+1, vector<double>(N+1, 0));
	bla(p, dp1);
	reverse(p.begin(), p.end());
	vector<vector<double> > dp2(N+1, vector<double>(N+1, 0));
	bla(p, dp2);
	double res = 0;
	REP(x,0,K+1) {
		int y = K-x;
		double h = 0;
		REP(s,0,x+1)
			h += dp1[x][s]*dp2[y][K/2-s];
		setmax(res, h);
	}
	printf("%.9lf\n", res);
}

int main() {
	int T;
	scanf("%d ", &T);
	for (int test = 0; test < T; test++) {
		fprintf(stderr, "Test %d/%d\n", test+1, T);
		printf("Case #%d: ", test+1);
		docase();
		fflush(stdout);
		fflush(stderr);
	}
	return 0;
}
