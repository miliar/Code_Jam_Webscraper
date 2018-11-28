#include <iostream>
#include <string>
#include <map>
#include <math.h>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>
#include <queue>
#include <sstream>
#include <deque>
#include <memory.h>
#include <cassert>
#include <ctime>


using namespace std;

#define ll long long
#define y1 _dfdfdfd


const int maxn = 105;
const int maxm = maxn * 13;
const int inf = 1000000007;
const int mod = 1000000007;

int n, p, q;
int a[maxn], b[maxn], f[maxn];
int dp[maxn][maxn][maxm][2];
int need[maxn], needt[maxn], sum[maxn];

int fastsolve() {
        for (int i = 0; i < n; i++) {
            needt[i] = a[i] / q + !!(a[i] % q);
            sum[i] = (i ? sum[i - 1] : 0) + needt[i];
            need[i] = a[i] / p + !!(a[i] % p);
            int x = a[i];
            int o = 1;
            f[i] = 0;
            while (x > 0) {
                if ((x - 1) % q + 1 <= p) {
                    if (o < need[i] && x > p) {
                        need[i] = o;
                        f[i] = 1;
                    }
                    break;
                }
                o++;
                x -= p;
            }
        }
        
        memset(dp, -1, sizeof(dp));
        dp[0][0][0][0] = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                for (int k = 0; k < maxm; k++) {
                    dp[i][j][k][1] = max(dp[i][j][k][1], dp[i][j][k][0]);
                    for (int o = 0; o < 2; o++) if (dp[i][j][k][o] != -1) {
                        {
                            dp[i + 1][j][k][0] = max(dp[i + 1][j][k][0], dp[i][j][k][o]);
                        }
                        if (o == 0 || o == 1 && needt[i] > 1) {
                            int tower = sum[i] - (j + 1);
                            int we = k + need[i];
                            if (tower >= we - 1) {
                                assert(we < maxm);
                                dp[i + 1][j + 1][we][1] = max(dp[i + 1][j + 1][we][1], dp[i][j][k][o] + b[i]);
                            }
                        }
                        {
                            int tower = sum[i] - (j + 1);
                            int we = k + (a[i] / p + !!(a[i] % p));
                            if (tower >= we - 1) {
                                assert(we < maxm);
                                dp[i + 1][j + 1][we][tower == we] = max(dp[i + 1][j + 1][we][tower == we], dp[i][j][k][o] + b[i]);
                            }                            
                        }
                    }
                }
            }
        }
        int ans = 0;
        for (int j = 0; j <= n; j++) for (int k = 0; k < maxm; k++) for (int o = 0; o < 2; o++) ans = max(ans, dp[n][j][k][o]);
        return ans;
}

int slowsolve() {
    return -1;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; test++) {
        cerr << "Case #" << test << ": ";
        cout << "Case #" << test << ": ";

        cin >> p >> q >> n;
        for (int i = 0; i < n; i++) cin >> a[i] >> b[i];
        int res = fastsolve();
        cout << res << endl;
        cerr << res << endl;
    }

	return 0;
}
