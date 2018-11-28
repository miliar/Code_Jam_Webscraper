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

const int primeMax = (1 << 16) + 5;

bool a[primeMax];
vector < int > primes;

void precalc()
{
    _(a, 1);
    for (int i = 2; i < primeMax; i ++)
    {
        if (a[i])
        {
            primes.pb(i);
            for (int j = i + i; j < primeMax; j += i)
            {
                a[j] = 0;
            }
        }
    }
}

vector < int > factors;

bool check(lint x, int base)
{
    lint val = 0, p = 1;
    while (x)
    {
        val += (x & 1) * p;
        x >>= 1;
        p *= base;
    }

    for (int i = 0; i < sz(primes); i ++)
    {
        if (primes[i] == val)
        {
            return false;
        }

        if (val % primes[i] == 0)
        {
            factors.pb(primes[i]);
            return true;
        }
    }

    return false;
}

bool check(lint x)
{
    if ((x & 1LL) == 0)
    {
        return false;
    }

    factors.clear();
    for (int base = 2; base <= 10; base ++)
    {
        if (!check(x, base))
        {
            return false;
        }
    }

    return true;
}

vector < pair < lint, vector < int > > > gen(int len, int cnt)
{
    lint from = (1LL << (len - 1));
    lint to = (1LL << len);
    vector < pair < lint, vector < int > > > res;

    for (lint x = from; x < to; x ++)
    {
        if (check(x))
        {
            res.pb(mp(x, factors));
            if (sz(res) == cnt)
            {
                return res;
            }
        }
    }

    return res;
}

vector < pair < lint, vector < int > > > answers[35];

void calc()
{
    for (int len = 1; len <= 32; len ++)
    {
        answers[len] = gen(len, 500);
        //cerr << len << " " << sz(answers[len]) << endl;
    }
}

int j, n;

void read()
{
    scanf("%d%d", &n, &j);
}

string toBinary(lint x)
{
    string s = "";
    while (x)
    {
        s.pb('0' + x % 2);
        x /= 2;
    }
    reverse(all(s));
    return s;
}

bool solve()
{
    printf("\n");
    for (int i = 0; i < j; i ++)
    {
        printf("%s", toBinary(answers[n][i].first).c_str());
        for (int base = 0; base < sz(answers[n][i].second); base ++)
        {
            printf(" %d", answers[n][i].second[base]);
        }
        printf("\n");
    }
    return false;
}

int main()
{
    prepare();
    precalc();
    calc();

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
