// In the name of God

#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <deque>
#include <assert.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <stdio.h>
#include <string.h>
#include <utility>
#include <math.h>
#include <bitset>
#include <iomanip>

using namespace std;

#define rep(i, n) for (int i = 0, _n = (int)(n); i < _n; ++i)
#define double long double
/*
#define cin fin
 */
#define cout fout

//ifstream fin(".in");
ofstream fout("res.out");

const int N = 205, M = 13, mod = 0;

double p[N], dp[N][N];


int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int tc;
    cin >> tc;
    rep(ntc, tc) {
        cout << "Case #" << ntc + 1 << ": ";
        // Clear Start

        // Clear End
        // Start
        int n, k;
        cin >> n >> k;
        rep(i, n)
            cin >> p[i];
        sort(p, p + n);
        double best = 0;
        rep(st, k + 1) {
            int ed = k - st;
            rep(i, N)
                rep(j, N)
                dp[i][j] = 0;
            dp[0][0] = 1;
            int cnt = k / 2, seen = 0;
            rep(i, n) if (i < st || i + ed >= n) {
                double prob = p[i];
                seen++;
                for (int j = 0; j <= min(cnt, seen); ++j) {
                    int k = seen - j;
                    if (j) dp[j][k] += dp[j - 1][k] * prob;
                    if (k) dp[j][k] += dp[j][k - 1] * (1 - prob);
                }
            }
            best = max(best, dp[cnt][cnt]);
        }
        // End
        cout << fixed << setprecision(15) << best << '\n';
    }
}













