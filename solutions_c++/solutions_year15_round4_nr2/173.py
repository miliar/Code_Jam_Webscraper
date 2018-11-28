#include <bits/stdc++.h>

#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define each(it,n) for(__typeof((n).begin()) it=(n).begin();it!=(n).end();++it)

using namespace std;

int dr[4] = {1, 0, -1, 0}, dc[4] = {0, 1, 0, -1};
// down right up left

const double eps = 1e-9;

void solve() {
    int N;
    long double V, X;
    cin >> N >> V >> X;
    vector<pair<long double, long double> > high, low; // {C, R}
    long double rate = 0;
    rep(i, N) {
        long double C, R;
        cin >> R >> C;
        if (X == C) {
            rate += R;
        } else if (C > X) {
            high.push_back({C - X, R});
        } else {
            low.push_back({C - X, R});
        }
    }

    sort(high.begin(), high.end());
    sort(low.begin(), low.end());
    reverse(low.begin(), low.end());

    if (rate < eps && (high.size() == 0 || low.size() == 0)) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }    

    int hit = 0, lit = 0;

    while (hit < (int)high.size() && lit < (int)low.size()) {
        long double hc = high[hit].first, hr = high[hit].second;
        long double lc = low[lit].first,  lr = low[lit].second;

        cerr << hc << " " << hr << " " << lc << " " << lr << endl;

        if (abs(hc * hr / lc * lr + 1.0) < eps) {
            rate += hr + lr;
            hit++;
            lit++;
            } else if (hc * hr + lc * lr > 0) {
            long double dhr = - lc * lr / hc;
            rate += dhr + lr;
            high[hit].second -= dhr;
            lit++;
        } else {
            long double dlr = - hc * hr / lc;
            rate += hr + dlr;
            low[lit].second -= dlr;
            hit++;
        }
    }

    cout << setprecision(15) << V / rate << endl;
}

int main() {
    int T;
    cin >> T;
    rep(i, T) {
        cout << "Case #" << i + 1 << ": "; 
        solve();
    }
    return 0;
}
