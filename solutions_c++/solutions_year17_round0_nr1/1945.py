#include <bits/stdc++.h>

int jizz() {
    static char str[int(1e4) + 10];
    int k;
    scanf("%s%d", str, &k);

    int ans = 0;
    int len = strlen(str);

    for (int i = 0; i < len; ++i) str[i] = str[i] == '+' ? 0 : 1;

    for (int i = 0; i <= len-k; ++i) {
        if (not str[i]) continue;

        ans += 1;
        for (int j = 0; j < k; ++j)
            str[i+j] ^= 1;
    }

    for (int i = 0; i < len; ++i)
        if (str[len-i])
            return -1;

    return ans;
}

int main() {
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);
        int gg = jizz();
        if (gg == -1) puts("IMPOSSIBLE");
        else printf("%d\n", gg);
    }
    return 0;
}
