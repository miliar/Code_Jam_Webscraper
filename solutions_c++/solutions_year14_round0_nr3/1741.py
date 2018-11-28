#pragma comment(linker, "/STACK:512000000")
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

typedef long double ld;
typedef long long ll;
typedef pair<int, int> pii;

#define NMAX 55

int n, m, k;
char a[NMAX][NMAX];
int ty[NMAX][NMAX];
bool used[NMAX][NMAX];

int dx[8] = {1, 0, -1, 0, 1, 1, -1, -1};
int dy[8] = {0, 1, 0, -1, 1, -1, 1, -1};

bool valid(int x, int y)
{
    return (x >= 0 && x < n && y >= 0 && y < m);
}

void dfs(int x, int y)
{
    if (used[x][y]) return;
	used[x][y] = true;

    forn(k, 8)
    {
        int xx = x + dx[k];
        int yy = y + dy[k];
        if (valid(xx, yy) && ty[xx][yy] == 0) dfs(xx, yy);
    }
}
bool good(int mask)
{
    int cnt = 0;
    int sum = 0;
    forn(i, n)
    {
        forn(j, m)
        {
            if (mask & (1 << cnt)) 
            {
                sum++;
                a[i][j] = '*';
            }
            else a[i][j] = '.';
            cnt++;                
        }
    }

    if (sum != k) return false;

    forn(i, n)
    {
        forn(j, m)
        {            
            if (a[i][j] == '*')
            {
                ty[i][j] = 2;
                continue;
            }
            ty[i][j] = 0;
            forn(k, 8)
            {
                int x = i + dx[k];
                int y = j + dy[k];
                if (valid(x, y) && a[x][y] == '*') ty[i][j] = 1;    
            }
                
        }
    }

    if (n * m - sum == 1)
    {
        forn(i, n)
        {
            forn(j, m)
            {
                if (a[i][j] == '.') a[i][j] = 'c';
            }
        }
        return true;
    }

    int cx = -1, cy = -1;
    forn(i, n)
    {
        forn(j, m)
        {
            if (ty[i][j] == 0)
            {
                cx = i;
                cy = j;
            }
        }
    }

    if (cx == -1) return false;

    memset(used, 0, sizeof(used));

    a[cx][cy] = 'c';
    dfs(cx, cy);

    forn(i, n)
    {
        forn(j, m)
        {
            if (ty[i][j] < 2)
            {
                bool ok = used[i][j];
                forn(k, 8)
                {
                    int x = i + dx[k];
                    int y = j + dy[k];
                    if (valid(x, y) && used[x][y]) 
                    {
                        ok = true;
                        break;
                     }
                }
                if (!ok) return false;
            }
        }
    }

    return true;
}

void solve(int test)
{
    printf("Case #%d:\n", test);
    cerr << test << endl;

    cin >> n >> m >> k;

    forn(mask, (1 << (n * m)))
    {
        if (good(mask))
        {
            forn(i, n)
            {
                forn(j, m)
                {
                    cout << a[i][j];
                }
                cout << endl;
            }
            return;
        }
    }

    cout << "Impossible\n";
}
int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);

    int tc;
    scanf("%d\n", &tc);
    forn(it, tc) solve(it + 1);
    
    return 0;
}
