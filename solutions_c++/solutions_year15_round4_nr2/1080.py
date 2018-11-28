/**
 * Copyright (c) 2015 Authors. All rights reserved.
 * 
 * FileName: B.cpp
 * Author: Beiyu Li <sysulby@gmail.com>
 * Date: 2015-05-30
 */
#include <bits/stdc++.h>

using namespace std;

#define rep(i,n) for (int i = 0; i < (n); ++i)
#define For(i,s,t) for (int i = (s); i <= (t); ++i)
#define foreach(i,c) for (__typeof(c.begin()) i = c.begin(); i != c.end(); ++i)

typedef long long LL;
typedef pair<int, int> Pii;

const int inf = 0x3f3f3f3f;
const LL infLL = 0x3f3f3f3f3f3f3f3fLL;

const int maxn = 100 + 5;
const long double eps = 1e-14;

int sgn(long double x) { return x < -eps? -1: x > eps; }

int n;
long double v, x;
struct Src {
        long double r, c;
        bool operator<(const Src &s) const { return c < s.c; }
} a[maxn];

bool check(long double t)
{
        long double nv = 0, nx = 0;
        rep(i,n) {
                if (nv + a[i].r * t < v) {
                        nv += a[i].r * t;
                        nx += a[i].r * t * a[i].c;
                } else {
                        nx += (v - nv) * a[i].c;
                        nv = v;
                        break;
                }
        }
        if (sgn(nv - v) < 0 || sgn(nx - x * v) > 0) return false;
        nv = nx = 0;
        for (int i = n - 1; i >= 0; --i) {
                if (nv + a[i].r * t < v) {
                        nv += a[i].r * t;
                        nx += a[i].r * t * a[i].c;
                } else {
                        nx += (v - nv) * a[i].c;
                        nv = v;
                        break;
                }
        }
        return sgn(nx - x * v) >= 0;
}

int main()
{
        int T, cas = 0;
        cin >> T;

        while (T--) {
                cin >> n >> v >> x;
                rep(i,n) cin >> a[i].r >> a[i].c;
                sort(a, a + n);
                cout << "Case #" << ++cas << ": ";
                if (sgn(a[0].c - x) > 0 || (a[n-1].c - x) < 0) {
                        cout << "IMPOSSIBLE" << endl;
                } else {
                        long double l = 0, r = 1e10L;
                        while (l - r < -1e-8) {
                                long double mid = (l + r) / 2;
                                if (check(mid)) r = mid;
                                else l = mid;
                        }
                        cout << fixed << setprecision(10) << r << endl;
                }
        }

        return 0;
}
