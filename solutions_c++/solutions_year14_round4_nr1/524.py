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

#define mp make_pair
#define pb push_back
#define fi first
#define se second

#define INF (1000000000)
#define LINF (1000000000000000000ll)
#define EPS (1e-9)

#define MOD 1000000007

#define NAME "test-large"
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
    assert(freopen(NAME ".out", "w", stdout));
#endif
    cout.setf(ios::fixed);
    cout.precision(20);
    cerr.setf(ios::fixed);
    cerr.precision(3);
    int n = 1;
    cin >> n;
    for (int i = 0; i < n; ++i)
        solve(i + 1);
}

int n, w;
multiset<int> q;
int sz;

void solve(int test_number) {
    q.clear();
    cin >> n >> w;
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        q.insert(a);
    }
    int res = 0;
    while (!q.empty()) {
        auto it = q.end();
        it--;
        int bg = *it;
        q.erase(it);
        res++;
        if (q.empty())
            break;
        int rem = w - bg;
        auto p = q.upper_bound(rem);
        if (p != q.begin()) {
            p--;
            q.erase(p);
        }
    }
    cout << "Case #" << test_number << ": " << res << endl;
}

