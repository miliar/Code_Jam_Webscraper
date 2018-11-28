#include <bits/stdc++.h>
using namespace std;

char s[110][1000];

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int n, L;
        scanf("%d%d", &n, &L);
        for (int i = 0; i < n; i++) {
            scanf("%s", s[i]);
        }
        scanf("%s", s[n]);
        bool sol = true;
        for (int i = 0; i < n; i++) {
            if (string(s[i]) == string(s[n])) {
                sol = false;
            }
        }
        printf("Case #%d:", cas);
        if (!sol) {
            puts(" IMPOSSIBLE");
        } else {
            if (L == 1) {
                puts(" 0? 0");
            } else {
                printf(" ");
                for (int i = 0; i < L; i++) {
                    printf("0?");
                }
                printf(" ");
                for (int i = 0; i < L - 1; i++) {
                    printf("1");
                }
                puts("");
            }
        }
    }
    return 0;
}