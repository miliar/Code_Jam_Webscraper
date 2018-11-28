#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;
#define PB push_back
#define MP make_pair
#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

int t, n;
long long x[40], B;
double ans;

long long amount(long long mid) {
    long long res = (37 - n) * mid;
    for (int i = 0; i < n; ++i)
        if (x[i] < mid)
            res += mid - x[i];
    return res;
}

double get(long long mid) {
    // cout << mid << endl;
    long long aa = amount(mid);
    double ans = 0.0;
    for (int k = -1; k < n; ++k) {
        long long a = aa;
        int cnt = 37 - n;
        for (int i = 0; i < n; ++i) {
            if (x[i] <= mid) {
                if (i > k)
                    ++a;
                else
                    ++cnt;
            }
        }
        if (a > B)
            continue;
        double res = mid * 36.0 * (37 - n) / cnt;
        for (int i = 0; i < n; ++i)
            if (x[i] < mid && i <= k)
                res += (mid - x[i]) * 36.0 / cnt;
        ans = max(ans, res - a);
    }
    return ans;
}

void check(long long lb, long long ub) {
    long long tb = lb - 1;
    while (tb != ub) {
        long long mid = (tb + ub + 1) / 2;
        if (amount(mid) > B)
            ub = mid - 1;
        else
            tb = mid;
    }
    if (amount(ub) > B)
        return;
    // while (lb != ub) {
        // long long mid1 = (lb * 2 + ub) / 3, mid2 = (lb + ub * 2) / 3;
        // if (get(mid1) < get(mid2))
    // }
    ans = max(ans, max(get(lb), get(ub)));
    ans = max(ans, max(get(lb - 1), get(ub - 1)));
    ans = max(ans, max(get(lb + 1), get(ub + 1)));
    // for (long long i = lb; i <= ub; ++i)
        // ans = max(ans, get(i));
    // cout << lb << ' ' << get(lb) << ' ' << amount(lb) << endl;
    // cout << ans << endl;
}

void solve() {
    cin >> B >> n;
    for (int i = 0; i < n; ++i)
        cin >> x[i];
    sort(x, x + n);
    long long last = 1;
    ans = 0.0;
    for (int i = 0; i < n; ++i) {
        check(last, x[i]);
        last = x[i];
    }
    check(last, 1000000000000LL);
    printf("Case #%d: ", ++t);
    printf("%.9lf\n", ans);
}

int main() {
    freopen("A.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}
