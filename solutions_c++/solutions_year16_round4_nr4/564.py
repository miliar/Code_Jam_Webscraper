#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

int popcount[139000];

int n;
char s[99][99];
int p[99], p2[99], u[99];
int reached = 0;

bool brute(int mask, int idx) {
    if (idx == n) return true;
    int was = 0;
    for (int i = 0; i < n; ++i) {
        if (u[i]) continue;
        if (mask & (1 << (p[idx] + i))) {
            u[i] = 1;
            if (!brute(mask, idx + 1)) return false;
            u[i] = 0;
            was = 1;
        }
    }
    return was;
}

bool check(int mask) {
    for (int i = 0; i < n; ++i)
        p[i] = i * n;
    do {
        for (int i = 0; i < n; ++i)
            u[i] = 0;
        reached = 0;
        if (!brute(mask, 0)) return false;
    } while (next_permutation(p, p + n));
    return true;
}

int main()
{
    //freopen("D-small-attempt0.in", "r", stdin);
   // freopen("D-small-attempt0.out", "w", stdout);

    for (int i = 0; i < 139000; ++i) popcount[i] = __builtin_popcount(i);

    int t;
    cin >> t;
    for (int ttt = 1; ttt <= t; ++ttt) {
        cin >> n;
        for (int i = 0; i < n; ++i) cin >> s[i];
        int mask_can = 0;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                mask_can |= ((s[i][j] - 48) << (i * n + j));
        int ans = 2e9;
        for (int mask = (1 << (n * n)) - 1; mask >= 0; --mask) {
            if (mask & mask_can) continue;
            if (check(mask | mask_can))
                ans = min(ans, popcount[mask]);
        }
        cout << "Case #" << ttt << ": " << ans << "\n";
    }

    return 0;
}
