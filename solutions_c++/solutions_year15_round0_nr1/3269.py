#include <cstdio>

int main() {
    int T;
    char s[1010];
    scanf("%d", &T);
    for (int x = 1; x <= T; ++x) {
        int len;
        scanf("%d %s", &len, s);
        int y = 0, cnt = s[0] - '0';
        for (int i = 1; i <= len; ++i) {
            if (y + cnt < i)
                y = i - cnt;
            cnt += (s[i] - '0');
        }
        printf("Case #%d: %d\n", x, y);
    }
    return 0;
}
