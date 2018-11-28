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

int main() {
#ifdef LOCAL
    freopen("inp", "r", stdin);
    //freopen("outp", "w", stdout);
#else
    // freopen(TASKNAME ".in", "r", stdin);
    // freopen(TASKNAME ".out", "w", stdout);
#endif
    int tests;
    scanf("%d", &tests);
    forn(test, tests)
    {
        int gr;
        scanf("%d", &gr);
        vector <pii> list;
        forn(j, gr)
        {
            int d, h, m;
            scanf("%d%d%d", &d, &h, &m);
            assert(h <= 2);
            fore(j, m, m + h - 1)
                list.pb(mp(360 - d, j));
        }
        int ans;
        if (list.size() <= 1)
        {
            ans = 0;
        }
        else if (list.size() == 2)
        {
            pii first = list[0];
            pii second = list[1];
            if (first.first < second.first || (first.first == second.first && first.se < second.se))
                swap(first, second);
            if (first.second >= second.second)
            {
                i64 t1 = (i64)first.first * first.second;
                i64 t2 = (i64)(second.first + 360) * second.second;
                if (t1 < t2)
                    ans = 0;
                else ans = 1;
            }
            else
            {
                i64 t3 = (i64)(first.first + 360) * first.second;
                i64 t4 = (i64)second.first * second.second;
                if (t3 > t4)
                    ans = 0;
                else ans = 1;
            }
        }
        else assert(false);
        printf("Case #%d: %d\n", test + 1, ans);
    }
}
