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
#define maxn 100005
#define maxx 10000000

int main() {
    ios_base::sync_with_stdio(0);
    freopen("A_large.inp", "r", stdin);
    freopen("A_large.out", "w", stdout);

    int test;
    cin >> test;

    FOR(t, 1, test) {
        int n;
        cin >> n;

        int sum = 0, res = 0;
        FOR(i, 0, n) {
            char ch;
            cin >> ch;

            res = max(res, i - sum);
            sum += ch - '0';
        }

        cout << "Case #" << t << ": " << res << endl;
    }
    return 0;
}