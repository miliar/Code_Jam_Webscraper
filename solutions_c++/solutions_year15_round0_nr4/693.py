#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <algorithm>
#include <map>
#include <queue>
#include <stack>
using namespace std;

int di[] = {-1, 0, 1, 0}, dj[] = {0, 1, 0, -1};

int x, r, c;

bool used[22][22];

int dfs(int i, int j)
{
    used[i][j] = true;
    int sz = 1;
    for(int k = 0; k < 4; k++)
    {
        int ii = i + di[k], jj = j + dj[k];
        if(0 <= ii and ii < r and 0 <= jj and jj < c and !used[ii][jj]) sz += dfs(ii, jj);
    }
    return sz;
}

bool ok()
{
    for(int i = 0; i < r; i++) for(int j = 0; j < c; j++) if(!used[i][j])
    {
        int sz = dfs(i, j);
        if(sz % x != 0) return false;
    }
    return true;
}

bool can(int l1, int l2, int xi, int xj)
{
    //cout << l1 << " " << l2 << endl;

    for(int si = 0; si + l2 <= r; si++) for(int sj = 0; sj + l1 <= c; sj++)
    {
        memset(used, 0, sizeof(used));
        for(int i = 0; i < l2; i++) used[i + si][xj + sj] = 1;
        for(int j = 0; j < l1; j++) used[xi + si][j + sj] = 1;

        /*cout << "1:" << endl;
        for(int i = 0; i < r; i++)
        {
            for(int j = 0; j < c; j++) cout << int(used[i][j]);
            cout << endl;
        }cout << endl;*/

        if(ok()) return true;
    }
    for(int si = 0; si + l1 <= r; si++) for(int sj = 0; sj + l2 <= c; sj++)
    {
        memset(used, 0, sizeof(used));
        for(int i = 0; i < l1; i++) used[i + si][xi + sj] = 1;
        for(int j = 0; j < l2; j++) used[xj + si][j + sj] = 1;

        /*cout << "2:" << endl;
        for(int i = 0; i < r; i++)
        {
            for(int j = 0; j < c; j++) cout << int(used[i][j]);
            cout << endl;
        }cout << endl;*/

        if(ok()) return true;
    }
    return false;
}

bool solve()
{
    if((r * c) % x != 0) return true;

    int m = min(r, c);
    int M = max(r, c);

    if(x > M) return true;
    if(m < M and x >= m * 2 + 1) return true;
    if(m == M and x >= m * 2) return true;

    for(int l1 = 1; l1 < x; l1++)
    {
        for(int j = 0; j < l1; j++) for(int i = 0; i < x + 1 - l1; i++)
        {
            //printf("%d %d (%d,%d)\n", l1, x + 1 - l1, i, j);
            if(!can(l1, x + 1 - l1, i, j)) return true;
        }
    }

    return false;
}

int main()
{
    freopen("d1_1.in", "r", stdin);
    freopen("d1_1.out", "w", stdout);
    int testcnt;
    cin >> testcnt;
    for(int i = 1; i <= testcnt; i++)
    {
        cin >> x >> r >> c;
        bool ans = solve();
        printf("Case #%d: ", i);
        cout << (ans ? "RICHARD" : "GABRIEL") << endl;
    }
}
