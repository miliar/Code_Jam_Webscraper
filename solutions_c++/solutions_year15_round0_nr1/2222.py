#include <cstdio>
#include <cstdlib>
#include <cstring>

char s[1100];

int main()
{
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        int smax;
        scanf("%d%s", &smax, s);
        int len = strlen(s);
        int tot = 0, ans = 0;
        for (int i = 0; i < len; ++i) {
            int d = s[i] - '0';
            if (d == 0)
                continue;
            if (tot < i) {
                ans += i - tot;
                tot = i;
            }
            tot += d;
        }
        printf("Case #%d: %d\n", t, ans);
    }

    return 0;
}
