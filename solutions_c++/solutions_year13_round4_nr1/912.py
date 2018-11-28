#include <iostream>
#include <stdio.h>
#include <string>
#include <string.h>
#include <math.h>
#include <vector>
#include <stdlib.h>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <cassert>
#include <ctime>
#include <queue>
#include <deque>
#include <memory.h>
#include <complex>
#include <numeric>

#ifdef _GEANY
    #include "/home/pershik/debug_lib/debug.h"
#endif

#define mp make_pair
#define pb push_back
#define fi first
#define se second

#define INF (1000000000)
#define LINF (1000000000000000000ll)
#define EPS (1e-9)

#define MOD 1000002013LL

#define NAME "a_small"
//#define NAME "a"
#ifndef NAME
    #error Write problem name!
#endif

using namespace std;

typedef long long li;
typedef unsigned long long uli;

li gcd(li x, li y){
    if (y == 0)
        return x;
    else
        return gcd(y, x % y);
}

li lcm(li x, li y){
    return x / gcd(x, y) * y;
}

li binpow(li a, li p){
    if (!p)
        return 1;
    li g = binpow(a, p >> 1);
    if (p % 2 == 0)
        return (g * g) % MOD;
    else
        return (((g * g) % MOD) * a) % MOD;
}

li rev(li n){
    return binpow(n, (li)MOD - 2LL);
}

void solve(int test_number);

int main() {
#ifdef _GEANY
    assert(freopen(NAME ".in", "r", stdin));
#endif
    freopen(NAME ".out", "w", stdout);
    cout.setf(ios::fixed);
    cout.precision(20);
    cerr.setf(ios::fixed);
    cerr.precision(3);
    int n = 1;
    cin >> n;
    for (int i = 0; i < n; ++i)
        solve(i + 1);
}

li n, m;
pair<pair<li, li>, li> a[100100];

inline li cost(li st, li f){
    li len = f - st;
    return (m * len - len * (len - 1LL) / 2LL) % MOD;
}

void solve(int test_number) {
    cin >> m >> n;
    //cerr << cost(1, m) << ' ' << m << endl;
    int i;
    int cnt = 0;
    int c, d, e;
    for (i = 0; i < n; i++){
        cin >> c >> d >> e;
        for (int j = 0; j < e; j++){
            a[cnt].fi.fi = c, a[cnt].fi.se = d;
            cnt++;
        }
    }
    n = cnt;
    li full = 0;
    for (i = 0; i < n; i++)
        full = (full + cost(a[i].fi.fi, a[i].fi.se) % MOD) 
            % MOD;
    int j;
    li res = 0;
    sort(a, a + n);
    for (i = 0; i < n; i++){
        for (j = i + 1; j < n; j++)
            if (a[j].fi.se > a[i].fi.se && a[j].fi.fi <= a[i].fi.se )
                swap(a[j].fi.se, a[i].fi.se);
        res = (res + cost(a[i].fi.fi, a[i].fi.se)) % MOD;
    }
    li ans = (full - res + MOD) % MOD;
    cout << "Case #" << test_number << ": " << ans << endl;
}

