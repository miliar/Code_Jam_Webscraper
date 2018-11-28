#include <cassert>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <climits>
#include <cstddef>
#include <cctype>
#include <cmath>
#include <cstring>
#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <numeric>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <bitset>
#include <list>
#include <string>
#include <functional>
#include <utility>
using namespace std;
typedef long long llint;
int const S = 5;
inline bool in(int x, int y, int nr, int nc)
{
    return x >= 0 && x < nr && y >= 0 && y < nc;
}
bool bfs(char board[][S + 10], int nr, int nc, int m)
{
    static int const ND = 8;
    static int const D[ND][2] = {
        {-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1},
        {1, -1}, {1, 0}, {1, 1}};
    queue <pair <int, int> > q;
    set <pair <int, int> > visited;
    for (int r = 0; r < nr; ++r)
    {
        for (int c = 0; c < nc; ++c)
        {
            if (board[r][c] != '.')
            {
                continue;
            }
            int cnt = 0;
            for (int d = 0; d < ND; ++d)
            {
                int x = r + D[d][0], y = c + D[d][1];
                if (in(x, y, nr, nc) && board[x][y] == '*')
                {
                    ++cnt;
                }
            }
            if (cnt == 0)
            {
                board[r][c] = 'c';
                q.push(make_pair(r, c));
                visited.insert(make_pair(r, c));
                goto END_1;
            }
        }
    }
END_1:
    ;
    while (!q.empty())
    {
        pair <int, int> entry = q.front();
        q.pop();
        int r = entry.first, c = entry.second;
        for (int d = 0; d < ND; ++d)
        {
            int x = r + D[d][0], y = c + D[d][1];
            if (in(x, y, nr, nc) && board[x][y] == '*')
            {
                goto END_2;
            }
        }
        for (int d = 0; d < ND; ++d)
        {
            int x = r + D[d][0], y = c + D[d][1];
            if (!in(x, y, nr, nc) || board[x][y] == '*')
            {
                continue;
            }
            else if (visited.find(make_pair(x, y)) == visited.end())
            {
                q.push(make_pair(x, y));
                visited.insert(make_pair(x, y));
            }
        }
END_2:
        ;
    }
    return int(visited.size()) == nr * nc - m;
}
bool solve(int nr, int nc, int m, char board[][S + 10])
{
    if (m == nr * nc - 1)
    {
        for (int r = 0; r < nr; ++r)
        {
            fill(board[r], board[r] + nc, '*');
            board[r][nc] = '\0';
        }
        board[0][0] = 'c';
        return true;
    }
    for (int mask = 0; mask < (1 << (nr * nc)); ++mask)
    {
        if (__builtin_popcount(mask) != m)
        {
            continue;
        }
        for (int r = 0; r < nr; ++r)
        {
            for (int c = 0; c < nc; ++c)
            {
                if ((mask & (1 << (r * nc + c))) != 0)
                {
                    board[r][c] = '*';
                }
                else
                {
                    board[r][c] = '.';
                }
            }
            board[r][nc] = '\0';
        }
        if (bfs(board, nr, nc, m))
        {
            return true;
        }
    }
    return false;
}
int main()
{
    int tc;
    int nr, nc, m;
    char board[S][S + 10];
    scanf("%d", &tc);
    for (int cc = 1; cc <= tc; ++cc)
    {
        scanf("%d%d%d", &nr, &nc, &m);
        printf("Case #%d:\n", cc);
        if (solve(nr, nc, m, board))
        {
            for (int r = 0; r < nr; ++r)
            {
                printf("%s\n", board[r]);
            }
        }
        else
        {
            printf("Impossible\n");
        }
    }
    return 0;
}
