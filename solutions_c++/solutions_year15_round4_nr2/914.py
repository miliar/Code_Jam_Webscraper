#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

#define double long double
typedef pair<double, double> PP;
typedef long long LL;
#define pb push_back
#define fr first
#define sc second

int n;
double r[200], c[200], V, C;


double vmin(double t) {
    double res = 0.0;
    double rem = V;
    for (int i = 0; i < n; i ++) {
        double cur = min(r[i] * t,  rem);
        res += cur * c[i];
        if (rem < r[i] * t) break;
        rem -= cur;
    }
    return res;
}
double vmax(double t) {
    double res = 0.0;
    double rem = V;
    for (int i = n - 1; i >= 0; i --) {
        double cur = min(r[i] * t,  rem);
        res += cur * c[i];
        if (rem < r[i] * t) break;
        rem -= cur;
    }
    return res;
}

void solve() {
    cin >> n >> V >> C;
    for (int i = 0; i < n; i ++) cin >> r[i] >> c[i];
    vector<PP> v;
    for (int i = 0; i < n; i ++) v.pb(PP(c[i], r[i]));
    sort(v.begin(), v.end());
    for (int i = 0; i < n; i ++) r[i] = v[i].sc, c[i] = v[i].fr;
    double sr = 0;
    for (int i = 0; i < n; i ++) sr += r[i];
    double lmin = 100000, lmax = 0;
    for (int i = 0; i < n; i ++) 
        lmin = min(lmin, c[i]), lmax = max(lmax, c[i]);
    if (lmin > C || C > lmax) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }
/*    if (n == 1) {
        cout << setprecision(9) << fixed << V / r[0] << endl;
    }
    else if (c[0] == c[1]) {
        cout << setprecision(9) << fixed << V / (r[0] + r[1]) << endl;
    }
    else if (c[0] == C) {
        cout << setprecision(9) << fixed << V / r[0] << endl;
    }
    else if (c[1] == C) {
        cout << setprecision(9) << fixed << V / r[1] << endl;
    }
    else {
        double a = V * (c[1] - C) / (c[1] - c[0]), b = V - a;
        cout << setprecision(9) << fixed << max(a / r[0], b / r[1]) << endl;
    }
    return;*/
    double lt = V / sr, rt = 1e9;
    while (rt - lt >= 1e-9) {
        double mid = (lt + rt) * 0.5;
        if (vmin(mid) - 1e-15 <=  V * C && V * C <= vmax(mid) + 1e-15) rt = mid;
        else lt = mid;
    }
    cout << setprecision(9) << fixed << (lt + rt) / 2 << endl;
}
int main() {
    #ifdef _TEST_
    freopen("input.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    #endif
    int Q;
    cin >> Q;
    for (int i = 0; i < Q; i ++) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }

    return 0;
}
