#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <fstream>
#include <math.h>
#include <limits>
#include <set>
#include <map>
#include <sstream>
#include <stdio.h>
#include <time.h>
#include <memory.h>
#include <cassert>
#include <complex>
using namespace std;

///////////////// macros and typedefs ////////////////////
#define DEB(k) cerr << "debug: " #k << "=" << k << endl;
#define rep(i, n) for (int i = 0, _n = (n); i < _n; ++i)
#define repd(i, n) for (int i = (n)-1; i >= 0; --i)
#define _fill(a, x) memset((a), (x), sizeof((a)))
#define all(c) (c).begin(), (c).end()
#define mp(a, b) make_pair(a, b)
#define l(c) (int)((c).size())
#define sqr(a) ((a)*(a))
#define inf 0x7f7f7f7f
#define pb push_back
#define ppb pop_back
#define x first
#define y second
typedef long long ll;
typedef vector<int> vi;
typedef vector<double> vd;
typedef pair<int, int> pi;

#define PROBLEM_NAME "B-large"

int n;
ll p;
ll N;

void solveCase(int tc) {
    cin >> n >> p;
    ll X, Y;
    N = 1LL<<n;
    //DEB(N);
    ll p2 = 1;
    ll mask = N-1;
    rep(i, n+1) {
        ll idx = N-p2;
        //DEB(idx);
        if (mask < p) {
            Y = idx;
            break;
        }
        mask >>= 1;
        p2 <<= 1;
    }
    p2 = 1;
    mask = 0;
    ll add = 1LL<<(n-1);
    rep(i, n+1) {
        ll idxNext = min(N-1, (p2*2)-2);
        //DEB(idxNext);
        //DEB(mask);
        if (mask < p)
            X = idxNext;
        mask |= add;
        add >>= 1;
        p2 *= 2;
    }
    cout << "Case #" << (tc+1) << ": " << X << " " << Y << endl;
}

void solution()
{
    int tc;
    scanf("%d\n", &tc);
    rep(i, tc)
        solveCase(i);
}

int main()
{
#ifndef ONLINE_JUDGE
   freopen(PROBLEM_NAME".in", "rt", stdin);
   freopen(PROBLEM_NAME".out", "wt", stdout);
#endif
   solution();
#ifndef ONLINE_JUDGE
   //fprintf(stderr, "Time: %.2lf sec\n", (clock()*1./CLOCKS_PER_SEC));
#endif
   return 0;
}
