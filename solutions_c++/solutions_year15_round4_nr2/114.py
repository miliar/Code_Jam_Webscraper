#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <set>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <map>
#include <queue>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef vector<pii> vii;
typedef vector<string> vs;

int main() {
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        printf("Case #%d: ", test);
        int n;
        double v,x;
        scanf("%d%lf%lf", &n, &v, &x);
        vd r(n), t(n);
        vi v1, v2;
        double r0 = 0, r1 = 0, r2 = 0, a1 = 0, a2 = 0;
        for (int i = 0; i < n; ++i) {
            scanf("%lf%lf",&r[i],&t[i]);
            if (t[i] < x) {
                v1.push_back(i);
                r1 += r[i];
                a1 += r[i]*t[i];
            } else if (t[i] > x) {
                v2.push_back(i);
                r2 += r[i];
                a2 += r[i]*t[i];
            } else if (t[i] == x) r0 += r[i];
        }
        if (v1.empty() || v2.empty()) {
            if (r0 == 0) {
                cout << "IMPOSSIBLE\n";
            } else {
                printf("%.8lf\n", v / r0);
            }
            continue;
        }
        a1 /= r1;
        a2 /= r2;
        double c1 = (x - a2) / (a1 - a2);
        double c2 = (x - a1) / (a2 - a1);
        double c = c1 * r2 / c2 / r1;
        double L = 0, R = 1e10;
        while (R - L > 1e-7) {
            double m = (L + R) / 2;
            double rem = v - r0*m;
            double x1 = m, x2 = m;
            if (c < 1) {
                x1 = c * x2;
            } else {
                x2 = x1 / c;
            }
            rem -= r1*x1 + r2*x2;
            if (rem < 0) {
                R = m;
            } else L = m;
        }
        printf("%.8lf\n", (L + R) / 2);
    }
    return 0;
}
