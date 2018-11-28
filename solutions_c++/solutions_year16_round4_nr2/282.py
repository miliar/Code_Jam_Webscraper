#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
#include <cmath>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdlib>

using namespace std;

#define TASKNAME ""

void solve(int test_number);

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.setf(ios::fixed);
    cout.precision(9);
    cerr.setf(ios::fixed);
    cerr.precision(3);
#ifdef LOCAL
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
#else
#endif
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        solve(i);
    }
}

const int MAX_N = 405;

double dp[MAX_N][2 * MAX_N];
vector<double> p;

/*
double solve(int n, int k, int balance) {
    if (n < 0) {
        return make_pair((k == 0 && balance == 0), 0);
    }
    if (k == 0) {
        return make_pair((balance == 0), 0);
    }
    pair<double, double>& x = dp[n][k][balance + MAX_N];
    if (x >= 0) {
        return x;
    }
    x = solve(n - 1, k, balance);
    pair<double, double> a = solve(n - 1, k - 1, balance + 1);
    pair<double, double> b = solve(n - 1, k - 1, balance - 1);
    x = make_pair(p[n] * a.first + (1 - p[n]) * a.second;
    return x;
}
*/

double solve(int n, int balance) {
    if (n < 0) {
        return balance == 0;
    }
    double& x = dp[n][balance + MAX_N];
    if (x >= 0) {
        return x;
    }
    x = p[n] * solve(n - 1, balance + 1) + (1 - p[n]) * solve(n - 1, balance - 1);
    return x;
}

void solve(int test_number) {
    int n, k;
    cin >> n >> k;
    double pp[MAX_N];
    for (int i = 0; i < n; i++) {
        cin >> pp[i];
    }
    sort(pp, pp + n);
    double ans = 0;
    for (int i = 0; i <= k; i++) {
        p.clear();
        for (int j = 0; j < i; j++) {
            p.push_back(pp[j]);
        }
        for (int j = 0; j < k - i; j++) {
            p.push_back(pp[n - j - 1]);
        }
        memset(dp, -1, sizeof(dp));
        ans = max(ans, solve(k - 1, 0));
    }
    /*
    double ans = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        if (__builtin_popcount(mask) != k) {
            continue;
        }
        p.clear();
        for (int j = 0; j < n; j++) {
            if (mask & (1 << j)) {
                p.push_back(pp[j]);
            }
        }
        memset(dp, -1, sizeof(dp));
        ans = max(ans, solve(k - 1, 0));
    }
    */
    cout << "Case #" << test_number + 1 << ": ";
    cout << ans << endl;
}
