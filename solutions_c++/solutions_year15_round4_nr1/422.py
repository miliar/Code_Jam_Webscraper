/*
g++ -g -DBUG -D_GLIBCXX_DEBUG -std=c++11 -Wall -Wfatal-errors -o cjam{,.cpp}
g++ -O3 -std=c++11 -Wall -Wfatal-errors -o cjam{,.cpp}
ulimit -s 1268435456
*/
#include <bits/stdc++.h>
#ifdef BUG
    #include "debug.hpp"
#else
    #define DEBUG(var)
#endif
#define NO_IO_TIE ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define CASE(i) "Case #" << (i) + 1 << ": "

using namespace std;
template<class T1, class T2> inline istream &
operator>>(istream & fin, pair<T1, T2> & pr)
{ fin >> pr.first >> pr.second; return fin; }
template<class T0, class T1, class T2> inline istream &
operator>>(istream & fin, tuple<T0, T1, T2> & t)
{ fin >> get<0>(t) >> get<1>(t) >> get<2>(t); return fin; }
template<class T> inline istream &
operator>>(istream & fin, vector<T> & a) {
for(auto & u: a) fin >> u; return fin; }
template<class T, size_t n> inline istream &
operator>>(istream & fin, array<T, n> & a) {
for(auto & u: a) fin >> u; return fin; }
/* ------------------------------ */

inline bool
xwalk(const int r,  const int c,
      const int di, const int dj,
      const vector<string> & grid)
{
    const int n = grid.size();
    const int m = n ? grid.front().size() : 0;

    for(int i = r + di, j = c + dj; -1 < i && i < n && -1 < j && j < m; i += di, j += dj)
        if(grid[i][j] != '.')
            return true;

    return false;
}


inline int
walk(const int r, const int c, const vector<string> & grid)
{
    if(grid[r][c] == '.')
        return 0;

    const auto ch = grid[r][c];

    const int di = ch == '^' ? -1 : ch == 'v' ? 1 : 0;
    const int dj = ch == '<' ? -1 : ch == '>' ? 1 : 0;

    if(xwalk(r, c, di, dj, grid))
        return 0;

    if(xwalk(r, c, 1, 0, grid) || xwalk(r, c, -1, 0, grid)
            || xwalk(r, c, 0, 1, grid) || xwalk(r, c, 0, -1, grid))
        return 1;

    return -1;
}

inline int
pegman()
{
    int n, m;
    cin >> n >> m;

    vector<string> grid(n);
    cin >> grid;

    int val = 0;
    for(int i = 0; i < n; ++ i)
        for(int j = 0; j < m; ++ j)
        {
            const auto inc = walk(i, j, grid);
            if(inc == -1)
                return -1;
            else
                val += inc;
        }

    return val;
}

int main( const int argc, char * argv [])
{
    NO_IO_TIE;
    size_t ncase;
    cin >> ncase;

    for(size_t i = 0; i < ncase; ++i, cout << '\n') {
        cerr << '~' << std::flush;
        const auto val = pegman();
        cout << CASE(i);

        if(val != -1)
            cout << val;
        else
            cout << "IMPOSSIBLE";

    }

    return EXIT_SUCCESS;
}
