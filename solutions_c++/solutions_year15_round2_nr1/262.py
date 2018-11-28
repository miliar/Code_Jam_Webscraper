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

const int limit = 1e6;

int dp[limit + 5];

int main() {
#ifdef LOCAL
    freopen("inp", "r", stdin);
    //freopen("outp", "w", stdout);
#else
    // freopen(TASKNAME ".in", "r", stdin);
    // freopen(TASKNAME ".out", "w", stdout);
#endif
    fore(i, 1, limit)
        dp[i] = i;
    fore(i, 1, limit)
    {
//        printf("dp[%d] = %d\n", i, dp[i]);
        vi digits;
        int j = i;
        while(j > 0)
        {
            digits.pb(j % 10);
            j /= 10;
        }
        reverse(digits.begin(), digits.end());
        int k = 0;
        for(int d = digits.size() - 1; d >= 0; d--)
            k = k * 10 + digits[d];
    //   printf("i = %d k = %d\n", i, k);
        if (k <= limit)
        {
            if (k < i)
                assert(dp[i] + 1 >= dp[k]);
            dp[k] = min(dp[k], dp[i] + 1);
        }
        dp[i + 1] = min(dp[i + 1], dp[i] + 1);
    }
    int tests;
    scanf("%d", &tests);
    forn(test, tests)
    {
        int x;
        scanf("%d", &x);
        printf("Case #%d: %d\n", test + 1, dp[x]);
    }
}
