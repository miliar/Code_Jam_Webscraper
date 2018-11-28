#include <cstdio>
#include <iostream>
#include <fstream>
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
#include <cassert>

#define REP(i,n) for(int i = 0, _n = (n); i < _n; i++)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)
#define FOR(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define FORD(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define FORN(i,a,b) for(int i=a;i<b;i++)
#define FOREACH(it,c) for (__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define RESET(c,x) memset (c, x, sizeof (c))

#define PI acos(-1)
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

using namespace std;

int n, k;

int cmp(double x, double y) {
    if (abs(x - y) <= 1e-6) return 0;
    if (x < y) return -1;
    return 1;
}

int main() {
    freopen("B-large.in", "rb", stdin); freopen("a.out", "wb", stdout);
    int ntest;
    cin >> ntest;
    for (int test = 1; test <= ntest; test++) {
        printf("Case #%d: ", test);
        double C, F, X;

        scanf("%lf%lf%lf", &C, &F, &X);

        double speed = 2, time = 0, res = X/2.0;

        while (cmp(time, res) <= 0) {
            res = min(res, time + X / speed);
            time = time + C / speed;
            speed += F;
        }

        printf("%.9lf", res);
        if (test < ntest) printf("\n");
    }

    return 0;
}
