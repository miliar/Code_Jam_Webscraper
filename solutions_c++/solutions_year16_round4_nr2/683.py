#include <bits/stdc++.h>

using namespace std;

double p[210];
double dp[210][210];
int n, k;
const double eps = 1E-9;

double calc(const vector<double> &ch) {
    assert(ch.size() == k);
    for (int i = 0; i <= ch.size(); i++) {
        for (int j = 0; j <= ch.size(); j++) {
            dp[i][j] = 0.0;
        }
    }
    dp[0][0] = 1.0;
    for (int i = 0; i < k; i++) {
        for (int j = 0; j < k; j++) {
            dp[i + 1][j] += dp[i][j] * (1.0 - ch[i]);
            dp[i + 1][j + 1] += dp[i][j] * ch[i];
        }
    }
    return dp[k][k/2];
}

void solve(int test_id) {
    cout << "Case #" << test_id << ": ";
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> p[i];
    }

    sort(p, p + n);
    /*double ans = 0.0;
    vector<int> best;
    for (int i = 0; i < (1 << n); i++) {
        if (__builtin_popcount(i) != k) {
            continue;
        }
        vector<double> cand;
        vector<int> who;
        for (int j = 0; j < n; j++) {
            if ( i & (1 << j) ) {
                cand.push_back(p[j]);
                who.push_back(j);
            }
        }
        if (ans < calc(cand) ) {
            ans = calc(cand);
            best = who;
        }
    }

    cout << fixed << setprecision(12) << ans << endl;
    for (int i = 0; i < n; i++) {
        cerr << fixed << setprecision(3) << p[i] << " ";
    }
    cerr << endl;
    cerr << n << " " << k << endl;
    for (int i = 0; i < best.size(); i++) {
        cerr << best[i] << " ";
    }
    cerr << endl;*/

    double myans = 0.0;
    for (int i = 0; i <= k; i++) {
        vector<double> cand;
        for (int j = 0; j < i; j++) {
            cand.push_back(p[j]);
        }
        for (int j = 1; j <= k - i; j++) {
            cand.push_back(p[n - j]);
        }
        myans = max(myans, calc(cand) );
    }
    //assert( fabs(ans - myans) < eps );
    cout << fixed << setprecision(12) << myans << endl;
}

int main () {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        solve(i);
    }
    return 0;
}
