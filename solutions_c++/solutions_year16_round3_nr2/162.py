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

const int nmax = 55;

int f[nmax][nmax], n;
lint m, dp[nmax], cnt[nmax];

bool check()
{
    dp[n - 1] = 1;
    for (int i = n - 2; i >= 0; i --)
    {
        dp[i] = 0;
        for (int j = i + 1; j < n; j ++)
        {
            if (f[i][j])
            {
                dp[i] += dp[j];
            }
        }
    }
    return dp[0] == m;
}

void read()
{
    cin >> n >> m;
}

void build(int cntv)
{
    for (int i = 1; i < cntv; i ++)
    {
        for (int j = i + 1; j < cntv; j ++)
        {
            f[i][j] = 1;
        }
    }

    lint lft = m;
    for (int i = 1; i < cntv; i ++)
    {
        lint k = cntv - i;
        if (cnt[k] <= lft)
        {
            lft -= cnt[k];
            f[0][i] = 1;
        }
    }
}

bool solve()
{
    _(f, 0);
    cnt[0] = 0;
    cnt[1] = 1;
    cnt[2] = 1;
    for (int i = 3; i <= n; i ++)
    {
        cnt[i] = cnt[i - 1] * 2;
    }

    for (int i = 1; i <= n; i ++)
    {
        if (cnt[i] >= m)
        {
            build(i);
            for (int j = i + 1; j <= n; j++)
            {
                f[j - 2][j - 1] = 1;
            }

            assert(check());

            printf("POSSIBLE\n");
            for (int i = 0; i < n; i ++)
            {
                for (int j = 0; j < n; j ++)
                {
                    printf("%d", f[i][j]);
                }
                printf("\n");
            }

            return false;
        }
    }

    printf("IMPOSSIBLE\n");
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
