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
#define SIZE(t) ((int)((t).size()))
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

int N;
int A[4][4], B[4][4];

bool zle() {
    REP(w,N) {
        // test ci je worker w zly
        vector<int> wskills;
        REP(s,N) if (B[w][s]) wskills.push_back(s);
        do {
            int vyzral = 0;
            REP(n,N) {
                if (w == n) continue;
                if (vyzral == SIZE(wskills)) break;
                if (B[n][wskills[vyzral]]) ++vyzral;
            }
            if (vyzral == SIZE(wskills)) return true;
        } while( next_permutation( wskills.begin(), wskills.end() ) );
    }
    return false;
}

int main() {
    int T; cin >> T;
    FOR(tt,1,T) {
        cin >> N;
        int start = 0;
        REP(a,N) {
            string S; cin >> S;
            REP(b,N) {
                A[a][b] = (S[b]=='1');
                if (A[a][b]) start |= 1 << (N*a+b);
            }
        }
        int best = N*N+47;
        for (int add=0; add<(1<<(N*N)); ++add) {
            if (start & add) continue;
            REP(a,N) REP(b,N) {
                B[a][b] = A[a][b];
                if (add & 1 << (N*a+b)) B[a][b] = 1;
            }
            if (!zle()) best = min( best, __builtin_popcount(add) );
        }
        printf("Case #%d: %d\n",tt,best);
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
