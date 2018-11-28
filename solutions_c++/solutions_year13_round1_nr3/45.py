//Written by technolt~h

#pragma comment(linker, "/STACK:16777216")
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
 #include <stack>
#include <set>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <memory.h>
#include <sstream>
 #include <complex>

#define REP(i,n) for(int i = 0, _n = (n); i < _n; i++)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)
#define FOR(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define FORD(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
 #define FORN(i,a,b) for(int i=a;i<b;i++)
#define FOREACH(it,c) for (__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define RESET(c,x) memset (c, x, sizeof (c))

#define sqr(x) ((x) * (x))
#define PB push_back
 #define MP make_pair
#define F first
#define S second
#define Aint(c) (c).begin(), (c).end()
#define SIZE(c) (c).size()

#define DEBUG(x) { cerr << #x << " = " << x << endl; }
#define PR(a,n) {cerr<<#a<<" = "; FOR(_,1,n) cerr << a[_] << ' '; cerr <<endl;}
#define PR0(a,n) {cerr<<#a<<" = ";REP(_,n) cerr << a[_] << ' '; cerr << endl;}
#define LL long long
#define PI acos(-1.0)

using namespace std;

#define maxn 10011

int R, N, M, K, P[100];
bool ok[9 * 9 * 9 + 10];
bool check(int x, int y, int z) {
    RESET (ok, false);
    ok[1] = true;
    ok[x] = ok[y] = ok[z] = true;
    ok[x *y ] = ok[y * z ] = ok[z * x] = true;
    ok[x * y * z] = true;

    FOR (i, 1, K)
        if (!ok[P[i]]) return false;

    return true;
}

int main() {
    freopen("C-small-1-attempt0.in", "r", stdin);
    //freopen("a.in", "r", stdin);
    freopen("c.out", "w", stdout);

    int ntest;
    cin >> ntest;
    cout << "Case #1:"<< endl;
    cin >> R >> N >> M >> K;
    FOR (i, 1, R) {
        FOR (i, 1, K) cin >> P[i];
        int a, b, c;
        a = b = c = 2;
        FOR (x, 2, M)
            FOR (y, 2, M)
                FOR (z, 2, M)
                    if (check(x, y, z)) {
                        a = x;
                        b = y;
                        c = z;
                    }
        cout << a << b << c << endl;
    }
    return 0;
}



