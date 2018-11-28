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
#define REP(i,n) for(int i=0;i<(int)(n);++i)
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

int main() {
    int T; cin >> T;
    FOR(t,1,T) {
        int N; cin >> N;
        vector<int> A(N), B(N);
        REP(n,N) cin >> A[n];
        REP(n,N) cin >> B[n];
        vector< vector<bool> > menej(N, vector<bool>(N,false));
        REP(n,N) {
            for (int i=n-1; i>=0; --i) if (A[i]==A[n]) { menej[n][i] = true; break; }
            for (int i=n-1; i>=0; --i) if (A[i]==A[n]-1) { menej[i][n] = true; break; }
            for (int i=n+1; i<N; ++i) if (B[i]==B[n]) { menej[n][i] = true; break; }
            for (int i=n+1; i<N; ++i) if (B[i]==B[n]-1) { menej[i][n] = true; break; }
        }
        REP(k,N) REP(a,N) REP(b,N) if (menej[a][k] && menej[k][b]) menej[a][b] = true;
        /*
        REP(a,N) {
            REP(b,N) cout << menej[a][b] << " ";
            cout << endl;
        }
        */
        vector<bool> used(N,false);
        vector<int> answer(N,-1);
        FOR(add,1,N) {
            REP(n,N) {
                if (used[n]) continue;
                bool ok = true;
                REP(a,N) if (!used[a] && menej[a][n]) { ok=false; break; }
                if (ok) {
                    answer[n] = add;
                    used[n] = true;
                    // cout << "davam " << add << " na " << n << endl;
                    break;
                }
            }
        }
        cout << "Case #" << t << ":";
        for (int a : answer) cout << " " << a;
        cout << endl;
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
