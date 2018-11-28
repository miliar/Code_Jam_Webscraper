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

#define NMAX 505
#define WMAX 105

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int a[WMAX][NMAX];
int w, h, b;
int c[WMAX][NMAX][4], cc[WMAX][NMAX];
int f[WMAX][NMAX][4], fc[WMAX][NMAX];
int invf[WMAX][NMAX][4], invfc[WMAX][NMAX];


bool valid(int x, int y)
{
    return x >= 0 && x < w && y >= 0 && y < h;
}

int prv[WMAX][NMAX][2];
bool used[WMAX][NMAX][2];

void make_flow(int vx, int vy, int vt)
{
    while (vy != 0)
    {

        if (prv[vx][vy][vt] == -1)
        {
            if (vt == 1)
            {
                invfc[vx][vy]--;
                fc[vx][vy]++;
                vt = 0;
            }
            else
            {
                fc[vx][vy]--;
                invfc[vx][vy]++;
                vt = 1;
            }
        }
        else
        {
            int k = prv[vx][vy][vt];
            int ux = vx + dx[k];
            int uy = vy + dy[k];

            if (vt == 0)
            {
                f[ux][uy][k^2]++;
                invf[vx][vy][k]--;
                vt = 1;
            }
            else
            {
                invf[ux][uy][k^2]--;
                f[vx][vy][k]++;
                vt = 0;
            }
            vx = ux; vy = uy;
        }
    }
}
bool bfs()
{
    queue<int> qx, qy, qt;
    
    memset(prv, -1, sizeof(prv));
    memset(used, 0, sizeof(used));

    forn(i, w)
    {
        qx.push(i);
        qy.push(0);
        qt.push(1);
        used[i][0][1] = true;
    }


    while (!qx.empty())
    {
        int ux = qx.front(); qx.pop();        
        int uy = qy.front(); qy.pop();        
        int ut = qt.front(); qt.pop();

        if (uy == h - 1)
        {
            make_flow(ux, uy, ut);
            return true;
        }

        if (ut == 1)
        {
            forn(k, 4)
            {
                int vx = ux + dx[k];
                int vy = uy + dy[k];

                if (f[ux][uy][k] < c[ux][uy][k] && !used[vx][vy][0])
                {
                    used[vx][vy][0] = true;
                    prv[vx][vy][0] = (k + 2) & 3;
                    qx.push(vx); qy.push(vy); qt.push(0);                                            
                }
            }

            if (invfc[ux][uy] < 0 && !used[ux][uy][0])
            {
                used[ux][uy][0] = true;
                qx.push(ux); qy.push(uy); qt.push(0);                                              
            }
        }
        else
        {
            if (fc[ux][uy] < cc[ux][uy] && !used[ux][uy][1])
            {
                used[ux][uy][1] = true;
                qx.push(ux); qy.push(uy); qt.push(1);                
            }

            forn(k, 4)
            {
                int vx = ux + dx[k];
                int vy = uy + dy[k];

                if (invf[ux][uy][k] < 0 && !used[vx][vy][1])
                {
                    used[vx][vy][1] = true;
                    prv[vx][vy][1] = (k + 2) & 3;
                    qx.push(vx); qy.push(vy); qt.push(1);                                            
                }
            }
        }
    }
    return false;
}
void solve(int test)
{
    printf("Case #%d: ", test);
    cerr << "Case #" << test << endl;

    scanf("%d %d %d", &w, &h, &b);
    memset(a, 0, sizeof(a));

    forn(i, b)
    {
        int x0, y0, x1, y1;
        scanf("%d %d %d %d", &x0, &y0, &x1, &y1);

        for (int x = x0; x <= x1; x++)
            for (int y = y0; y <= y1; y++)
                a[x][y] = 1;
    }

    memset(f, 0, sizeof(f));
    memset(fc, 0, sizeof(fc));
    memset(invf, 0, sizeof(invf));
    memset(invfc, 0, sizeof(invfc));
    memset(c, 0, sizeof(c));
    memset(cc, 0, sizeof(cc));

    forn(i, w)
    {
        forn(j, h)
        {
            forn(k, 4)
            {
                int x = i + dx[k];
                int y = j + dy[k];
                if (valid(x, y) && a[x][y] == 0 && a[i][j] == 0)
                {
                    c[i][j][k] = 1;
                }
            }
            if (a[i][j] == 0) cc[i][j] = 1;
        }
    }

    int flow = 0;        
    while(bfs()) flow++;
    cout << flow << endl;
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
