#include <iostream>
#include <algorithm>
#include <bitset>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <iomanip>
#include <queue>
#include <utility>
#include <cmath>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<int, char> pci;

const int kN = 500;
const int kZero = 250;
const double kInf = 1e+9;

vector<double> p;
double pp[kN];

double dp[kN][kN];
bool used[kN][kN];


double DP(int n, int bal) {
    if (n < 0) {
        return 0.0;
    }
    if (n == 0) {
        return bal == 0 ? 1.0 : 0.0;
    }
    int bal_ = bal + kZero;
    if (!used[n][bal_]) {
        used[n][bal_] = 1;
        dp[n][bal_] = DP(n - 1, bal - 1) * p[n - 1] + DP(n - 1, bal + 1) * (1.0 - p[n - 1]);
        // cerr << "n = " << n << " k = " << k << " bal = " << bal << " dp = " << dp[n][k][bal_] << "\n";
    }
    return dp[n][bal_];
}

int main() {
    std::ios_base::sync_with_stdio(false);
    int tests_count;
    cin >> tests_count;
    for (int test_index = 0; test_index < tests_count; ++test_index) {

            memset(used, 0, sizeof(used));
            int n, k;
            cin >> n >> k;
            for (int i = 0; i < n; ++i) {
                cin >> pp[i];
            }
            double best = -1;
        for (int mask = 0; mask < (1 << n); ++mask) {
            int cnt = 0;
            for (int i = 0; i < n; ++i) {
                cnt += ((mask & (1 << i)) > 0);
            }
            if (cnt != k) {
                continue;
            }
            p.clear();
            for (int i = 0; i < n; ++i) {
                if (mask & ( 1 << i)) p.push_back(pp[i]);
            }
        memset(used, 0, sizeof(used));
        best = max(best, DP(k, 0));
        }
        cout.precision(7);
        cout << "Case #" << test_index + 1 << ": ";
        cout << fixed << best << "\n";
    }
    return 0;
}
