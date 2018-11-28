#define LARGE
//#define SMALL

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int t, T;
int i, r, R, c, C;

int main()
{
#if defined(LARGE)
    freopen("../A-large.in", "r", stdin);
    freopen("../A-large.out", "w", stdout);
#elif defined(SMALL)
    freopen("../A-small-attempt0.in", "r", stdin);
    freopen("../A-small.out", "w", stdout);
#else
    freopen("input.txt", "r", stdin);
#endif

    cin >> T;

    for(t = 0; t < T; ++t)
    {
        cin >> R >> C;
        vector<string> grid(R);
        int changed = 0;
        bool possible = true;
        for (r = 0; r < R; ++r)
        {
            cin >> grid[r];
        }
        for (r = 0; r < R; ++r)
        {
            for (c = 0; c < C; ++c)
            {
                if (grid[r][c] == '^')
                {
                    for (i = r-1; i >= 0; --i)
                    {
                        if (grid[i][c] != '.') break;
                    }
                    if (i >= 0) continue;
                    else ++changed;
                    for (i = r+1; i < R; ++i)
                    {
                        if (grid[i][c] != '.') break;
                    }
                    if (i < R)
                    {
                        grid[r][c] = 'v';
                        continue;
                    }
                    for (i = c-1; i >= 0; --i)
                    {
                        if (grid[r][i] != '.') break;
                    }
                    if (i >= 0)
                    {
                        grid[r][c] = '<';
                        continue;
                    }
                    for (i = c+1; i < C; ++i)
                    {
                        if (grid[r][i] != '.') break;
                    }
                    if (i < C) grid[r][c] = '>';
                    else
                    {
                        possible = false;
                        break;
                    }
                }
                else if (grid[r][c] == 'v')
                {
                    for (i = r+1; i < R; ++i)
                    {
                        if (grid[i][c] != '.') break;
                    }
                    if (i < R) continue;
                    else ++changed;
                    for (i = r-1; i >= 0; --i)
                    {
                        if (grid[i][c] != '.') break;
                    }
                    if (i >= 0)
                    {
                        grid[r][c] = '^';
                        continue;
                    }
                    for (i = c-1; i >= 0; --i)
                    {
                        if (grid[r][i] != '.') break;
                    }
                    if (i >= 0)
                    {
                        grid[r][c] = '<';
                        continue;
                    }
                    for (i = c+1; i < C; ++i)
                    {
                        if (grid[r][i] != '.') break;
                    }
                    if (i < C) grid[r][c] = '>';
                    else
                    {
                        possible = false;
                        break;
                    }
                }
                else if (grid[r][c] == '<')
                {
                    for (i = c-1; i >= 0; --i)
                    {
                        if (grid[r][i] != '.') break;
                    }
                    if (i >= 0) continue;
                    else ++changed;
                    for (i = r-1; i >= 0; --i)
                    {
                        if (grid[i][c] != '.') break;
                    }
                    if (i >= 0)
                    {
                        grid[r][c] = 'v';
                        continue;
                    }
                    for (i = r+1; i < R; ++i)
                    {
                        if (grid[i][c] != '.') break;
                    }
                    if (i < R)
                    {
                        grid[r][c] = '^';
                        continue;
                    }
                    for (i = c+1; i < C; ++i)
                    {
                        if (grid[r][i] != '.') break;
                    }
                    if (i < C) grid[r][c] = '>';
                    else
                    {
                        possible = false;
                        break;
                    }
                }
                else if (grid[r][c] == '>')
                {
                    for (i = c+1; i < C; ++i)
                    {
                        if (grid[r][i] != '.') break;
                    }
                    if (i < C) continue;
                    else ++changed;
                    for (i = r-1; i >= 0; --i)
                    {
                        if (grid[i][c] != '.') break;
                    }
                    if (i >= 0)
                    {
                        grid[r][c] = 'v';
                        continue;
                    }
                    for (i = r+1; i < R; ++i)
                    {
                        if (grid[i][c] != '.') break;
                    }
                    if (i < R)
                    {
                        grid[r][c] = '^';
                        continue;
                    }
                    for (i = c-1; i >= 0; --i)
                    {
                        if (grid[r][i] != '.') break;
                    }
                    if (i >= 0) grid[r][c] = '<';
                    else
                    {
                        possible = false;
                        break;
                    }
                }
            }
            if (!possible) break;
        }

        if (possible) cout << "Case #" << t+1 << ": " << changed << "\n";
        else cout << "Case #" << t+1 << ": " << "IMPOSSIBLE" << "\n";
    }

    return 0;
}
