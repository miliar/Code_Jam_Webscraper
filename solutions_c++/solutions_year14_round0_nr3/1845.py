// Author: Harhro94 [Harutyunyan Hrayr]
#pragma comment(linker, "/STACK:66777216")
#define _CRT_SECURE_NO_WARNINGS
#include <functional>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <cassert>
#include <iomanip>
#include <cstring>
#include <cstdio>
#include <bitset>
#include <string>
#include <vector>
#include <ctime>
#include <queue>
#include <stack>
#include <cmath>
#include <set>
#include <map>
using namespace std;

typedef long long LL;
typedef long double LD;
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()
#define sz(v) (int)(v).size()

const int dx[8] = { 1, 0, -1, 0, 1, 1, -1, -1 };
const int dy[8] = { 0, 1, 0, -1, 1, -1, 1, -1 };
bool B[5][5], used[5][5];
int R, C, M;
int op;

void open(int x, int y)
{
    ++op;
    used[x][y] = true;
    for (int d = 0; d < 8; ++d)
    {
        int tx = x + dx[d];
        int ty = y + dy[d];
        if (tx >= 0 && ty >= 0 && tx < R && ty < C && B[tx][ty]) return;
    }
    for (int d = 0; d < 8; ++d)
    {
        int tx = x + dx[d];
        int ty = y + dy[d];
        if (tx >= 0 && ty >= 0 && tx < R && ty < C && !used[tx][ty]) open(tx, ty);
    }
}

void dfs(int x, int y)
{
    used[x][y] = true;
    for (int d = 0; d < 8; ++d)
    {
        int tx = x + dx[d];
        int ty = y + dy[d];
        if (tx >= 0 && ty >= 0 && tx < R && ty < C && !B[tx][ty] && !used[tx][ty]) dfs(tx, ty);
    }
}

int main()
{
#ifdef harhro94
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#else
#define task ""
    //freopen(task".in", "r", stdin);
    //freopen(task".out", "w", stdout);
#endif

    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test)
    {
        cout << "Case #" << test << ":\n";

        cin >> R >> C >> M;

        int n = R * C;
        bool ok = false;
        int ansMask, ansx, ansy;
        for (int mask = 0; mask < (1 << n) && !ok; ++mask)
        {
            int cnt = 0;
            for (int i = 0; i < n; ++i)
                if ((mask >> i) & 1) ++cnt;
            if (cnt != M) continue;
            for (int i = 0; i < n; ++i) B[i / C][i % C] = ((mask >> i) & 1);
            memset(used, 0, sizeof used);
            cnt = 0;
            for (int i = 0; i < R && cnt < 2; ++i)
            {
                for (int j = 0; j < C && cnt < 2; ++j)
                {
                    if (!B[i][j] && !used[i][j])
                    {
                        dfs(i, j);
                        ++cnt;
                    }
                }
            }
            if (cnt != 1) continue;
            for (int i = 0; i < R && !ok; ++i)
            {
                for (int j = 0; j < C && !ok; ++j)
                {
                    if (!B[i][j])
                    {
                        memset(used, 0, sizeof used);
                        op = 0;
                        open(i, j);
                        if (op == R * C - M)
                        {
                            ok = true;
                            ansMask = mask;
                            ansx = i;
                            ansy = j;
                        }
                    }
                }
            }
        }
        if (!ok) cout << "Impossible" << endl;
        else
        {
            ok = true;
            for (int i = 0; i < n; ++i) B[i / C][i % C] = ((ansMask >> i) & 1);
            for (int i = 0; i < R; ++i)
            {
                for (int j = 0; j < C; ++j)
                {
                    if (i == ansx && j == ansy) cout << 'c';
                    else if (B[i][j]) cout << '*';
                    else cout << '.';
                }
                cout << endl;
            }
        }
    }

#ifdef harhro94
    cerr << fixed << setprecision(3) << "\nExecution time = " << clock() / 1000.0 << "s\n";
#endif
    return 0;
}