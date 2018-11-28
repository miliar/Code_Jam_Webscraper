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

const int nmax = 105;

char buf[nmax];
string init, s;
map < string , int > d;
queue < string > q;
int n;

char flipChar(char c)
{
    if (c == '+')
        return '-';
    else
        return '+';
}

bool canFlip(string &s, int prefix)
{
    for (int i = 0; i < prefix; i ++)
    {
        if (s[i] == s[prefix - i - 1])
        {
            return true;
        }
    }
    return false;
}

string flip(string &s, int prefix)
{
    string t = s;
    for (int i = 0; i < prefix; i ++)
    {
        t[i] = flipChar(s[prefix - i - 1]);
    }
    return t;
}

bool isGood(string &s)
{
    for (int i = 0; i < n; i ++)
    {
        if (s[i] == '-')
        {
            return false;
        }
    }
    return true;
}

void upd(string &s, int val)
{
    if (d.count(s) == 0)
    {
        d[s] = val;
        q.push(s);
    }
}

void read()
{
    scanf("%s", buf);
    n = strlen(buf);
    init = buf;
}

void gen()
{
    n = 100;
    init = "";
    for (int i = 0; i < n; i ++)
    {
        char c = rand() & 1 ? '+' : '-';
        init.pb(c);
    }
}

bool solve()
{
    d.clear();
    while (!q.empty())
    {
        q.pop();
    }

    upd(init, 0);

    while (!q.empty())
    {
        s = q.front();
        q.pop();
        int cur = d[s];

        if (isGood(s))
        {
            printf("%d\n", cur);
            return false;
        }

        int lastMinus = n - 1;
        while (s[lastMinus] != '-')
        {
            lastMinus--;
        }

        bool flipped = 0;
        for (int i = lastMinus; i >= 0; i --)
        {
            if (canFlip(s, i + 1))
            {
                upd(flip(s, i + 1), cur + 1);
            }
        }
    }

    throw 42;

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
