#include <bits/stdc++.h>

const int maxn = 1005;

int T, k;
char s[maxn];

int main() {
    scanf("%d", &T);
    for (int test = 1; test <= T; test++) {
        scanf(" %s%d", s, &k);
        int n = strlen(s);
        int ans = 0;
        for (int i = 0; i <= n-k; i++) {
            if (s[i] == '-') {
                for (int j = i; j < i+k; j++) {
                    s[j] = (s[j] == '+' ? '-' : '+');
                }
                ans++;
            }
        }
        bool done = true;
        for (int i = 0; i < n; i++) {
            if (s[i] == '-') {
                done = false;
            }
        }
        printf("Case #%d: ", test);
        if (done) {
            printf("%d\n", ans);
        } else {
            printf("IMPOSSIBLE\n");
        }
    }
}

