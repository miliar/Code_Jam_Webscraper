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

const int nmax = 15;

int a, b, c, k, n;
int cnt[3][nmax][nmax], cntTaken, bst;
int x[1005][3];
vector < pair < int , pii > > ans;
bool used[1005];

void read()
{
    cin >> a >> b >> c >> k;
}

void add(int id)
{
    used[id] = 1;
    cnt[0][x[id][0]][x[id][1]]++;
    cnt[1][x[id][0]][x[id][2]]++;
    cnt[2][x[id][1]][x[id][2]]++;
    cntTaken++;
}

void del(int id)
{
    used[id] = 0;
    cnt[0][x[id][0]][x[id][1]]--;
    cnt[1][x[id][0]][x[id][2]]--;
    cnt[2][x[id][1]][x[id][2]]--;
    cntTaken--;
}

bool canTake(int id)
{
    return 
        cnt[0][x[id][0]][x[id][1]] < k &&
        cnt[1][x[id][0]][x[id][2]] < k &&
        cnt[2][x[id][1]][x[id][2]] < k;
}

void rec(int id)
{
    if (id == n)
    {
        if (cntTaken > bst)
        {
            bst = cntTaken;
            ans.clear();
            for (int i = 0; i < n; i ++)
            {
                if (used[i])
                {
                    ans.pb(mp(x[i][0],mp(x[i][1],x[i][2])));
                }
            }
        }
        return;
    }

    if (canTake(id))
    {
        add(id);
        rec(id + 1);
        del(id);
    }

    rec(id + 1);
}

bool solve()
{
    n = 0;
    for (int i = 0; i < a; i ++)
    {
        for (int j = 0; j < b; j ++)
        {
            for (int k = 0; k < c; k ++)
            {
                x[n][0] = i;
                x[n][1] = j;
                x[n][2] = k;
                n++;
            }
        }
    }

    cntTaken = 0;
    bst = 0;
    _(cnt, 0);
    rec(0);

    printf("%d\n", bst);
    for (int i = 0; i < sz(ans); i ++)
    {
        printf("%d %d %d\n", ans[i].first + 1, ans[i].second.first + 1, ans[i].second.second + 1);
    }

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
