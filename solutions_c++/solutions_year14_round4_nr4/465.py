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

#define NAME "test"
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

struct node {
    int next[26];
};

node t[10010];
int sz = 1;

void initNode(int pos) {
    memset(t[pos].next, 255, sizeof(t[pos].next));
}

void addString(string s) {
    int cur = 0;
    for (int i = 0; i < (int)s.length(); i++) {
        int c = s[i] - 'A';
        if (t[cur].next[c] != -1) {
            cur = t[cur].next[c];
        } else {
            initNode(sz);
            t[cur].next[c] = sz;
            cur = sz;
            sz++;
        }
    }
}

int n, m;
string s[100];
int res = 0, bg = -1;
int a[100];

void rec(int p) {
    if (p == n) {
        int cur = 0;
        for (int i = 0; i < m; i++) {
            initNode(0);
            sz = 1;
            bool flag = false;
            for (int j = 0; j < n; j++)
                if (a[j] == i)
                    addString(s[j]), flag = true;
            if (flag)
                cur += sz;
        }
        if (cur > bg) {
            bg = cur;
            res = 0;
        }
        if (cur == bg)
            res++;
    } else {
        for (int i = 0; i < m; i++) {
            a[p] = i;
            rec(p + 1);
        }
    }
}

void solve(int test_number) {
    cin >> n >> m;
    res = 0, bg = -1;
    for (int i = 0; i < n; i++)
        cin >> s[i];
    rec(0);
    cout << "Case #" << test_number << ": " << bg << ' ' << res << endl;
}

