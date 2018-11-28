#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <memory>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

const int N = (int)1e5 + 4;
const int inf = (int)1e9 + 7;
const int M = 101;

long double dp[2 * M][M];
long double p[2 * M];

void brute(int T) {
    int n, k;
    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; ++i) {
        scanf("%Lf", &p[i]);
    }
    long double ans = 0.0;
    for (int i = 0; i < (1 << n); ++i) {
        vector<int> d;
        int c = 0;
        for (int j = 0; j < n; ++j) {
            if (((1 << j) & i)) {
                d.push_back(j);
                ++c;
            }
        }
        if (c != k) {
            continue;
        }
        long double w = 0.0;
        for (int j = 0; j < (1 << c); ++j) {
            int q = 0;
            long double s = 1.0;
            for (int t = 0; t < c; ++t) {
                if (((1 << t) & j)) {
                    s *= p[d[t]];
                    ++q;
                } else {
                    s *= (1.0 - p[d[t]]);
                }
            }
            if (2 * q == c) {
                w += s;
            }
        }
        ans = max(w, ans);
    }
    printf("Case #%d: %.7Lf\n", T, ans);
}

void solve(int T) {
    int n, k;
    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; ++i) {
        scanf("%Lf", &p[i]);
    }
    long double ans = 0.0;
    sort(p, p + n);
    for (int i = -1; i < k; ++i) {
        vector<long double> d;
        for (int j = 0; j <= i; ++j) {
            d.push_back(p[j]);
        }
        for (int j = n - 1; j >= n - k + i + 1; --j) {
            d.push_back(p[j]);
        }
        memset(dp, 0.0, sizeof dp);
        dp[0][0] = 1.0;
        for (int j = 1; j <= k; ++j) {
            dp[j][0] = dp[j - 1][0] * d[j - 1];
            for (int t = 1; t <= j; ++t) {
                dp[j][t] = dp[j - 1][t] * d[j - 1] + dp[j - 1][t - 1] * (1.0 - d[j - 1]);
            }
        }
        ans = max(ans, dp[k][k / 2]);
    }
    printf("Case #%d: %.7Lf\n", T, ans);
}


int main() {
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        solve(t);
    }
    return 0;
}