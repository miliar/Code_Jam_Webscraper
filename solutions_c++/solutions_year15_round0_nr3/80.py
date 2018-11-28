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

#define N 10123
#define M 1012

int n, q;
ll m;
int A[N];
char S[N];

int sgn(int a) {
    if (a > 0) return 1;
    if (a < 0) return -1;
    return 0;
}

int next(int a, int b) {
    int r = (abs(a) - 1 ^ abs(b) - 1) + 1;
    r *= sgn(a);
    r *= sgn(b);
    a = abs(a);
    b = abs(b);
    int p = a + 1;
    if (p == 5) p = 2;
    if (a > 1 && b > 1 && p != b) r *= -1;
    return r;
}

int rd(char c) {
    return c - 'i' + 2;
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
        printf("Case #%d: ", ts);
        in(d, n);
        in(lld, m);
        in(s, S);
        int a = 1;
        int mm = m % 4;
        rep(k, 0, mm) {
            rep(i, 0, n)
                a = next(a, rd(S[i]));
        }
        if (a != -1) out(s, "NO");
        else {
            mm = (int)min((ll)12, m);
            a = 1;
            int p = 2;
            rep(k, 0, mm) {
                rep(i, 0, n) {
                    a = next(a, rd(S[i]));
                    if (a == p) {
                        a = 1;
                        ++p;
                    }
                }
            }
            out(s, p == 5 ? "YES" : "NO");
        }
        nl;
#ifndef XDEBUG
        cerr << ts << endl;
#endif
    }

    return 0;
}
