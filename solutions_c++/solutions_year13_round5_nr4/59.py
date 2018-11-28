// another fine solution by misof
// #includes {{{
#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;
// }}}

/////////////////// PRE-WRITTEN CODE FOLLOWS, LOOK DOWN FOR THE SOLUTION ////////////////////////////////

// pre-written code {{{
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

int N;
double memo[1<<20];

double solve(int config) {
    if (config == (1<<N)-1) return 0.;
    double &res = memo[config];
    if (res >= 0) return res;
    int cakat[20];
    if (config & 1) {
        int kde=N-1;
        while ((config >> kde) & 1) --kde;
        cakat[0] = N-kde;
    } else cakat[0] = 0;
    for (int n=1; n<N; ++n) {
        if ((config >> n) & 1) cakat[n] = cakat[n-1]+1; else cakat[n]=0;
    }
    res = 0.;
    double pp = 1./N;
    for (int n=0; n<N; ++n) {
        int nconfig = config;
        int zaplni = n - cakat[n];
        while (zaplni<0) zaplni += N;
        nconfig |= 1<<zaplni;
        res += pp * ( N - cakat[n] + solve(nconfig) );
    }
    return res;
}

int main() {
    int T; cin >> T;
    FOR(test,1,T) {
        string S; cin >> S;
        reverse(S.begin(),S.end());
        N = S.size();
        for (int x=0; x<(1<<N); ++x) memo[x] = -1;
        int start = 0;
        for (int n=0; n<N; ++n) if (S[n]=='X') start |= 1<<n;
        printf("Case #%d: %.20f\n",test,solve(start));
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
