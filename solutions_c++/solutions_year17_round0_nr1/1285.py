// jimjam
#include <cstdio>

int T, K, S;
bool a[1005];

int main() {
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        getc(stdin);
        S = 0;
        char c = getc(stdin);
        while (c != ' ') {
            a[S++] = c == '-';
            c = getc(stdin);
        }
        scanf("%d", &K);
        int ans = 0;
        for (int i = 0; i+K <= S; i++) {
            if (a[i]) {
                for (int j = i; j < i+K; j++) a[j] ^= 1;
                ans++;
            }
        }
        bool g = 1;
        for (int i = 0; i < S && g; i++) g = !a[i];
        printf("Case #%d: ", t);
        if (g) printf("%d\n", ans);
        else printf("IMPOSSIBLE\n");
    }
}


