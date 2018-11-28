#define _USE_MATH_DEFINES
#include <iostream>
#include <utility>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <climits>
#include <cstring>
#include <cmath>
#include <queue>
#include <functional>
#include <cstdio>
#include <cassert>
#include <stack>

#define mp make_pair
#define mt(x,y,z) mp((x), mp((y), (z)))
#define ZERO(x) memset((x), 0, sizeof(x))
#define NEGATE(x) memset((x), 255, sizeof(x))
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;

// globals starts here

const int MAX_R = 105;
char grid[MAX_R][MAX_R];

int di[] = { 0, 0, 1, -1 };
int dj[] = { 1, -1, 0, 0 };

int main()
{
#ifdef DEBUGAGA
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);	
#elif defined(CONTEST)
    freopen(CONTEST ".in", "r", stdin);
    freopen(CONTEST ".out", "w", stdout);
#endif

    int tests;
    cin >> tests;
    for (int tc = 1; tc <= tests; ++tc)
    {
        int r, c;
        cin >> r >> c;

        for (int i = 0; i < r; ++i)
        {
            cin >> grid[i];
        }

        int cnt = 0;
        bool ok = true;
        for (int i = 0; i < r && ok; ++i)
        {
            for (int j = 0; j < c && ok; ++j)
            {
                int dx = 0;
                int dy = 0;
                switch (grid[i][j])
                {
                case '^':
                    dy = -1;
                    break;
                case 'v':
                    dy = 1;
                    break;
                case '<':
                    dx = -1;
                    break;
                case '>':
                    dx = 1;
                    break;
                }

                if (dx == 0 && dy == 0)
                {
                    continue;
                }

                bool good = false;
                int ii = i + dy;
                int jj = j + dx;
                for (; ii >= 0 && ii < r && jj >= 0 && jj < c; ii += dy, jj += dx)
                {
                    if (grid[ii][jj] != '.')
                    {
                        good = true;
                        break;
                    }
                }

                if (!good)
                {
                    ++cnt;

                    bool found = false;
                    for (int k = 0; k < 4 && !found; ++k)
                    {
                        dx = dj[k];
                        dy = di[k];
                        ii = i + dy;
                        jj = j + dx;
                        for (; ii >= 0 && ii < r && jj >= 0 && jj < c; ii += dy, jj += dx)
                        {
                            if (grid[ii][jj] != '.')
                            {
                                found = true;
                                break;
                            }
                        }
                    }

                    if (!found)
                    {
                        ok = false;
                    }
                }
            }
        }

        if (!ok)
        {
            printf("Case #%d: IMPOSSIBLE\n", tc);
        }
        else
        {
            printf("Case #%d: %d\n", tc, cnt);
        }
    }

    return 0;
}