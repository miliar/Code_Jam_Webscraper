#include <bits/stdc++.h>

int main()
{
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        int N; scanf("%d", &N);
        int k = 0, ans = 0;
        for (int i = 0; i <= N; i++) {
            char c; scanf(" %c", &c);
            if (k < i) ans++, k++;
            k += c-'0';
        }
        printf("Case #%d: %d\n", t, ans);
    }
}

