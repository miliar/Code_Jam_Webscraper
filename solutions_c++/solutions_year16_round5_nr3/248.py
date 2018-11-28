#define FNAME ""

#include <bits/stdc++.h>

#define hash padjf9srpi
#define y0 sdkfaslhagaklsldk
#define y1 aasdfasdfasdf
#define yn askfhwqriuperikldjk
#define j1 assdgsdgasghsf
#define tm sdfjahlfasfh
#define lr asgasgash
#define pb push_back
#define mp make_pair
#define forn(i, n) for (int i = 0; i < (n); i++)
#define fornr(i, n) for (int i = (n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (a); i < (b); i++)
#define gcd __gcd
#define all(a) (a).begin(), (a).end()
 
#ifdef _WIN32
    #define I64 "%I64d"
#else
    #define I64 "%lld"
#endif

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef pair <int, int> pii;
typedef vector <int> vi;

template <class T> T sqr(const T &a) {return a * a;}

const int MAXN = 1e3;

int used[MAXN], x[MAXN], y[MAXN], z[MAXN], T, n, s;

void dfs(int v, double r) {
    used[v] = 1;
    forn(i, n) {
        if (!used[i] && sqr(x[v] - x[i]) + sqr(y[v] - y[i]) + sqr(z[v] - z[i]) <= r * r)
            dfs(i, r);
    }
}

int main()
{
#ifdef LOCAL
    freopen(FNAME".in", "r", stdin);
    freopen(FNAME".out", "w", stdout);
#endif
    scanf("%d", &T);
    forn(qqq, T) {
        scanf("%d%d", &n, &s);
        forn(i, n) {
            scanf("%d%d%d", &x[i], &y[i], &z[i]);
            int tmp;
            forn(j, 3)
                scanf("%d", &tmp);
        }
        double l = 0, r = 1e9;
        forn(it, 200) {
            double m = (l + r) / 2;
            forn(i, n)
                used[i] = 0;
            dfs(0, m);
            if (used[1])
                r = m;
            else
                l = m;
        }
        printf("Case #%d: %.10f\n", qqq + 1, l);
    }
}

