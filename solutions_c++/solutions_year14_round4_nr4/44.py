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
typedef vector<string> VS;
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

int W, S; // words, servers
vector<string> words;

vector<int> node_count;

int compute_node_count(const vector<string> &VS) {
    set<string> tmp;
    for (string s:VS) for (unsigned l=0; l<=s.size(); ++l) tmp.insert( string( s.begin(), s.begin()+l ) );
    return tmp.size();
}

void compute_node_count() {
    node_count.clear();
    node_count.resize(1 << W);
    for (int mam=0; mam<(1<<W); ++mam) {
        vector<string> tmp;
        for (int w=0; w<W; ++w) if (mam & 1<<w) tmp.push_back( words[w] );
        node_count[mam] = compute_node_count(tmp);
    }
}

int mostmemo[5][256], cntmemo[5][256];

void solve(int serverov, int slova) {
    //cout << "solve " << serverov << " " << slova << endl;
    if (mostmemo[serverov][slova] != -1) return;

    int &most = mostmemo[serverov][slova];
    int &cnt  =  cntmemo[serverov][slova];
    if (serverov==1) { most=node_count[slova]; cnt=1; return; }
    most = 0;
    cnt = 0;
    for (int tu=1; tu<(1<<W); ++tu) if ((slova & tu) == tu) { // nie 0
        int tam = slova ^ tu;
        if (__builtin_popcount(tam) < serverov-1) continue; // primalo ostalo
        solve(serverov-1,tam);
        if (node_count[tu] + mostmemo[serverov-1][tam] > most) {
            most = node_count[tu] + mostmemo[serverov-1][tam];
            cnt = cntmemo[serverov-1][tam];
        } else if (node_count[tu] + mostmemo[serverov-1][tam] == most) {
            cnt += cntmemo[serverov-1][tam];
        }
    }
}

int main() {
    int T; cin >> T;
    FOR(test,1,T) {
        cin >> W >> S;
        words.clear();
        words.resize(W);
        for (string &word:words) cin >> word;
        compute_node_count();
        memset( mostmemo, -1, sizeof(mostmemo) );
        solve(S,(1<<W)-1);
        cout << "Case #" << test << ": " << mostmemo[S][(1<<W)-1] << " " << cntmemo[S][(1<<W)-1] << endl;
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
