#include <bits/stdc++.h>
using namespace std;

int main() {
    int T, N, m[1010];

    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d", &N);
        for (int i = 0; i < N; i++)
            scanf("%d", &m[i]);

        int a = 0;
        for (int i = 1; i < N; i++)
            if (m[i-1] > m[i])
                a += m[i-1] - m[i];

        int x = 0;
        for (int i = 1; i < N; i++)
            x = max(x, m[i-1] - m[i]);
        int b = 0;
        for (int i = 0; i < N-1; i++)
            b += min(x, m[i]);

        printf("Case #%d: %d %d\n", t, a, b);
    }
}
