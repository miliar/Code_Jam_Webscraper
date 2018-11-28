#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
#include <cmath>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdlib>

using namespace std;

#define INF 1e+9
#define mp make_pair
#define pb push_back
#define fi first
#define fs first
#define se second
#define i64 long long
#define li long long
#define lint long long
#define pii pair<int, int>
#define vi vector<int>

#define forn(i, n) for (int i = 0; i < (int)n; i++)
#define fore(i, b, e) for (int i = (int)b; i <= (int)e; i++)

const int maxn = 1005;

int a[maxn];

int main() {
#ifdef LOCAL
    freopen("inp", "r", stdin);
    freopen("outp", "w", stdout);
#else
    // freopen(TASKNAME ".in", "r", stdin);
    // freopen(TASKNAME ".out", "w", stdout);
#endif
    int T;
    scanf("%d", &T);
    forn(test, T)
    {
        int n;
        scanf("%d", &n);
        int maxx = 0;
        forn(i, n)
        {
            scanf("%d", &a[i]);
            maxx = max(maxx, a[i]);
        }
        int ans = 1e9;
        fore(bound, 1, maxx)
        {
            int nnew = bound;
            forn(i, n) if (a[i] > bound)
            {
                int tmp = (a[i] % bound == 0 ? a[i] / bound - 1 : a[i] / bound);
                nnew += tmp;
            }
            ans = min(ans, nnew);
                
        }
        printf("Case #%d: %d\n", test + 1, ans);
    }
}
