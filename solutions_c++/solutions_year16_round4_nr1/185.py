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
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

map< pair<char,char>, char > wins;
void init() {
    wins[ {'P','R'} ] = 'P';
    wins[ {'R','P'} ] = 'P';
    wins[ {'P','S'} ] = 'S';
    wins[ {'S','P'} ] = 'S';
    wins[ {'R','S'} ] = 'R';
    wins[ {'S','R'} ] = 'R';
}

string solve(int n, int p, int r, int s, string order) {
    if (n == 0) return string(p,'P') + string(r,'R') + string(s,'S');
    if (p > r+s || r > p+s || s > r+p) return "";
    int pr, ps, rs; if (r >= s) { int delta = r-s; ps = (p-delta)/2; pr = ps + delta; rs = (1<<(n-1)) - pr - ps; } else { int delta = s-r; pr = (p-delta)/2; ps = pr + delta; rs = (1<<(n-1)) - pr - ps; } assert( pr >= 0 && ps >= 0 && rs >= 0);
    string neworder;
    neworder += wins[ { order[0],order[1] } ];
    neworder += wins[ { order[0],order[2] } ];
    neworder += wins[ { order[1],order[2] } ];
    string tmp = solve( n-1, pr, rs, ps, neworder );
    
    map<char,int> invorder;
    invorder[ order[0] ] = 0;
    invorder[ order[1] ] = 1;
    invorder[ order[2] ] = 2;

    string ans;
    for (char c : tmp) {
        if (c == 'P') {
            if (invorder['P'] < invorder['R']) ans += "PR"; else ans += "RP";
        }
        if (c == 'R') {
            if (invorder['R'] < invorder['S']) ans += "RS"; else ans += "SR";
        }
        if (c == 'S') {
            if (invorder['P'] < invorder['S']) ans += "PS"; else ans += "SP";
        }
    }
    return ans;

    /*
    map< pair<char,char>, int> CNT; 
    CNT[ {'P','R'} ] = CNT[ {'R','P'} ] = pr;
    CNT[ {'P','S'} ] = CNT[ {'S','P'} ] = ps;
    CNT[ {'R','S'} ] = CNT[ {'S','R'} ] = rs;
    */
}

int main() {
    init();
    int T; cin >> T;
    FOR(tt,1,T) {
        int N,P,R,S; cin >> N >> R >> P >> S;
        string ans = solve(N,P,R,S,"PRS");
        if (ans == "") ans = "IMPOSSIBLE";
        cout << "Case #" << tt << ": " << ans << endl;
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
