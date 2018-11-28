#include <string>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <string.h>
#include <queue>
#include <cstdio>
#include <cassert>
#include <deque>
#include <stack>
#include <utility>
#include <numeric>
#include <ctime>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forv(i, v) forn(i, v.size())

#define mp make_pair
#define pb push_back
#define all(v) v.begin(), v.end()

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

const int MAXN = 105;

int dp[MAXN][2][MAXN * 10];

void solve(int tc) {
    cerr << "Case #" << tc << ", " << clock() << " ms.\n";
    cout << "Case #" << tc << ": ";
    int p, q, n;
    cin >> p >> q >> n;
    vector<int> h(n), g(n);
    forn(i, n) cin >> h[i] >> g[i];
    memset(dp, 255, sizeof(dp));
    dp[0][0][0] = 0;
    forn(i, n) {
        forn(j, MAXN * 10) {			
            if (dp[i][0][j] != -1) {
				int z = (h[i] + q - 1) / q;
				dp[i + 1][0][j + z] = max(dp[i + 1][0][j + z], dp[i][0][j]);
				for (int prev = 0; prev <= j; prev++) {
					int rh = h[i] - prev * p;
					if (rh <= 0) {
						dp[i + 1][0][j - prev] = max(dp[i + 1][0][j - prev], dp[i][0][j] + g[i]);
						break;
					}
					forn(x, 11) {
						forn(y, x + 1) {
							if (rh - x * q - (x - y) * p > 0 &&
								rh - x * q - (x - y + 1) * p <= 0) {
									dp[i + 1][1][j - prev + y] = max(dp[i + 1][1][j - prev + y], dp[i][0][j] + g[i]);
								}
						}
					}
				}    
			}
			if (dp[i][1][j] != -1) {
				int z = (h[i] + q - 1) / q;
				dp[i + 1][0][j + z - 1] = max(dp[i + 1][0][j + z - 1], dp[i][1][j]);
				for (int prev = 0; prev <= j; prev++) {
					int rh = h[i] - prev * p;
					if (rh <= 0) {
						dp[i + 1][1][j - prev] = max(dp[i + 1][1][j - prev], dp[i][1][j] + g[i]);
						break;
					}
					forn(x, 11) {
						forn(y, x + 1) {
							if (rh - (x + 1) * q - (x - y) * p > 0 &&
								rh - (x + 1) * q - (x - y + 1) * p <= 0) {
									dp[i + 1][1][j - prev + y] = max(dp[i + 1][1][j - prev + y], dp[i][1][j] + g[i]);
								}
						}
					}
				}  
			}
        }
    }
    int ans = 0;
    forn(j, MAXN) ans = max(ans, max(dp[n][0][j], dp[n][1][j]));
    cout << ans << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    cin >> tc;
    forn(i, tc) solve(i + 1);
    return 0;
}
