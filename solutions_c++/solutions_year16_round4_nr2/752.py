#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

int popcount[139000];
int n, k;
ld pr12[139000];
ld pr1[139000], pr2[139000];
ld p[999];

int main()
{
    //freopen("B-small-attempt1.in", "r", stdin);
    //freopen("B-small-attempt1.out", "w", stdout);

    for (int i = 0; i < 139000; ++i) popcount[i] = __builtin_popcount(i);

    int t;
    cin >> t;
    for (int ttt = 1; ttt <= t; ++ttt) {
        cin >> n >> k;
        for (int i = 0; i < n; ++i) cin >> p[i];
        for (int mask = (1 << n) - 1; mask >= 0; --mask) {
            pr12[mask] = 0;
            int qqq = mask;
            ld ans1 = 1, ans2 = 1;
            for (int j = 0; j < n; ++j) {
                if (qqq & 1) {
                    ans1 *= p[j];
                    ans2 *= 1 - p[j];
                }
                qqq >>= 1;
            }
            pr1[mask] = ans1;
            pr2[mask] = ans2;
        }
        ld ans = 0;
        for (int mask = (1 << n) - 1; mask >= 0; --mask) {
            if (popcount[mask] != k / 2) continue;
            int mask2 = ((1 << n) - 1) ^ mask;
            for (int m = mask2; m; m = (m - 1) & mask2) {
                if (popcount[m] != k / 2) continue;
                pr12[mask ^ m] += pr1[mask] * pr2[m];
            }
        }
        for (int mask = (1 << n) - 1; mask >= 0; --mask) {
            if (popcount[mask] == k)
                ans = max(ans, pr12[mask]);
        }
        printf("Case #%d: %.17f\n", ttt, (double)ans);
    }

    return 0;
}
