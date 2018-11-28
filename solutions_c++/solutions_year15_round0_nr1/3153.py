#include<bits/stdc++.h>
#define in freopen("A-large.in", "r", stdin);
#define out freopen("solve_out.txt", "w", stdout);
using namespace std;
const int maxn = 10000;
char s[maxn];

int main() {
//    in
//    out
    int T;
    for (int t = scanf("%d", &T); t <= T; t++) {
        int n;
        scanf("%d%s", &n, s);
        int ans = 0, now = 0;
        for (int i = 0; i <= n; i++) {
            ans += max(0, i - now);
            now = max(now, i) + (int)(s[i] - '0');
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
