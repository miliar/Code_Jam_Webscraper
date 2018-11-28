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

bool isFirstWin(char x, char y)
{
    return 
        x == 'R' && y == 'S' ||
        x == 'S' && y == 'P' ||
        x == 'P' && y == 'R';
}

bool isTie(char x, char y)
{
    return x == y;
}

string alpha = "RPS";
int cnt[3], n;
string perm, best;
string cur, nxt;

void read()
{
    scanf("%d%d%d%d", &n, &cnt[0], &cnt[1], &cnt[2]);
}

bool good()
{
    cur = perm;
    for (int i = 0; i < n; i ++)
    {
        nxt = "";
        for (int j = 0; j < sz(cur); j += 2)
        {
            char x = cur[j];
            char y = cur[j + 1];
            if (isTie(x, y))
            {
                return false;
            }

            if (isFirstWin(x, y))
            {
                nxt.pb(x);
            }
            else
            {
                nxt.pb(y);
            }
        }
        cur = nxt;
    }
    return true;
}

bool solve()
{
    best = "";
    perm.clear();
    for (int i = 0; i < 3; i ++)
    {
        for (int j = 0; j < cnt[i]; j ++)
        {
            perm.pb(alpha[i]);
        }
    }
    sort(all(perm));

    do{
        if (good() && (best == "" || best > perm))
        {
            best = perm;
        }
    }while (next_permutation(all(perm)));

    if (best == "")
    {
        best = "IMPOSSIBLE";
    }

    printf("%s\n", best.c_str());

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
