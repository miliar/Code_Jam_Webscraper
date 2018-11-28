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

int rect[1024][4];
int G[1024][1024];
int D[1024];
bool done[1024];

int idist(int a, int b, int c, int d) {
    if (b<c) return c-b;
    if (d<a) return a-d;
    return 0;
}

int main() {
    int T; cin >> T;
    FOR(test,1,T) {
        int W, H, B; cin >> W >> H >> B;
        for (int b=0; b<B; ++b) {
            for (int i=0; i<4; ++i) cin >> rect[b][i];
            ++rect[b][2];
            ++rect[b][3];
        }
        for (int a=0; a<B; ++a) for (int b=0; b<B; ++b) {
            int xdist = idist( rect[a][0], rect[a][2], rect[b][0], rect[b][2] );
            int ydist = idist( rect[a][1], rect[a][3], rect[b][1], rect[b][3] );
            G[a][b] = max( xdist, ydist );
        }
        for (int a=0; a<B; ++a) G[a][B] = G[B][a] = rect[a][0];
        for (int a=0; a<B; ++a) G[a][B+1] = G[B+1][a] = W - rect[a][2];
        G[B][B+1] = G[B+1][B] = W;
        for (int a=0; a<B+2; ++a) D[a] = 987654321; 
        for (int a=0; a<B+2; ++a) done[a] = false;
        D[B] = 0;
        while (!done[B+1]) {
            int kde=-1;
            for (int a=0; a<B+2; ++a) {
                if (done[a]) continue;
                if (kde==-1) kde=a;
                if (D[a] < D[kde]) kde=a;
            }
            done[kde] = true;
            for (int a=0; a<B+2; ++a) D[a] = min( D[a], D[kde] + G[kde][a] );
        }
        cout << "Case #" << test << ": " << D[B+1] << endl;
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
