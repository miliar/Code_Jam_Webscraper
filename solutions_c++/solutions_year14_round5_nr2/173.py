#pragma comment(linker,"/stack:256000000")

#include <cmath> 
#include <ctime> 
#include <iostream> 
#include <string> 
#include <vector> 
#include <algorithm> 
#include <set> 
#include <map> 
#include <cstring> 
#include <cstdlib> 
#include <queue> 
#include <cstdio> 
#include <cfloat>
#include <cassert>

using namespace std; 

#define REP(i, n) for (int (i) = 0; (i) < (n); (i)++) 
#define sz(v) (int)(v).size() 
#define all(v) (v).begin(), (v).end()

const int INF = (int)1e9;

void upd(int &a, int b) {
	a = max(a, b);
}

int dp[110][1010][2];
int h[110], g[110];

void solve() {
	int p, q, n;
	cin >> p >> q >> n;
	REP(i, n) cin >> h[i] >> g[i];
	REP(i, 110) REP(j, 1010) REP(k, 2) dp[i][j][k] = -INF;
	dp[0][0][0] = 0;
	REP(i, n) {
		for (int j = 0; j <= 10 * i; j++) {
			for (int k = 0; k < 2; k++) {
				for (int x = 0; x <= min(j, 10); x++) {
					int cur = h[i] - x * p;
					if (cur <= 0) {
						upd(dp[i + 1][j - x][k], dp[i][j][k] + g[i]);
						break;
					} else {
						if (k > 0) {
							cur -= q;
						}
						if (cur <= 0) {
							upd(dp[i + 1][j - x][0], dp[i][j][k]);
						} else {
							for (int y = 0; y <= 10; y++) {
								int tmp = cur - y * q;
								if (tmp <= 0) {
									upd(dp[i + 1][j - x + y][0], dp[i][j][k]);
									break;
								}
								while (tmp >= 1) {
									tmp -= p;
									if (tmp <= 0) {
										upd(dp[i + 1][j - x + y][1], dp[i][j][k] + g[i]);
										break;
									}
									tmp -= q;
									if (tmp <= 0) {
										upd(dp[i + 1][j - x + y][0], dp[i][j][k]);
										break;
									}
								}
							}
						}
					}
				}
			}
		}
	}
	int res = 0;
	REP(i, 1010) REP(j, 2) res = max(res, dp[n][i][j]);
	cout << res;
}

int main() {
#ifdef LOCAL
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif
	int T;
	cin >> T;
	for (int tst = 1; tst <= T; tst++) {
		cout << "Case #" << tst << ": ";
		solve();
		cout << endl;
	}
	return 0;
}