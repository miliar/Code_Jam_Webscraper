#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <cassert>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#define RD(x)      scanf("%d", &x)
#define REP(i, n)  for (int i=0; i<(n); i++)
#define FOR(i, n) for (int i=1; i<=(n); i++)
#define pii        pair<int, int>
#define mp         make_pair
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

using namespace std;
#define  N   1160
#define  M   22222
#define  eps 1e-9
#define  pi  acos(-1.0)
#define  inf 0XFFFFFFFll
#define  mod 9999991ll
#define  LL  long long

int dp[1<<20];
string s[N];
int a[10][10];
int work(int b[], int cnt) {
	set<string> st;
	REP(i, cnt) {
		FOR(j, s[b[i]].length())
			st.insert(s[b[i]].substr(0, j));
	}
	return st.size();
}
int m, n, r;
int Main() {
	freopen("D-small-attempt0.in", "r", stdin);
//	freopen("out.txt", "w", stdout);
//	int T; RD(T);
	int T;
	cin >> T;
	FOR(_T, T) {
//		RD(m); RD(n);
		cin >> m >> n;
		memset(dp, 0, sizeof dp);
		REP(i, m) cin >> s[i];
		r = 1;
		REP(i, m) r *= n;
		int ans = 0;
		REP(i, r) {
			int st = i;
			memset(a, 0, sizeof a);
			REP(j, m) {
				int k = st % n;
				st /= n;
				a[k][++a[k][0]] = j;
			}
			REP(j, n) {
				dp[i] += work(a[j] + 1, a[j][0]);
				if (a[j][0] == 0) {
					dp[i] = 0;
					break;
				}
			}
			ans = max(ans, dp[i]);
		}
		int num = 0;
		REP(i, r) if (dp[i] == ans) num++;
		printf("Case #%d: %d %d\n", _T, ans + n, num);
	}
	return 0;
}
int main() {
	return Main();
}
