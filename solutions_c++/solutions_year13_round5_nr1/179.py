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

#define PROBLEM_NAME "A-small-attempt0"
//#define PROBLEM_NAME "my"

int n;
int S;
int d[37];
int my[37];

void solveCase(int tc) {
    _fill(d, 0);
    _fill(my, 0);
    scanf("%d %d", &S, &n);
    rep(i, n) scanf("%d", d+i);
    sort(d, d+37);
    double ret = 0;
    for (int v = 1; v <= 2000; v++) {
        int spent = 0;
        int totMy = 0;
        int k = 0;
        while (k < 37 && d[k] <= v) {
            my[k] = v-d[k];
            spent += my[k];
            totMy += my[k];
            k++;
        }
        for (int i = k-1; i > 0; i--) {
            if (spent > S) break;
            double cur = (1./(i+1)) * totMy * 36 - spent;
            DEB(i);
            DEB(cur);
            cerr << "---" << endl;
            ret = max(ret, cur);
            totMy -= my[i];
            spent++;
        }
    }
    printf("Case #%d: %.10lf\n", tc+1, ret);
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
