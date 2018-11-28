//#include <bits/stdc++.h>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
using namespace std;
#define FOR(i, a, b) for(int i = a; i <= b; i ++)
#define DOW(i, a, b) for(int i = a; i >= b; i --)
#define RESET(c, val) memset(c, val, sizeof(c))
#define oo 1e9
#define eps 1e-9
#define base 1000000007
#define maxn 1005
#define maxx 10000000

int n, a[maxn];

int main() {
    ios_base::sync_with_stdio(0);
    freopen("B_large.inp", "r", stdin);
    freopen("B_large.out", "w", stdout);

    int test;
    cin >> test;

    FOR(t, 1, test) {
        cin >> n;
        FOR(i, 1, n) cin >> a[i];

        int res = 1000000000;
        FOR(i, 1, 1000) {
            int rr = i;
            FOR(j, 1, n) if (a[j] > i) {
                rr += (a[j] - i) / i + ((a[j] - i) % i != 0);
            } 
            res = min(res, rr);
        }

        cout << "Case #" << t << ": " << res << endl;
    }
    return 0;
}