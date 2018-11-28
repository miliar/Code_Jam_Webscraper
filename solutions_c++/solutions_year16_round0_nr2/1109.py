#include <cstdio>
#include <cstring>

int main() {
    int T, n;
    char s[105];
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%s", s);
        n = strlen(s);
        s[n++] = '+';
        int ans = 0;
        for (int i = 1; i < n; i++)
            if (s[i] != s[i-1])
                ans++;
        printf("Case #%d: %d\n", t, ans);
    }
}
