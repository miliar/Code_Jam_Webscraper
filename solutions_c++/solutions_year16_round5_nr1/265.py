#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

#define FOR(i,a,b) for (int i=int(a);i<=int(b);++i)
#define REP(i,n) FOR(i,0,(n)-1)
#define PB push_back

const int inf = 1 << 28;
int cost[2010][2010], dp[2010][2010];
string s;

int calc(int a, int b) {
	if (dp[a][b] >= 0) return dp[a][b];
	int ret = cost[a][b];
	if (a+1 < b-1) ret = min(ret, calc(a+1, b-1) + (s[a] != s[b-1]));
	for (int len = 2; a + len < b; len += 2) {
		ret = min(ret, calc(a, a+len) + calc(a+len, b));
	}
	return dp[a][b] = ret;
}

int main() {
	int tN;
	cin >> tN;
	FOR(cN, 1, tN) {
		cin >> s;
		// cout << s << endl;
		int n = s.size();
		memset(cost, 0, sizeof(cost));
		memset(dp, -1, sizeof(dp));
		REP(i, n)
		for (int len = 2; i+len <= n; len += 2) {
			int j = i+len;
			for (int k = 0; i+k < j-1-k; ++k) if (s[i+k] != s[j-1-k]) ++cost[i][j];
			// printf("cost[%d][%d] = %d\n", i, j, cost[i][j]);
		}
		int ans = calc(0, n);
		cout << "Case #" << cN << ": " << (n - ans) * 5 << endl;
	}
}
