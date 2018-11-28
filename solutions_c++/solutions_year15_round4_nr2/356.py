#include <bits/stdc++.h>

using namespace std;

#define sz(x) ((int) (x).size())
#define forn(i,n) for (int i = 0; i < int(n); ++i)
#define forab(i,a,b) for (int i = int(a); i < int(b); ++i)

typedef long long ll;
typedef long double ld;

const int INF = 1000001000;
const ll INFL = 2000000000000001000;
int solve();


int main()
{
    srand(2317);
    cout.precision(10);
    cout.setf(ios::fixed);
    #ifdef LOCAL
    freopen("b.in", "r", stdin);
    #else
    #endif
    int tn = 1;
    cin >> tn;
    for (int i = 0; i < tn; ++i)
        solve();
    #ifdef LOCAL
    cerr << "Time: " << double(clock()) / CLOCKS_PER_SEC << '\n';
    #endif
}

const int maxn = 200;

bool eq(ld a, ld b)
{
    return fabsl(a - b) < 1e-10;
}

bool lower(ld a, ld b)
{
    return b - a > 1e-10;
}


ld c[maxn];
ld r[maxn];

int test = 1;

int solve()
{
    int n;
    ld V, X;
    cin >> n >> V >> X;
    forn (i, n)
        cin >> r[i] >> c[i];
    if (n == 2 && eq(c[0], c[1]))
        r[0] += r[1], n = 1;
    if (n == 1)
    {
        if (eq(c[0], X))
            printf("Case #%d: %.10Lf\n", test++, V / r[0]);
        else
            printf("Case #%d: IMPOSSIBLE\n", test++);
        return 0;
    }
    if (n == 2)
    {
        if (lower(X, c[0]) && lower(X, c[1]))
        {
            printf("Case #%d: IMPOSSIBLE\n", test++);
            return 0;
        }
        if (lower(c[0], X) && lower(c[1], X))
        {
            printf("Case #%d: IMPOSSIBLE\n", test++);
            return 0;
        }
        ld v1 = (X * V - c[1] * V) / (c[0] - c[1]);
        ld v2 = V - v1;
        printf("Case #%d: %.10Lf\n", test++, max(v1 / r[0], v2 / r[1]));
        return 0;
    }
    assert(false);
    return 0;
}
