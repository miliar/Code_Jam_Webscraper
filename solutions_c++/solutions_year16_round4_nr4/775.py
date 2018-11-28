#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker,"/STACK:64000000")
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>
#include <time.h>
#include <bitset>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()
#ifdef WIN32
#define dbg(...) {fprintf(stderr, __VA_ARGS__); fflush(stderr);}
#define dbgx(x) {cerr << #x << " = " << x << endl;}
#define dbgv(v) {cerr << #v << " = {"; for (typeof(v.begin()) it = v.begin(); it != v.end(); it ++) cerr << *it << ", "; cerr << "}"; cerr << endl;}
#else
#define dbg(...) { }
#define dbgx(x) { }
#define dbgv(v) { }
#endif

typedef unsigned long long ull;
typedef long long lint;
typedef pair < int , int > pii;
typedef long double ld;

const int INF = 1000 * 1000 * 1000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-9;

void prepare()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
}

const int nmax = 10;

int n, cost, best;
char f[nmax][nmax];

void read()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i ++)
    {
        scanf("%s", f[i]);
    }
}

bool usedWorker[nmax];
bool usedMachine[nmax];

bool check(int cnt)
{
    if (cnt == n)
    {
        return true;
    }

    for (int i = 0; i < n; i ++)
    {
        if (!usedWorker[i])
        {
            usedWorker[i] = true;
            bool isAny = false;

            for (int j = 0; j < n; j ++)
            {
                if (f[i][j] == '1' && !usedMachine[j])
                {
                    isAny = true;
                    usedMachine[j] = true;
                    if (!check(cnt + 1))
                    {
                        return false;
                    }
                    usedMachine[j] = false;
                }
            }

            if (!isAny)
            {
                return false;
            }

            usedWorker[i] = false;
        }
    }

    return true;
}

bool good()
{
    _(usedWorker, 0);
    _(usedMachine, 0);
    return check(0);
}

void rec(int i, int j)
{
    if (cost >= best)
        return;

    if (i == n)
    {
        if (good())
        {
            best = min(best, cost);
        }
        return;
    }
    if (j == n)
    {
        rec(i + 1, 0);
        return;
    }

    rec(i, j + 1);
    if (f[i][j] == '0')
    {
        f[i][j] = '1';
        cost++;
        rec(i, j + 1);
        cost--;
        f[i][j] = '0';
    }
}

bool solve()
{
    best = INF;
    cost = 0;
    rec(0, 0);
    printf("%d\n", best);
    return false;
}

int main()
{
    prepare();
    int t;
    scanf("%d",&t);
    for (int i = 0; i < t; i ++)
    {
        dbg("Test %d\n", i);
        printf("Case #%d: ", i + 1);
        read();
        solve();
    }
    return 0;
}
