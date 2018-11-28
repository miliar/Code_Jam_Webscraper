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
#define maxn 105
#define maxx 10000000

int ki[1000], kj[1000];
char a[maxn][maxn];
int m, n;


int check(int i, int j) {
    if (a[i][j] == '.') return 0;

    int k = 0;
    FOR(z, 1, m) k += a[z][j] != '.';
    FOR(z, 1, n) k += a[i][z] != '.';
    if (k == 2) return -100000;

    int ii = i, jj = j;
    k = 0;
    while (ii > 0 && ii <= m && jj > 0 && jj <= n) {
        k += a[ii][jj] != '.';
        ii += ki[a[i][j]];
        jj += kj[a[i][j]];
    }

    return k == 1 ? 1 : 0;
}

int main() {
    ios_base::sync_with_stdio(0);
    freopen("a_large.inp", "r", stdin);
    freopen("test.out", "w", stdout);


    ki['<'] = 0; kj['<'] = -1;
    ki['>'] = 0; kj['>'] = 1;
    ki['v'] = 1; kj['v'] = 0;
    ki['^'] = -1; kj['^'] = 0;
    
    int test;
    cin >> test;   

    FOR(t, 1, test) {
        cin >> m >> n;
        FOR(i, 1, m) FOR(j, 1, n) cin >> a[i][j];

        int res = 0;
        FOR(i, 1, m) FOR(j, 1, n) {
            res += check(i, j);
        }
        if (res < 0) {
            cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;    
        } else {
            cout << "Case #" << t << ": " << res << endl;
        }
        
    }
    return 0;
}