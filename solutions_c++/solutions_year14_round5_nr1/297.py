/**
 * Copyright (c) 2014 Authors. All rights reserved.
 * 
 * FileName: A.cpp
 * Author: Beiyu Li <sysulby@gmail.com>
 * Date: 2014-06-14
 */
#include <bits/stdc++.h>

using namespace std;

#define REP(i,n) for (int i = 0; i < (n); ++i)
#define FOR(i,s,t) for (int i = (s); i <= (t); ++i)
#define FOREACH(i,c) for (__typeof(c.begin()) i = c.begin(); i != c.end(); ++i)

typedef long long LL;
typedef pair<int, int> Pii;

const int inf = 0x3f3f3f3f;
const LL infLL = 0x3f3f3f3f3f3f3f3fLL;

const int maxn = 1000000 + 5;

int n, p, q, r, s;
int a[maxn];
LL pre[maxn];

int main()
{
        int T, cas = 0;
        cin >> T;

        while (T--) {
                cin >> n >> p >> q >> r >> s;
                REP(i,n) {
                        a[i] = ((LL)i * p + q) % r + s;
                        pre[i] = a[i] + (i > 0? pre[i-1]: 0);
                }
                LL res = 0;
                REP(i,n) {
                        int p = upper_bound(pre, pre + i, pre[i] / 2) - pre;
                        if (p == 0) {
                                res = max(res, pre[n-1] -
                                                max(pre[i], pre[n-1] - pre[i]));
                        } else {
                                res = max(res, pre[n-1] -
                                                max(max(pre[p-1], pre[i]
                                                                - pre[p-1]),
                                                        pre[n-1] - pre[i]));
                        }
                        p = lower_bound(pre, pre + i, (pre[i] + 1) / 2) - pre;
                        if (p == i) {
                                res = max(res, pre[n-1] -
                                                max(pre[i], pre[n-1] - pre[i]));
                        } else {
                                res = max(res, pre[n-1] -
                                                max(max(pre[p], pre[i]
                                                                - pre[p+1]),
                                                        pre[n-1] - pre[i]));
                        }
                }
                cout << "Case #" << ++cas << ": ";
                cout << fixed << setprecision(10) <<
                        (double)res / pre[n-1] << endl;
        }

        return 0;
}
