// {{{ Headers
// vim:filetype=cpp:foldmethod=marker:foldmarker={{{,}}}

#include <cassert>
#include <cctype>
#include <cmath>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

#include <algorithm>
#include <deque>
#include <functional>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#include <fstream>
#include <iostream>
#include <sstream>

#include <ext/numeric>

using namespace std;
using namespace __gnu_cxx;
// }}}

typedef long long int64;
const int INF = 0x3f3f3f3f;
const int dx [] = { -1, -1, -1, +0, +1, +1, +1, +0 }; // NW, N, NE, E, SE, S, SW, W neighbours.
const int dy [] = { -1, +0, +1, +1, +1, +0, -1, -1 };
template <class T> inline int len (const T &a) { return a.size (); }

int R, C, M;
vector <string> grid;

void
dfs (int x, int y) {
    if (grid [x][y] != '.') return;
    int cnt = 0;
    for (int h = 0; h < 8; h++) {
        int X = x + dx [h], Y = y + dy [h];
        if (X < 0 || X >= R || Y < 0 || Y >= C) continue;
        if (grid [X][Y] == '*') cnt++;
    }
    grid [x][y] = cnt + '0';
    if (cnt) return;
    for (int h = 0; h < 8; h++) {
        int X = x + dx [h], Y = y + dy [h];
        if (X < 0 || X >= R || Y < 0 || Y >= C) continue;
        if (grid [X][Y] == '*') continue;
        dfs (X, Y);
    }
}

int
main () {
#ifdef LOCALHOST
    freopen ("test.in", "r", stdin);
    // freopen ("test.out", "w", stdout);
#endif
    int T;
    scanf ("%d", &T);
    for (int t = 1; t <= T; t++) {
        bool ok = false;
        scanf ("%d %d %d", &R, &C, &M);
        for (int mask = 0; mask < (1 << (R * C)) - 1; mask++) {
            if (__builtin_popcount (mask) != M) continue;
            grid.clear ();
            string s = "";
            for (int i = 0; i < C; i++) s += '.';
            for (int i = 0; i < R; i++) grid.push_back (s);
            for (int i = 0; i < R * C; i++) {
                if (mask & 1 << i) {
                    int x = i / C, y = i % C;
                    grid [x][y] = '*';
                }
            }
            int x = -1, y = -1;
            for (int i = 0; i < R; i++)
                for (int j = 0; j < C; j++)
                    if (grid [i][j] == '.') {
                        x = i, y = j;
                        break;
                    }
            if (x == -1 || y == -1) continue;
            dfs (x, y);
            int cnt = 0;
            for (int i = 0; i < R; i++) 
                for (int j = 0; j < C; j++) 
                    cnt += (grid [i][j] == '.');
            if (cnt == 0) { ok = true; break; }
        }
        if (! ok) printf ("Case #%d:\nImpossible\n", t);
        else {
            printf ("Case #%d:\n", t);
            if (M != R * C - 1) {
                for (int i = 0; i < R; i++) 
                    for (int j = 0; j < C; j++) 
                        if (grid [i][j] == '0') {
                            grid [i][j] = 'c';
                            goto label;
                        }
            }
            else {
                for (int i = 0; i < R; i++) 
                    for (int j = 0; j < C; j++) 
                        if (grid [i][j] != '*')
                            grid [i][j] = 'c';
            }
            label:
            for (int i = 0; i < R; i++) 
                for (int j = 0; j < C; j++) 
                    if (grid [i][j] != '*' && grid [i][j] != 'c') grid [i][j] = '.';
            for (int i = 0; i < R; i++) printf ("%s\n", grid [i].c_str ());
        }
    }
    return 0;
}

