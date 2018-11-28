#include <cstdio>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <memory.h>
#include <sstream>
#include <complex>
#include <cassert>

#define REP(i,n) for(int i = 0, _n = (n); i < _n; i++)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)
#define FOR(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define FORD(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define FORN(i,a,b) for(int i=a;i<b;i++)
#define FOREACH(it,c) for (__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define RESET(c,x) memset (c, x, sizeof (c))

#define PI acos(-1)
#define sqr(x) ((x) * (x))
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define Aint(c) (c).begin(), (c).end()
#define SIZE(c) (c).size()

#define DEBUG(x) { cerr << #x << " = " << x << endl; }
#define PR(a,n) {cerr<<#a<<" = "; FOR(_,1,n) cerr << a[_] << ' '; cerr <<endl;}
#define PR0(a,n) {cerr<<#a<<" = ";REP(_,n) cerr << a[_] << ' '; cerr << endl;}
#define LL long long

using namespace std;

int n, k;
int a[100], res[100];
int R, C, M;
int ok;

int grid[100][100];
int clicked[100][100];

bool inside(int u, int v) {
    return (1 <= u && u <= R && 1 <= v && v <= C);
}

int cal(int u, int v) {
    int cnt = 0;
    assert(grid[u][v] == 0);
    for (int i = -1; i<= 1; i++)
        for (int j = -1; j <= 1; j++)
            if (inside(u + i, v + j))
                cnt += grid[u + i][v + j];

    return cnt;
}

void click(int u, int v) {
    if (!inside(u, v)) return;
    if (clicked[u][v]) return;
    clicked[u][v] = 1;
    assert(grid[u][v] == 0);
    int cnt = cal(u, v);

    if (cnt == 0)
        for (int i = -1; i<= 1; i++)
            for (int j = -1; j <= 1; j++)
                click(u + i, v + j);
}

void check() {
    int sum = 0;
    for (int i = 1; i <= R; i++)
        sum += a[i];
    if (sum != M) return;

    memset(grid, 0, sizeof(grid));

    for (int i = 1; i <= R; i++)
        for (int j = 1; j <= C; j++)
            grid[i][j] = (j > a[i]);

    memset(clicked, 0, sizeof(clicked));
    click(1, 1);

    for (int i = 1;i <= R; i++)
        for (int j = 1; j <= C; j++)
            if (grid[i][j] == 0 && ! clicked[i][j])
                return;

    ok = 1;
    for (int i = 1; i <= R; i++) res[i] = a[i];
}

void try_(int pos) {
    if (pos == R + 1) {
        check();
        return;
    }

    if (ok) return;

    for (int i = 0; i <= C; i++) {
        if (i == 0 && pos == 1) continue;
        a[pos] = i;
        try_(pos + 1);
    }
}

int main() {
    freopen("C-small-attempt1.in", "rb", stdin); freopen("a.out", "wb", stdout);
    int ntest;

    cin >> ntest;
    for (int test = 1; test <= ntest; test++) {
        printf("Case #%d:\n", test);
        cin >> R >> C >> M;
        M = R * C - M;

        ok = 0;
        memset(a, 0, sizeof(a));

        try_(1);

        if (!ok) printf("Impossible");
        else {
            for (int i = 1; i <= R; i++) {
                for (int j = 1; j <= C; j++)
                    if (j <= res[i]) {
                        if (i == 1 && j == 1) printf("c");
                        else printf(".");
                    } else printf("*");
                if (i < R) printf("\n");
            }
        }
        if (test < ntest) printf("\n");
    }

    return 0;
}
