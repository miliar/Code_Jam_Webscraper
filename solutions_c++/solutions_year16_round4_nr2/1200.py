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

const int nmax = 20;

bool bit(int msk, int i)
{
    return msk & (1 << i);
}

int cntbit(int msk, int n)
{
    int ret = 0;
    for (int i = 0; i < n; i ++)
        ret += bit(msk, i);
    return ret;
}

int n, target;
double dp[nmax][nmax];
double p[nmax];
vector < double > prob;

void read()
{
    scanf("%d%d", &n, &target);
    for (int i = 0; i < n; i ++)
    {
        scanf("%lf", &p[i]);
    }
}

double calc()
{
    _(dp, 0);
    dp[0][0] = 1.0;
    for (int i = 0; i < sz(prob); i ++)
    {
        for (int j = 0; j < sz(prob); j ++)
        {
            dp[i + 1][j + 1] += dp[i][j] * prob[i];
            dp[i + 1][j] += dp[i][j] * (1.0 - prob[i]);
        }
    }
    return dp[target][target / 2];
}

bool solve()
{
    double ans = 0;
    for (int msk = 0; msk < (1 << n); msk ++)
    {
        if (cntbit(msk, n) == target)
        {
            prob.clear();
            for (int i = 0; i < n; i ++)
            {
                if (bit(msk, i))
                {
                    prob.pb(p[i]);
                }
            }
            ans = max(ans, calc());
        }
    }
    printf("%.12lf\n", ans);
    return false;
}

int main()
{
    prepare();
    int t;
    scanf("%d",&t);
    for (int i = 0; i < t; i ++)
    {
        if (i == 2)
        {
            int xx = -1;
        }

        dbg("Test %d\n", i);
        printf("Case #%d: ", i + 1);
        read();
        solve();
    }
    return 0;
}
