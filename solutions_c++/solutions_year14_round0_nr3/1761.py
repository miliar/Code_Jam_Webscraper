#define _CRT_SECURE_NO_WARNINGS
#include <cstdlib> 
#include <cctype> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <algorithm> 
#include <vector> 
#include <string> 
#include <iostream> 
#include <sstream> 
#include <map> 
#include <set> 
#include <queue> 
#include <stack> 
#include <fstream> 
#include <numeric> 
#include <iomanip> 
#include <bitset> 
#include <list> 
#include <stdexcept> 
#include <functional> 
#include <utility> 
#include <ctime> 
using namespace std;
template<class T> inline void checkmin(T &a, T b){ if (b<a) a = b; }//NOTES:checkmin( 
template<class T> inline void checkmax(T &a, T b){ if (b>a) a = b; }//NOTES:checkmax( 
#define SIZE(x) ((int)(x).size()) 
#define for0(i,n) for(int i=0;i<(n);i++) 
#define for1(i,n) for(int i=1;i<=(n);i++) 
#define for0r(i,n) for(int i=(n)-1;i>=0;i--) 
#define for1r(i,n) for(int i=(n);i>=1;i--) 
typedef long long ll;

int R, C, M;

char d[10][10];
int cc;

bool visited[10][10];
int vc;

int ux[8] = { -1, -1, -1, 0, 0, 1, 1, 1 };
int uy[8] = { -1, 0, 1, -1, 1, -1, 0, 1 };

bool ok(int x, int y)
{
    return x >= 0 && x < R && y >= 0 && y < C;
}

int CountMine(int x, int y)
{
    int c = 0;
    for (int k = 0; k < 8; k++)
    {
        int nx = x + ux[k];
        int ny = y + uy[k];
        if (ok(nx, ny) && d[nx][ny] == '*')c++;
    }
    return c;
}

void inner(int x, int y)
{
    visited[x][y] = true;
    vc++;
    if (CountMine(x, y) != 0)return;
    for (int k = 0; k < 8; k++)
    {
        int nx = x + ux[k];
        int ny = y + uy[k];
        if (!ok(nx, ny) || d[nx][ny] == '*' || visited[nx][ny])continue;
        inner(nx, ny);
    }
}

bool dfs(int i)
{
    if (i == R * C)
    {
        if (cc != M)return false;
        for0(x, R)for0(y, C)if (d[x][y] == '.')
        {
            memset(visited, 0, sizeof(visited));
            vc = 0;
            inner(x, y);
            if (vc == R * C - M)
            {
                d[x][y] = 'c';
                for0(a, R)puts(d[a]);
                return true;
            }
        }
        return false;
    }
    int x = i / C;
    int y = i % C;
    d[x][y] = '.';
    if (dfs(i + 1))return true;
    if (cc < M)
    {
        d[x][y] = '*';
        cc++;
        if (dfs(i + 1))return true;
        cc--;
    }
    return false;
}

void solve()
{
    scanf("%d %d %d", &R, &C, &M);
    for0(x, R)d[x][C] = '\0';
    cc = 0;
    bool result = dfs(0);
    if (!result)puts("Impossible");
}

int main()
{
    //freopen("in.txt", "r", stdin);
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
    //freopen("C-large.in", "r", stdin);
    //freopen("C-large.out", "w", stdout);
    int T, TC = 0;
    scanf("%d", &T);
    while (++TC <= T)
    {
        printf("Case #%d:\n", TC);
        solve();
    }
    return 0;
}
