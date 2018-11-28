#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <cmath>
#include <cassert>
#include <cstdio>
#include <ctime>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <queue>
#include <deque>
#include <algorithm>
#include <stack>
#include <string.h>

using namespace std;

#define mp make_pair
#define pb push_back
#define all(v) v.begin(), v.end()

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define for1(i, n) for (int i = 1; i <= (int)(n); i++)
#define forv(i, v) forn(i, v.size())

typedef pair<int, int> pii;
typedef long long ll;

#define NMAX 20
#define INF 1000000009

int n, m, p;
int x[NMAX], y[NMAX], low[NMAX], up[NMAX], w[NMAX];
vector<int> g[NMAX], gt[NMAX];
int d1[NMAX], d2[NMAX];
bool used[NMAX];

void go1()
{
    memset(used, 0, sizeof(used));
    forn(i, n) d1[i] = INF;
    d1[0] = 0;
    forn(it, n - 1)
    {
        int k = -1;
        forn(i, n) if (!used[i] && (k == -1 || d1[i] < d1[k])) k = i;
        if (d1[k] == INF) break;
		used[k] = true;

        forv(j, g[k])
        {
            int c = w[g[k][j]];
            int i = y[g[k][j]];
            if (!used[i] && d1[i] > d1[k] + c)
            {
                d1[i] = d1[k] + c;
            }
        }
    }
}

void go2()
{
    memset(used, 0, sizeof(used));
    forn(i, n) d2[i] = INF;
    d2[1] = 0;
    forn(it, n - 1)
    {
        int k = -1;
        forn(i, n) if (!used[i] && (k == -1 || d2[i] < d2[k])) k = i;
        if (d2[k] == INF) break;
		used[k] = true;

        forv(j, gt[k])
        {
            int c = w[gt[k][j]];
            int i = x[gt[k][j]];
            if (!used[i] && d2[i] > d2[k] + c)
            {
                d2[i] = d2[k] + c;
            }
        }
    }
}


void solve(int tc)
{
    cerr << tc << endl;
    printf("Case #%d: ", tc);
    cin >> n >> m >> p;
    forn(i, n) 
    {
        g[i].clear();
        gt[i].clear();
    }
    forn(i, m)
    {
        cin >> x[i] >> y[i] >> low[i] >> up[i];
        --x[i];
        --y[i];
        g[x[i]].pb(i);
        gt[y[i]].pb(i);
    }
    vector<int> path(p);
    forn(i, p)
    {
        cin >> path[i];
        path[i]--;  
    }
    vector<bool> good(p, false);
    forn(mask, (1 << m))
    {
        forn(i, m)
        {
            if (mask & (1 << i))
            {
                w[i] = up[i];
            }
            else
            {
                w[i] = low[i];
            }
        }
        go1();
        go2();

        forv(i, path)
        {
            int id = path[i];

            if (d1[x[id]] + w[id] == d1[y[id]] &&
                d2[y[id]] + w[id] == d2[x[id]])
                {
                    good[i] = true;
                }    
                else break;

        }    
    }

    int k = 0;
    while (k < p && good[k]) k++;

    if (k == p) cout << "Looks Good To Me\n"; else cout << path[k] + 1 << endl;
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int tc;
    cin >> tc;
    forn(it, tc) solve(it + 1);
    return 0;
}
