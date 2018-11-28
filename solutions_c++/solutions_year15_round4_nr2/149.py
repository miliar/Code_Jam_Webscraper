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

#define N 1012
#define M 1012

int n, m, q;
pair<double, double> A[N];

int main()
{
#ifdef XDEBUG
    freopen("in.txt", "rt", stdin);
#else
    freopen("b.in", "rt", stdin);
    freopen("b.out", "wt", stdout);
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
        double p, pp;
        in(lf, pp); in(lf, p);
        rep (i, 0, n) in(lf, A[i].second), in(lf, A[i].first);
        sort (A, A + n);
        if (A[0].first > p + eps || A[n - 1].first < p - eps) out(s, "IMPOSSIBLE"), nl;
        else {
            double c = A[0].first;
            double r = A[0].second;
            rep (i, 1, n) {
                double cc = (c * r + A[i].first * A[i].second) / (r + A[i].second), rr = r + A[i].second;
                if (cc > p + eps) {
                    rr = (p - c) / (A[i].first - c);
                    double rx = (p - A[i].first) / (c - A[i].first);
                    rr *= r / rx;
                    if (rr >= 0.) r += rr;
                    else out(s, "ooopppsss"), nl;
                    out(.8lf, pp / r); nl; break;
                }
                c = cc;
                r = rr;
            }
            if (i == n) {
                if (abs(c - p) < eps) {
                    out(.8lf, pp / r); nl;
                } else {
                    reverse (A, A + n);
                    c = A[0].first;
                    r = A[0].second;
                    rep (i, 1, n) {
                        double cc = (c * r + A[i].first * A[i].second) / (r + A[i].second), rr = r + A[i].second;
                        if (cc < p - eps) {
                            rr = (p - c) / (A[i].first - c);
                            double rx = (p - A[i].first) / (c - A[i].first);
                            rr *= r / rx;
                            if (rr >= 0.) r += rr;
                            else out(s, "ooopppsss"), nl;
                            out(.8lf, pp / r); nl; break;
                        }
                        c = cc;
                        r = rr;
                    }
                    if (i == n) out(s, "ooopsss"), nl;
                }
            }
        }

#ifndef XDEBUG
        cerr << ts << endl;
#endif
    }

    return 0;
}
