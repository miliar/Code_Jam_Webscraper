#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <climits>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <ctime>
#include <iostream>
#include <sstream>
#include <cctype>

#define PI 3.14159265358979
#define EPS 1e-9

using namespace std;

#define REP(i, n) for (int i=0; i<n; i++)
#define FOR(i, m, n) for (int i=m; i<=n; i++)
#define ABS(a) (((a)>0)?(a):(-(a)))
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> ii;

int n,k;
double p[222];
bool chosen[222];
vector<double> pst;
double ans;
double dp[222][500];

double sol(int K) {
	pst.clear();
	REP(i, n) if ((K & (1<<i))!=0) pst.push_back(p[i]);
	if (pst.size()!=k) return 0.0;

	REP(i, n+1) REP(j, 500) dp[i][j] = 0.0;
	dp[0][250] = 1.0;
	REP(i, pst.size()) {
		REP(j, 500) {
			if (j<499) dp[i+1][j+1] += pst[i]*dp[i][j];
			if (j>0) dp[i+1][j-1] += (1-pst[i])*dp[i][j];
		}
	}
	return dp[pst.size()][250];
}

void solve() {
	ans = 0.0;
	pst.clear();
	cin >> n >> k;
	REP(i, n) cin >> p[i];
	REP(i, n) chosen[i] = 0;
	int N = 1<<n;
	REP(i, N) {
		ans = max(ans, sol(i));
	}
	cout << ans << endl;
}

int main() {
	int t; scanf("%d", &t);
	REP(i, t) {
		printf("Case #%d: ", i+1);
		solve();
	}
	return 0;
}
