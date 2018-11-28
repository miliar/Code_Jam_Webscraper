#include <iostream>
#include <fstream>
#include <cstdio>
#include <sstream>
#include <string>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <numeric>
#include <utility>
#include <functional>
#include <iomanip>
#include <cstring>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
#define FOR(i, a, b) for(int i = (a); i < (b); i++)
#define TR(i, a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)

int r, c, m;
char g[55][55];

bool solve()
{
    int no = r * c - m;
    FOR(i, 0, r) FOR(j, 0, c) g[i][j] = '.';
    g[0][0] = 'c';
    if(m == 0) return true;
    if(r == 1 or c == 1)
    {
        if(r == 1) FOR(i, 0, m) g[0][c - 1 - i] = '*';
        else FOR(i, 0, m) g[r - 1 - i][0] = '*';
        return true;
    }
    if(r == 2 or c == 2)
    {
        if(r == 2) FOR(i, 0, m / 2) g[0][c - 1 - i] = g[1][c - 1 - i] = '*';
        else FOR(i, 0, m / 2) g[r - 1 - i][0] = g[r - 1 - i][1] = '*';
        if(no == 1)
        {
            if(r == 2) g[1][0] = '*';
            else g[0][1] = '*';
            return true;
        }
        if(m % 2 == 1) return false;

    }
    if(no == 2 or no == 3 or no == 5 or no == 7) return false;
    FOR(i, 0, r - 2)
    {
        if(m >= c)
        {
            FOR(j, 0, c) g[r - 1 - i][j] = '*';
            m -= c;
        }
        else
        {
            FOR(j, 0, m) g[r - 1 - i][j] = '*';
            if(m == c - 1)
            {
                if(i < r - 3)
                {
                    g[r - 1 - i][c - 2] = '.';
                    g[r - 2 - i][0] = '*';
                }
                else
                {
                    g[0][c - 1] = g[1][c - 1] = g[2][c - 1] = '*';
                    g[2][0] = g[2][1] = g[2][2] = '.';
                }
            }
            return true;
        }
    }
    int ind = c - 1;
    FOR(j, 0, m / 2)
    {
        g[0][ind] = g[1][ind] = '*';
        ind--;
    }
    if(m % 2 == 1)
    {
        if(ind == 0) g[1][0] = '*';
        else
        {
            g[2][0] = g[2][1] = g[2][2] = '.';
            g[0][ind] = g[1][ind] = g[0][ind - 1] = g[1][ind - 1] = '*';
        }
    }
    return true;
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int t;
    cin >> t;
    FOR(ti, 1, t + 1)
    {
        cin >> r >> c >> m;
        printf("Case #%d:\n", ti);
        if(solve())
        {
            FOR(i, 0, r)
            {
                FOR(j, 0, c) cout << g[i][j];
                cout << endl;
            }
        }
        else cout << "Impossible" << endl;
    }
}

