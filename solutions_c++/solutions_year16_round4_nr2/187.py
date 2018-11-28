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

long double cnt[256][256]; // cnt[x][y] je suma pp cez vsetky moznosti ako z prvych x ludi dostat y kladnych hlasov

long double eval(const vector<long double> &P) {
    int N = P.size();
    cnt[0][0] = 0;
    cnt[1][1] = P[0];
    cnt[1][0] = 1 - P[0];
    for (int poc=2; poc<=N; ++poc) {
        for (int kl=0; kl<=poc; ++kl) {
            cnt[poc][kl] = 0;
            if (kl > 0) cnt[poc][kl] += cnt[poc-1][kl-1] * P[poc-1];
            if (kl < poc) cnt[poc][kl] += cnt[poc-1][kl] * (1 - P[poc-1]);
        }
    }
    return cnt[N][N/2];
}

int main() {
    int T; cin >> T;
    FOR(tt,1,T) {
        int N, K; cin >> N >> K;
        vector<long double> P(N);
        REP(n,N) cin >> P[n];
        sort( P.begin(), P.end() );

        double best = 0;
        for (int prefix=0; prefix<=K; ++prefix) {
            vector<long double> Q;
            Q.insert( Q.end(), P.begin(), P.begin()+prefix );
            Q.insert( Q.end(), P.end()-(K-prefix), P.end() );
            long double curr = eval(Q);
            if (curr > best) best = curr;
        }
        printf("Case #%d: %.15f\n",tt,best);
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
