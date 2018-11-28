#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#pragma warning( disable : 4244 4267 4018 4996 4800 )
//#pragma comment( linker, "/stack:10000000" )
using namespace std; 
typedef vector< int > vi; typedef vector< vector< int > > vvi; typedef vector< string > vs; typedef vector< double > vd;
typedef vector< vd > vvd; typedef long long ll; typedef vector< ll > vll; typedef vector< vll > vvll; typedef pair< int, int > pii;
#define all( v ) (v).begin( ), (v).end( )

ifstream in( "a.in" );
ofstream out( "a.out" );

vs p;
int R, C;
int dx[] = {0, -1, 0, 1};
int dy[] = {1, 0, -1, 0};

int chtodir(char ch) {
    switch (ch) {
    case '^': return 2;
    case '>': return 3;
    case 'v': return 0;
    case '<': return 1;
    }
}

bool is_edge(int r, int c, int dir) {
    for (;;) {
        r += dy[dir]; c += dx[dir];
        if (!(r >= 0 && c >= 0 && r < R && c < C))
            return true;
        if (p[r][c] != '.')
            return false;
    }
}

int main() {
    int ntests;
    in >> ntests;
    for (int test = 1; test <= ntests; ++test) {        
        in >> R >> C;
        p.resize(R);
        for (auto & s : p) in >> s;
        int cnt = 0;
        for (int r = 0; r < R; ++r) {
            for (int c = 0; c < C; ++c) {
                if (cnt == -1) break;
                if (p[r][c] == '.') continue;
                int edge[4];
                for (int i = 0; i < 4; ++i) {
                    edge[i] = is_edge(r, c, i);
                }
                int curdir = chtodir(p[r][c]);
                if (edge[curdir]) {
                    if (all_of(edge, edge + 4, [](int x) { return x; }))
                        cnt = -1;
                    else
                        ++cnt;
                }
            }
        }
        out << "Case #" << test << ": " << (cnt == -1 ? "IMPOSSIBLE" : to_string(cnt)) << "\n";
    }
    return 0;
}