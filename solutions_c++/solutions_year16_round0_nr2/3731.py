#include <cstdio>
#include <cstring>

int main() {
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        char s[105];
        scanf("%s", s);
        int n = strlen(s), cnt = 1;
        for (int i = 1; i < n; ++i) {
            if (s[i] != s[i-1]) ++cnt;
        }
        if (s[n-1] == '+') --cnt;
        printf("Case #%d: %d\n", cas, cnt);
    }
}
