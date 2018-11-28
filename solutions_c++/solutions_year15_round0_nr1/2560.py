#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1000 + 10;

int n;
char s[MAXN];

int main() {
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small-attempt0.out", "w", stdout);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d%s", &n, &s);
        int ans = 0;
        int num = s[0] - '0';
        for (int i = 1; i <= n; ++i) {
            if (num < i) {
                ans += i - num;
                num = i;
            }
            num += s[i] - '0';
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
