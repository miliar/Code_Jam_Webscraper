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

#define N 1012345
#define M 1012

int n, m, q;
vector<int> A[N];
int P[N];
int R[N];
int B[N];
pair<int, int> S[N];

int dfs(int i, int r) {
    R[i] = r;
    int res = 1;
    int j, k;
    rep (k, 0, A[i].size()) {
        j = A[i][k];
        if (B[j]) res += dfs(j, r);
    }
    return res;
}

int main()
{
    const rlim_t kStackSize = 63 * 1024 * 1024;   // min stack size = 16 MB
    struct rlimit rl;
    int result;

    result = getrlimit(RLIMIT_STACK, &rl);
    if (result == 0)
    {
        if (rl.rlim_cur < kStackSize)
        {
            rl.rlim_cur = kStackSize;
            result = setrlimit(RLIMIT_STACK, &rl);
            if (result != 0)
            {
                fprintf(stderr, "setrlimit returned result = %d\n", result);
            }
        }
    }

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
        in(d, n); in(d, d);
        int s, a, c, r;
        in(d, s); in(d, a); in(d, c); in(d, r);
        rep (i, 0, n) {
            S[i] = mp(s, i);
            s = ((ll)s * a + c) % r;
        }
        in(d, s); in(d, a); in(d, c); in(d, r);
        rep (i, 0, n) {
            P[i] = i == 0 ? - 1 : s % i;
            s = ((ll)s * a + c) % r;
        }
        rep (i, 0, n) A[i].clear(), B[i] = 0, R[i] = 0;
        rep (i, 1, n) A[P[i]].push_back(i);
        int res = 0;
        r = 0;
        sort (S, S + n);
        i = 0; j = 0;
        for (; j < n; ++j) {
            B[S[j].second] = 1;
            if (S[j].second == 0 || R[P[S[j].second]]) r += dfs(S[j].second, 1);
            for (; S[j].first - S[i].first > d;) {
                if (R[S[i].second]) r -= dfs(S[i].second, 0);
                B[S[i++].second] = 0;
            }
            maxx(res, r);
        }
        printf("Case #%d: ", ts);
        out(d, res); nl;

#ifndef XDEBUG
        cerr << ts << endl;
#endif
    }

    return 0;
}
