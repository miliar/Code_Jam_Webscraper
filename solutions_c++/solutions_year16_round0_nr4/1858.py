#include <bits/stdc++.h>

using namespace std;

int t, k, c, s;

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small.out", "w", stdout);
    scanf("%d", &t);
    for (int tp=1; tp<=t; tp++) {
        cin >> k >> c >> s;
        if (s < k)
            printf("Case #%d: IMPOSSIBLE\n", tp);
        else {
            printf("Case #%d:", tp);
            for (int i=1; i<=k; i++) printf(" %d", i);
            printf("\n");
        }
    }

    return 0;
}
