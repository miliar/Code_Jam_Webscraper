#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <sstream>
using namespace std;
#pragma comment(linker, "/STACK:255000000")

typedef long long ll;

#define rep(i, a, b) for(i = (a); i < (b); ++i)
#define repb(i, a, b) for(i = (a) - 1; i >= (b); --i)
#define repd(i, a, b, d) for(i = (a); i < (b); i += (d))
#define repbd(i, a, b, d) for(i = (a) - 1; i >= (b); i -= (d))
#define reps(i, s) for(i = 0; (s)[i]; ++i)
#define repl(i, l) for(i = l.begin(); i != l.end(); ++i)

#define in(f, a) scanf("%"#f, &(a))

bool firstout = 1;

#define out(f, a) printf("%"#f, (a))
#define outf(f, a) printf((firstout) ? "%"#f : " %"#f, (a)), firstout = 0
#define nl printf("\n"), firstout = 1

#define all(x) (x).begin(),(x).end()
#define sqr(x) ((x) * (x))
#define mp make_pair

template<class T>
T &minn(T &a, T b)
{
    if(b < a) a = b;
    return a;
}

template<class T>
T &maxx(T &a, T b)
{
    if(a < b) a = b;
    return a;
}

#define inf 1012345678
#define eps 1e-9


#ifdef XDEBUG
#define mod 23
#else
#define mod 1000000007
#endif

int &madd(int &a, int b)
{
    a += b;
    if(a >= mod) a -= mod;
    return a;
}

int &msub(int &a, int b)
{
    a -= b;
    if(a < 0) a += mod;
    return a;
}

int &mmult(int &a, int b)
{
    return a = (ll)a * b % mod;
}

int mdiv(ll a, ll b, ll m)
{
    a = (a % m + m) % m;
    b = (b % m + m) % m;
    if(a % b == 0) return a / b;
    return (a + m * mdiv(-a, m, b)) / b;
}

#define N 6012
#define M 1012

int sgn(ll a) {
    if (a > 0) return 1;
    if (a < 0) return -1;
    return 0;
}

struct point {
    int x, y;
    point () {}
    point (int _x, int _y) {
        x = _x;
        y = _y;
    }
    int dir() const {
        if (x == 0) return sgn(y);
        if (x > 0) return 0;
        return 2;
    }
    bool operator<(const point &p) const {
        int d1 = dir();
        int d2 = p.dir();
        if (x == 0 || d1 != d2) return d1 < d2;
        return (ll)y * p.x < (ll)p.y * x;
    }
};

int n, m, q;
point A[N];
point O[N];

int calc() {
    int i, j, k;
    sort(A, A + n);
    rep (i, 0, n) A[n + i] = A[i];
    int res = 0;
    i = j = 0;
    for (; j < n + n;) {
        ll d = (ll)A[i].x * A[j].y - (ll)A[i].y * A[j].x;
        if (d < 0 || d == 0 && (ll)A[i].x * A[j].x + (ll)A[i].y * A[j].y > 0 && i / n != j / n) ++i;
        else {
            maxx(res, j - i + 1);
            ++j;
        }
    }
    return res;
}

int main()
{
#ifdef XDEBUG
    freopen("in.txt", "rt", stdin);
#else
    freopen("x.in", "rt", stdin);
    freopen("x.out", "wt", stdout);
#endif

    int i, j, k;
    char c;
    int a, d;

    int ts;
#if 1
    int tss;
    in(d, tss);
    rep(ts, 1, tss + 1)
#else
    for(ts = 1; in(d, n) > 0; ++ts)
#endif
    {
        printf("Case #%d:", ts);
        nl;
        in(d, n);
        rep (i, 0, n) in(d, O[i].x), in(d, O[i].y);
        --n;
        rep (i, 0, n + 1) {
            k = 0;
            rep (j, 0, n + 1) if (i != j) A[k++] = point(O[j].x - O[i].x, O[j].y - O[i].y);
            int res = n - calc();
            out(d, res); nl;
        }
#ifndef XDEBUG
        cerr << ts << endl;
#endif
    }

    return 0;
}
