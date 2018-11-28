#include <bits/stdc++.h>
using namespace std;

typedef long long li;
#define rep(i, n) for (int i = 0; i < (int)(n); ++i)

struct problem {
    // input fields.
    int n;
    double v, x;
    vector<pair<double, double> > crs;
    double ans;

    // parse here.
    problem () {
        cin >> n >> v >> x;
        rep(i, n) {
            double r, c;
            cin >> r >> c;
            crs.push_back(make_pair(c, r));
        }
        sort(crs.begin(), crs.end());
    }

    // called exactly once. set ans here.
    void solve () {
        if (n == 1) {
            if (x == crs[0].first) {
                ans = v / crs[0].second;
            } else {
                ans = -1;
            }
        } else {
            if (x < crs[0].first || crs[1].first < x) {
                //cerr << crs[0].first << " " << x << " " << crs[1].first << endl;
                ans = -1;
            } else {
                if (crs[0].first == crs[1].first) {
                    ans = v / (crs[0].second + crs[1].second);
                } else {
                    const double r0 = crs[0].second;
                    const double r1 = crs[1].second;
                    const double c0 = crs[0].first;
                    const double c1 = crs[1].first;
                    const double delta = (r0 * r1 * (c1 - c0));
                    const double t0 = ( r1 * c1 * v - r1 * v * x) / delta;
                    const double t1 = (-r0 * c0 * v + r0 * v * x) / delta;
                    //cerr << t0 << " " << t1 << endl;
                    ans = max(t0, t1);
                }
            }
        }
    }
};

// generally you don't have to modify below.
int main () {
    int t;
    cin >> t;
    vector<problem> inputs;
    rep (i, t) {
        inputs.push_back(problem());
    }
    #pragma omp parallel for
    rep (i, t) {
        inputs[i].solve();
    }

    cout.precision(12);
    rep (i, t) {
        cout << "Case #" << i + 1 << ": ";
        if (inputs[i].ans < 0) {
            cout << "IMPOSSIBLE" << endl;;
        } else {
            cout << fixed << inputs[i].ans << endl;;
        }
    }
    return 0;
}
