#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <queue>
#include <vector>
using namespace std;

const int Maxn = 105;
int board[Maxn][Maxn];
int n, m;
int col[Maxn], row[Maxn];
bool check(int k)
{
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < m; ++j)
            if (board[i][j] == k)
            {
                if (col[j] <= k || row[i] <= k) continue;
                return false;
            }
    }
    return true;
}
int main()
{
   // freopen("in.txt", "r", stdin);
   // freopen("small.in", "r", stdin);
   // freopen("small.out", "w", stdout);
    freopen("large.in", "r", stdin);
    freopen("large.out", "w", stdout);
    int T;scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas)
    {
        printf("Case #%d: ", cas);
        scanf ("%d%d", &n, &m);
        int small = 100, large = 1;
        for (int i = 0; i < n; ++i)
        {
            row[i] = 1;
            for (int j = 0; j < m; ++j)
            {
                scanf("%d", &board[i][j]);
                row[i] = max(row[i], board[i][j]);
                small = min(small, board[i][j]);
                large = max(large, board[i][j]);
            }
        }
        for (int j = 0; j < m; ++j)
        {
            col[j] = 1;
            for (int i = 0; i < n; ++i)
                col[j] = max(col[j], board[i][j]);
        }
        bool ok = true;
        for (int k = large; k >= small; --k)
        {
            if (check(k) == false)
            {
                ok = false;
                break;
            }
        }
        if (ok) printf("YES\n");
        else printf("NO\n");

    }


    return 0;
}
