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

struct binary_indexed_tree {
    int n, sum[1024];
    void clear(int size) {
        n = size;
        fill(sum + 1, sum + 1 + n, 0);
    }
    void add(int pos, int val) {
        for (; pos <= n; pos += pos & -pos)
            sum[pos] += val;
    }
    int get_sum(int pos) const {
        int res = 0;
        for (; pos > 0; pos -= pos & -pos)
            res += sum[pos];
        return res;
    }
    int get_sum(int first, int last) const {
        // printf("!! %d %d\n", first, last);
        return get_sum(last) - get_sum(first - 1);
    }
};

binary_indexed_tree bit_l, bit_r;

int t, n, x[1024], lval[1024], rval[1024];

void solve() {
    scanf("%d", &n);
    int pos = 0;
    for (int i = 0; i < n; ++i) {
        scanf("%d", &x[i]);
        if (x[i] > x[pos])
            pos = i;
    }
    vector<int> v(x, x + n);
    sort(v.begin(), v.end());
    for (int i = 0; i < n; ++i)
        x[i] = lower_bound(v.begin(), v.end(), x[i]) - v.begin() + 1;
    bit_l.clear(n);
    bit_r.clear(n);
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        lval[i] = bit_l.get_sum(x[i]);
        rval[n - 1 - i] = bit_r.get_sum(x[n - 1 - i]);
        bit_l.add(x[i], 1);
        bit_r.add(x[n - 1 - i], 1);
    }
    for (int i = 0; i < n; ++i)
        ans += min(i - lval[i], n - 1 - i - rval[i]);
    // map<int, int> pp;
    // for (int i = 0; i < n - 1; ++i)
    //     pp[v[i]] = i;
    // int ans = INT_MAX;
    // for (int i = 0; i < n; ++i) {
    //     int res = abs(pos - i);
    //     bit.clear(n + 1);
    //     for (int j = 0; j < n - 1; ++j) {
    //         bit.add(j + 1, 1);
    //     }
    //     set<int> ss(v.begin(), v.end());
    //     for (int j = 1; j < n; ++j) {
    //         int k = *ss.rbegin();
    //         // printf("-- %d %d\n", k, pp[k]);
    //         bit.add(pp[k] + 1, -1);
    //         if (pp[k] < i) {
    //             res += bit.get_sum(pp[k] + 1, i);
    //         } else {
    //             res += bit.get_sum(i + 1, pp[k] + 1);
    //         }
    //         ss.erase(k);
    //     }
    //     ans = min(ans, res);
    // }
    printf("Case #%d: %d\n", ++t, ans);
}

int main() {
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}
