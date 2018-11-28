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
typedef vector<double> VD;
typedef vector<string> VS;

int t;

int n, p, q, r, s;
LL cnt[1000010], sum[1000010];

bool check(LL mid) {
    LL ss = 0;
    int i;
    for (i = 0; i < n; ++i) {
        if (ss + cnt[i] > mid)
            break;
        ss += cnt[i];
    }
    if (i == n)
        return true;
    ss = 0;
    for (; i < n; ++i) {
        if (ss + cnt[i] > mid)
            break;
        ss += cnt[i];
    }
    if (i == n)
        return true;
    ss = 0;
    for (; i < n; ++i) {
        if (ss + cnt[i] > mid)
            break;
        ss += cnt[i];
    }
    return i == n;
}

void solve() {
    scanf("%d%d%d%d%d", &n, &p, &q, &r, &s);
    for (int i = 0; i < n; ++i) {
        cnt[i] = ((LL)i * p + q) % r + s;
        sum[i] = (i == 0 ? 0 : sum[i - 1]) + cnt[i];
    }
    LL lb = 0, ub = sum[n - 1];
    while (lb != ub) {
        LL mid = (lb + ub) / 2;
        if (check(mid)) {
            ub = mid;
        } else {
            lb = mid + 1;
        }
    }
    printf("Case #%d: ", ++t);
    printf("%.18f\n", (double)(sum[n - 1] - lb) / sum[n - 1]);
}

int main() {
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}
