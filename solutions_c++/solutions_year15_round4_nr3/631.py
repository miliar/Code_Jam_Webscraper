#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <vector>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <deque>
#include <cassert>
#include <unordered_map>

using namespace std;

#ifdef WIN32
    #define I64 "%I64d"
#else
    #define I64 "%lld"
#endif

typedef long long ll;

#define f first
#define s second
#define mp make_pair
#define pb push_back
#define all(s) s.begin(), s.end()
#define sz(s) (int(s.size()))
#define fname "a"
#define ms(a,x) memset(a, x, sizeof(a))
#define forit(it,s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); ++it)
#define MAXN 22
#define MAXL 1000001

int n;
unordered_map <string, int> m;
int k;
vector <int> a[MAXN];
string t;
char c[MAXL];
int d[MAXL];
int mark[MAXL];
int cc;

inline int get()
{
    if (m.find(t) == m.end()) return m[t] = k++;
    return m[t];
}

inline void solve()
{
    m.clear();
    k = 0;

    scanf("%d\n", &n);
    for (int i = 0; i < n; ++i)
    {
        gets(c);
        t = "";
        int l = strlen(c);
        a[i].clear();
        for (int j = 0; j < l; ++j)
        {
            if (c[j] != ' ') t += c[j];
            if (c[j] == ' ' || j + 1 == l)
            {
                a[i].pb(get());
                t = "";
            }
        }
    }

    int ans = int(1e6);
    for (int mask = 0; mask < (1 << n); ++mask)
    {
        if ((mask & 1) || !((mask >> 1) & 1)) continue;
        ++cc;
        int tt = 0;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < sz(a[i]); ++j)
            {
                if (mark[a[i][j]] != cc)
                {
                    mark[a[i][j]] = cc;
                    d[a[i][j]] = 0;
                }
                if (d[a[i][j]] == 3) continue;
                d[a[i][j]] |= (1 << ((mask >> i) & 1));
                if (d[a[i][j]] == 3) ++tt;
            }
        ans = min(ans, tt);
    }
    printf("%d\n", ans);
}

int main()
{
    #ifdef LOCAL
    freopen(fname".in", "r", stdin);
    freopen(fname".out", "w", stdout);
    #endif

    int tt;
    scanf("%d", &tt);
    for (int t = 0; t < tt; ++t)
    {
        printf("Case #%d: ", t + 1);
        solve();
    }
    return 0;
}
