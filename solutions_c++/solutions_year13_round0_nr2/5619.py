#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

#define ALL(v) (v).begin(), (v).end()
#define RALL(v) (v).rbegin(), (v).rend()
#define SZ(v) ((int)(v).size())
#define FOR(i, a, b) for (typeof(a) i = (a); i < (b); ++i)
#define FORD(i, a, b) for(typeof(a) i = (a);i >= (b); --i)
#define FOREACH(iter, v) for (typeof((v).begin()) iter = (v).begin(); iter != (v).end(); ++iter)
#define REP(i, n) FOR(i, 0, n)

using namespace std;

#define SMALL 1

int main()
{

#if SMALL
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small.out", "w", stdout);
#else
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
#endif


    int n, m, T, a[12][12];
    scanf("%d", &T);
    for (int tc = 1; tc <= T; ++tc) {
        scanf("%d%d", &n, &m);
        REP(i,n) REP(j,m) scanf("%d", &a[i][j]);
        bool res = true;
        REP(i,n) REP(j,m) {
            bool can = false;
            if (a[i][j] == 1) {
                int k;
                for (k = 0; k < m; ++k) if (a[i][k] == 2) break;
                can |= (k == m);
                if (can) continue;
                k = 0;
                for (; k < n; ++k) if (a[k][j] == 2) break;
                can |= (k == n);
                if (!can) {
                    res = false;
                    goto output;
                }
            }
        }
    output:
        printf("Case #%d: %s\n", tc, res ? "YES" : "NO");
    }

    return 0;
}
