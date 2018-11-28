/******************************************************************************\
*                         Author:  Dumbear                                     *
*                         Email:   dumbear[#at]163.com                         *
*                         Website: http://dumbear.com                          *
\******************************************************************************/
#include <algorithm>
#include <bitset>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <typeinfo>
#include <utility>
#include <vector>

using namespace std;

#define output(x) cout << #x << ": " << (x) << endl;

typedef long long LL;
typedef vector<int> VI;
typedef vector<long long> VL;
typedef vector<long double> VD;
typedef vector<string> VS;

const long double eps = 1e-8;

int sgn(long double d) {
    return d > eps ? 1 : (d < -eps ? -1 : 0);
}

int t, n;
long double V, X, res[128];
pair<long double, long double> w[128];
long double sum_r, sum_rc;

void total() {
    sum_rc = 0.0;
    sum_r = 0.0;
    for (int i = 0; i < n; ++i) {
        sum_rc += res[i] * w[i].first;
        sum_r += res[i];
    }
}

bool calc1() {
    sort(w, w + n, greater<pair<long double, long double> >());
    for (int i = 0; i < n; ++i)
        res[i] = w[i].second;
    if (w[n - 1].first >= X) {
        for (int i = 0; i < n; ++i) {
            if (w[i].first > X) {
                res[i] = 0.0;
                break;
            }
        }
    }
    total();
    for (int i = 0; i < n && sgn(sum_rc - sum_r * X) > 0; ++i) {
        if (X - w[i].first >= 0)
            return false;
        if (res[i] == 0.0)
            continue;
        long double tmp = ((sum_rc - res[i] * w[i].first) - (sum_r - res[i]) * X) / (X - w[i].first);
        // output(tmp);
        // output(res[i]);
        while (sgn(tmp - res[i]) >= 0);
        tmp = min(tmp, res[i]);
        if (tmp < 0.0) tmp = 0.0;
        res[i] = tmp;
        total();
    }
    while (sgn(sum_rc - sum_r * X) != 0);
    return true;
}

bool calc2() {
    sort(w, w + n);
    for (int i = 0; i < n; ++i)
        res[i] = w[i].second;
    if (w[n - 1].first <= X) {
        for (int i = 0; i < n; ++i) {
            if (w[i].first < X) {
                res[i] = 0.0;
                break;
            }
        }
    }
    total();
    for (int i = 0; i < n && sgn(sum_rc - sum_r * X) < 0; ++i) {
        if (X - w[i].first <= 0)
            return false;
        if (res[i] == 0.0)
            continue;
        long double tmp = ((sum_rc - res[i] * w[i].first) - (sum_r - res[i]) * X) / (X - w[i].first);
        // output(tmp);
        // output(res[i]);
        while (sgn(tmp - res[i]) >= 0);
        tmp = min(tmp, res[i]);
        if (tmp < 0.0) tmp = 0.0;
        res[i] = tmp;
        total();
    }
    while (sgn(sum_rc - sum_r * X) != 0);
    return true;
}

void solve() {
    scanf("%d", &n);
    double a, b;
    scanf("%lf%lf", &a, &b);
    V = a;
    X = b;
    bool f1 = true, f2 = true;
    for (int i = 0; i < n; ++i) {
        scanf("%lf%lf", &a, &b);
        w[i].second = a;
        w[i].first = b;
        if (w[i].first >= X) f1 = false;
        if (w[i].first <= X) f2 = false;
        res[i] = w[i].second;
    }
    total();
    printf("Case #%d: ", ++t);
    // printf("-- %lf %lf %lf\n", sum_rc, sum_r, X);
    // output(X);
    if (f1 || f2) {
        puts("IMPOSSIBLE");
    } else if (sgn(sum_rc - sum_r * X) >= 0) {
        // puts("op");
        if (!calc1()) {
            puts("IMPOSSIBLE");
        } else {
            printf("%.12f\n", (double)(V / sum_r));
        }
    } else {
        if (!calc2()) {
            puts("IMPOSSIBLE");
        } else {
            printf("%.12f\n", (double)(V / sum_r));
        }
    }
}

int main() {
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}
