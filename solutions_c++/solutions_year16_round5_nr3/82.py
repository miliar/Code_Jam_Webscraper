// another fine solution by misof
// #includes {{{
#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

#include <cassert>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <cmath>
#include <complex>
using namespace std;
// }}}

/////////////////// PRE-WRITTEN CODE FOLLOWS, LOOK DOWN FOR THE SOLUTION ////////////////////////////////

// pre-written code {{{
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define REP(i,n) for(int i=0;i<(int)(n);++i)
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

struct asteroid { double x,y,z,dx,dy,dz; };
int N, S;
vector<asteroid> A;

inline double sqr(double x) { return x*x; }

inline double adist(int i, int j) {
    return sqrt( sqr( A[i].x - A[j].x ) + sqr( A[i].y - A[j].y ) + sqr( A[i].z - A[j].z ) );
}

int main() {
    int T; cin >> T;
    FOR(test,1,T) {
        cin >> N >> S;
        A.clear();
        A.resize(N);
        REP(n,N) cin >> A[n].x >> A[n].y >> A[n].z >> A[n].dx >> A[n].dy >> A[n].dz;
        vector<double> treedist(N);
        treedist[0] = 0;
        for (int n=1; n<N; ++n) treedist[n] = adist(0,n);
        vector<bool> done(N,false);
        done[0] = true;
        double answer = 0;
        while (true) {
            double curr = 1e20;
            double cand = -1;
            REP(n,N) if (!done[n]) if (treedist[n] < curr) { curr=treedist[n]; cand=n; }
            done[cand] = true;
            answer = max( answer, treedist[cand] );
            if (cand == 1) break;
            REP(n,N) if (!done[n]) treedist[n] = min( treedist[n], adist(cand,n) );
        }
        printf("Case #%d: %.20f\n",test,answer);
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
