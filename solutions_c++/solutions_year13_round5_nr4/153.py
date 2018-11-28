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

#define PROBLEM_NAME "D-small-attempt0"
//#define PROBLEM_NAME "my"

int MAX;
int n;
char s[51];
double dp[1<<22];

double get(int mask) {
    if (mask == MAX) return 0;
    if (dp[mask] >= -1e-7) return dp[mask];
    double ret = 0;
    for (int i = 0; i < n; i++) {
        int money = n;
        int nxtMask = -1;
        for (int j = 0; j < n; j++) {
            int k = i+j;
            if (k >= n) k -= n;
            if (!((mask>>k)&1)) {
                nxtMask = mask | (1<<k);
                break;
            }
            money--;
        }
        ret += money + get(nxtMask);
    }
    ret /= n;
    return dp[mask] = ret;
}

void solveCase(int tc) {
    gets(s);
    n = strlen(s);
    MAX = (1<<n)-1;
    int maskInit = 0;
    rep(i, n)
        if (s[i] == 'X')
            maskInit |= (1<<i);
    rep(i, MAX)
        dp[i] = -1;
    double ret = get(maskInit);
    printf("Case #%d: %.10lf\n", tc+1, ret);
    fprintf(stderr, "Case #%d: %.10lf\n", tc+1, ret);
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
