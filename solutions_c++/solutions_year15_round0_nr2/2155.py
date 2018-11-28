#include <bits/stdc++.h>

const int inf = 1000*1000*1000+1;

int a[1005];

int main()
{
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        int N; scanf("%d", &N);
        for (int i = 0; i < N; i++) scanf("%d", &a[i]);
        int ans = inf;
        for (int p = 1; p <= 1000; p++) {
            int k = p;
            for (int i = 0; i < N; i++) k += (a[i]-1)/p;
            ans = std::min(ans, k);
        }
        printf("Case #%d: %d\n", t, ans);
    }
}
