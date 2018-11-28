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

int main() {
    ios_base::sync_with_stdio(0);
    freopen("D_small.inp", "r", stdin);
    freopen("D_small.out", "w", stdout);

    int test;
    cin >> test;

    FOR(t, 1, test) {
        int x, r, c;
        cin >> x >> r >> c;

        string res;
        if (x >= 4) {
            res = (r + c >= 7) ? "GABRIEL" : "RICHARD";
        } else if (x == 1) {
            res = "GABRIEL";
        } else if (x == 2) {
            res =(r % 2 == 1 && c % 2 == 1) ? "RICHARD": "GABRIEL";
        } else {
            res = ((r*c) % 3 == 0 && r*c > 3) ? "GABRIEL": "RICHARD";
        }
        cout << "Case #" << t << ": " << res << endl;
    }
    return 0;
}