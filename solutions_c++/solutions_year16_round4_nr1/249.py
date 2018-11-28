#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

#define FOR(i,a,b) for (int i=int(a);i<=int(b);++i)
#define REP(i,n) FOR(i,0,(n)-1)
#define PB push_back

int cnt[13][3][3], inp[3];
string ans[13][3];

int main() {
	ans[0][0] = "R";
	ans[0][1] = "P";
	ans[0][2] = "S";
	cnt[0][0][0] = 1;
	cnt[0][1][1] = 1;
	cnt[0][2][2] = 1;
	FOR(i, 1, 12)
	REP(j, 3) {
		int bj = (j+1)%3;
		if (ans[i-1][j] < ans[i-1][bj]) ans[i][bj] = ans[i-1][j] + ans[i-1][bj];
		else ans[i][bj] = ans[i-1][bj] + ans[i-1][j];
		REP(k, 3) cnt[i][bj][k] = cnt[i-1][j][k] + cnt[i-1][bj][k];
	}
	int tN;
	cin >> tN;
	FOR(cN, 1, tN) {
		int n, p, r, s;
		cin >> n;
		REP(k, 3) cin >> inp[k];
		cout << "Case #" << cN << ": ";
		bool ok;
		REP(j, 3) {
			ok = 1;
			REP(k, 3) if (inp[k] != cnt[n][j][k]) ok = 0;
			if (ok) {
				cout << ans[n][j] << endl;
				break;
			}
		}
		if (!ok) cout << "IMPOSSIBLE" << endl;
	}
}
