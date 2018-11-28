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

int t, n, dp[1 << 15][16][16], p[16];

int get(int s, int k, int m) {
    if (dp[s][k][m] != -1)
        return dp[s][k][m];
    int &res = dp[s][k][m];
    int cnt = 0;
    for (int i = 0; i < 15; ++i)
        if (((s >> i) & 1) == 1)
            ++cnt;
    cnt += m;
    if (k == n)
        return res = cnt;
    res = INT_MAX;
    if (p[k] == 0) {
        for (int i = 0; i < 15; ++i) {
            if (((s >> i) & 1) == 0)
                res = min(res, get(s ^ (1 << i), k + 1, m));
        }
        res = min(res, get(s, k + 1, m + 1));
    } else if ((~p[k]) == 0) {
        for (int i = 0; i < 15; ++i) {
            if (((s >> i) & 1) == 1)
                res = min(res, get(s ^ (1 << i), k + 1, m));
        }
        res = min(res, get(s, k + 1, m == 0 ? 0 : m - 1));
    } else if (p[k] > 0) {
        if (((s >> p[k]) & 1) == 0)
            res = min(res, get(s ^ (1 << p[k]), k + 1, m));
    } else {
        if (((s >> ~p[k]) & 1) == 1)
            res = min(res, get(s ^ (1 << ~p[k]), k + 1, m));
    }
    return res;
}

void solve() {
    scanf("%d", &n);
    vector<int> v;
    for (int i = 0; i < n; ++i) {
        char buf[8];
        scanf("%s%d", buf, &p[i]);
        v.push_back(p[i]);
        if (buf[0] == 'L')
            p[i] = ~p[i];
    }
    sort(v.begin(), v.end());
    v.push_back(0);
    v.resize(unique(v.begin(), v.end()) - v.begin());
    for (int i = 0; i < n; ++i) {
        if (p[i] >= 0)
            p[i] = lower_bound(v.begin(), v.end(), p[i]) - v.begin();
        else
            p[i] = ~(int)(lower_bound(v.begin(), v.end(), ~p[i]) - v.begin());
        // printf("-- %d\n", p[i]);
    }
    printf("Case #%d: ", ++t);
    int ans = INT_MAX;
    memset(dp, -1, sizeof(dp));
    for (int i = 0; i < (1 << 15); ++i) {
        ans = min(ans, get(i, 0, 0));
    }
    if (ans == INT_MAX)
        puts("CRIME TIME");
    else
        printf("%d\n", ans);
}

int main() {
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}
