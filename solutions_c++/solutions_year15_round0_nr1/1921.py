#include <cstdio>
#include <cassert>
#include <cstring>

int T, max;
char s[1010];

int main() {
    scanf("%d", &T);
    for (int Test = 1; Test <= T; ++Test) {
        scanf("%d %s", &max, s);
        assert(strlen(s) == max + 1);
        int cnt = 0, ans = 0;
        for (int i = 0; i <= max; ++i) {
            if (cnt < i) ans += i - cnt, cnt = i;
            cnt += s[i] - '0';
        }
        printf("Case #%d: %d\n", Test, ans);
    }
}
