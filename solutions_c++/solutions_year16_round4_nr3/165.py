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
// BEGIN CUT HERE
#define DEBUG(var) { cout << #var << ": " << (var) << endl; }
template <class T> ostream& operator << (ostream &os, const vector<T> &temp) { os << "[ "; for (unsigned int i=0; i<temp.size(); ++i) os << (i?", ":"") << temp[i]; os << " ]"; return os; } // DEBUG
template <class T> ostream& operator << (ostream &os, const set<T> &temp) { os << "{ "; for(__typeof((temp).begin()) it=(temp).begin();it!=(temp).end();++it) os << ((it==(temp).begin())?"":", ") << (*it); os << " }"; return os; } // DEBUG
template <class T> ostream& operator << (ostream &os, const multiset<T> &temp) { os << "{ "; for(__typeof((temp).begin()) it=(temp).begin();it!=(temp).end();++it) os << ((it==(temp).begin())?"":", ") << (*it); os << " }"; return os; } // DEBUG
template <class S, class T> ostream& operator << (ostream &os, const pair<S,T> &a) { os << "(" << a.first << "," << a.second << ")"; return os; } // DEBUG
template <class S, class T> ostream& operator << (ostream &os, const map<S,T> &temp) { os << "{ "; for(__typeof((temp).begin()) it=(temp).begin();it!=(temp).end();++it) os << ((it==(temp).begin())?"":", ") << (it->first) << "->" << it->second; os << " }"; return os; } // DEBUG
namespace aux{
    template<std::size_t...> struct seq{};
    template<std::size_t N, std::size_t... Is> struct gen_seq : gen_seq<N-1, N-1, Is...>{};
    template<std::size_t... Is> struct gen_seq<0, Is...> : seq<Is...>{};
    template<class Ch, class Tr, class Tuple, std::size_t... Is> void print_tuple(std::basic_ostream<Ch,Tr>& os, Tuple const& t, seq<Is...>) { using swallow = int[]; (void)swallow{0, (void(os << (Is == 0? "" : ", ") << std::get<Is>(t)), 0)...}; }
} // aux::
template<class Ch, class Tr, class... Args> auto operator<<(std::basic_ostream<Ch, Tr>& os, std::tuple<Args...> const& t) -> std::basic_ostream<Ch, Tr>& { os << "("; aux::print_tuple(os, t, aux::gen_seq<sizeof...(Args)>()); return os << ")"; }
// END CUT HERE
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define REP(i,n) for(int i=0;i<(int)(n);++i)
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

int N, R, C, D;
char maze[128][128];
vector< set<int> > G;
vector<int> match;

void add_edge(int x, int y) { G[x].insert(y); G[y].insert(x); }
void del_edge(int x, int y) { G[x].erase(y); G[y].erase(x); }

void build_graph() {
    N = 4*R*C + D;
    G.clear();
    G.resize(N);
    REP(r,R) REP(c,C) {
        // vnutri bunky
        for (int d=0; d<4; ++d) add_edge( 4*C*r + 4*c + d, 4*C*r + 4*c + (d+1)%4 );
        // do susednych buniek hore / vlavo
        if (r > 0) add_edge( 4*C*r + 4*c + 0, 4*C*(r-1) + 4*c + 2 );
        if (c > 0) add_edge( 4*C*r + 4*c + 3, 4*C*r + 4*(c-1) + 1 );
    }
    // dvorania
    for (int d=0; d<C; ++d) add_edge( 4*R*C + d, 4*C*0 + 4*d + 0 );
    for (int d=0; d<R; ++d) add_edge( 4*R*C + C + d, 4*C*d + 4*(C-1) + 1 );
    for (int d=0; d<C; ++d) add_edge( 4*R*C + C + R + d, 4*C*(R-1) + 4*(C-1-d) + 2 );
    for (int d=0; d<R; ++d) add_edge( 4*R*C + 2*C + R + d, 4*C*(R-1-d) + 4*0 + 3 );
}

bool connect(int dvoran) {
    vector<bool> visited(N,false);
    vector<int> from(N,-1);
    visited[ 4*R*C + dvoran ] = true;
    queue<int> Q;
    Q.push(4*R*C + dvoran);
    while (!Q.empty()) {
        int kde = Q.front(); Q.pop();
        if (kde == 4*R*C + match[dvoran]) break;
        REP(kolo,2) for (int kam : G[kde]) {
            if (kolo==0 && kde < 4*R*C && kam < 4*R*C && kde/4 == kam/4) continue;
            if (!visited[kam]) {
                visited[kam] = true;
                from[kam] = kde;
                Q.push(kam);
            }
        }
    }
    if (!visited[ 4*R*C + match[dvoran]]) return false;
    // teraz nakresli lomitka forcnute cestou
    int kde = 4*R*C + match[dvoran];
    while (kde != 4*R*C + dvoran) {
        int x = kde, y = from[kde];
        kde = from[kde];
        if (x >= 4*R*C || y >= 4*R*C) continue;
        if (x/4 != y/4) continue;
        int a = x%4, b = y%4;
        x /= 4;
        int r = x/C, c = x%C;
        //DEBUG(r); DEBUG(c);
        if (a > b) swap(a,b);
        assert(!(a==0 && b==1 && maze[r][c]=='/'));
        assert(!(a==2 && b==3 && maze[r][c]=='/'));
        assert(!(a==0 && b==3 && maze[r][c]=='\\'));
        assert(!(a==1 && b==2 && maze[r][c]=='\\'));
        if ((a == 0 && b == 1) || (a == 2 && b == 3)) {
            maze[r][c] = '\\';
            del_edge( 4*C*r + 4*c + 0, 4*C*r + 4*c + 3 );
            del_edge( 4*C*r + 4*c + 1, 4*C*r + 4*c + 2 );
        }
        if ((a == 0 && b == 3) || (a == 1 && b == 2)) {
            maze[r][c] = '/';
            del_edge( 4*C*r + 4*c + 0, 4*C*r + 4*c + 1 );
            del_edge( 4*C*r + 4*c + 2, 4*C*r + 4*c + 3 );
        }
    }
    return true;
}

bool is_collision(int a, int b, int c, int d) {
    if (a > b) swap(a,b);
    if (c > d) swap(c,d);
    if (a < c && c < b && b < d) return true;
    if (c < a && a < d && d < b) return true;
    return false;
}

int main() {
    int T; cin >> T;
    FOR(tt,1,T) {
        cout << "Case #" << tt << ":" << endl;
        cin >> R >> C;
        REP(r,R) REP(c,C) maze[r][c] = '.';
        D = 2*(R+C);
        match.clear();
        match.resize(D);
        for (int d=0; d<D/2; ++d) {
            int x,y; cin >> x >> y; --x; --y;
            match[x] = y;
            match[y] = x;
        }
        bool collision = false;
        for (int x=0; x<D; ++x) for (int y=0; y<D; ++y) if (x!=y && x!=match[y]) if (is_collision(x,match[x],y,match[y])) collision = true;
        if (collision) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        bool found = false;
        for (int GARDEN=0; GARDEN<(1<<(R*C)); ++GARDEN) {
            build_graph();
            REP(r,R) REP(c,C) {
                if (GARDEN & 1 << (r*C+c)) {
                    maze[r][c] = '\\';
                    del_edge( 4*C*r + 4*c + 0, 4*C*r + 4*c + 3 );
                    del_edge( 4*C*r + 4*c + 1, 4*C*r + 4*c + 2 );
                } else {
                    maze[r][c] = '/';
                    del_edge( 4*C*r + 4*c + 0, 4*C*r + 4*c + 1 );
                    del_edge( 4*C*r + 4*c + 2, 4*C*r + 4*c + 3 );
                }
            }
            found = true;
            REP(d,D) {
                found &= connect(d);// T[4*R*C+d][4*R*C+match[d]];
                if (!found) break;
            }
            if (found) break;
        }
        if (found) {
            REP(r,R) {
                REP(c,C) cout << maze[r][c];
                cout << endl;
            }
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
