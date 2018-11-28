#include <iostream>
#include <cstring>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <bitset>
#define _USE_MATH_DEFINES
#include <math.h>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <assert.h>
#include <stdlib.h>
using namespace std;

void smain();
int main(){
#ifdef TASK
    //freopen(TASK".in","rt",stdin);
    freopen("/Users/ramis/Downloads/B-small-attempt0.in.txt","rt",stdin);
    freopen("out.txt","wt",stdout);
    const clock_t start = clock();
#endif
    smain();
#ifdef TASK
    cerr << "\nTotal Execution Time: " << float( clock () - start ) /  CLOCKS_PER_SEC << endl;
#endif
    return 0;
}

#ifndef M_PI
#define M_PI 3.14159265358979311599796346854418516
#endif
#define forn(i,n) for (int i=0;i<n;i++)
#define rforn(i,n) for (int i=n-1;i>=0;i--)
#define int long long
#define LL long long
#define mp(a,b) make_pair(a,b)
#define INF 2305843009213693951LL
#define MOD 1000000007
#define EPS 1E-9
#define N 201
/* --------- END TEMPLATE CODE --------- */

int n, k;
double p[N], d[N][N];

double calc(const vector<double> a) {
    forn(i, k + 1) forn(j, k + 1) d[i][j] = 0;
    d[0][0] = 1;
    forn(i, k) forn(j, i + 1) if (d[i][j] > EPS) {
        d[i + 1][j + 1] += d[i][j] * a[i];
        d[i + 1][j] += d[i][j] * (1 - a[i]);
    }
    return d[k][k/2];
}

double naive() {
    int mm = 1 << n;
    double res = 0;
    vector<double> a;
    forn(mask, mm) {
        if (__builtin_popcount(mask) != k) continue;
        a.clear();
        forn(i, n) if ((mask >> i) & 1) a.push_back(p[i]);
        res = max(res, calc(a));
    }
    return res;
}

void smain() {
    cin >> n;
    cout << fixed;
    cout.precision(9);
    cerr << fixed;
    cerr.precision(9);
    for (int cas = 1; cin >> n >> k; ++cas) {
        forn(i, n) cin >> p[i];
        double res = naive();
        cout << "Case #" << cas << ": " << res << endl;
        cerr << "Case #" << cas << ": " << res << endl;
    }
}
