#include <cstdio>
#include <cstring>

int main() {
    int T, l, cnt;
    char s[110];
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%s", s);
        l = strlen(s);
        cnt = 0;
        for (int i = 1; i < l; ++i)
            if (s[i] != s[i-1])
                ++cnt;
        if (s[l-1] == '-')
            ++cnt;
        printf("Case #%d: %d\n", t, cnt);
    }
    return 0;
}
