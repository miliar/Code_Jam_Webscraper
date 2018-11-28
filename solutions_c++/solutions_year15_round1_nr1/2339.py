#include<stdio.h>

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("out_A.txt", "w", stdout);

    int T, N, m1, m2, x, y, z, i, max, m[1010];
    scanf("%d", &T);
    for (x = 1; x <= T; x++) {
        scanf("%d", &N);
        scanf("%d", &m1);
        m[0] = m1;
        y = 0;
        max = 0;
        for (i = 1; i < N; i++) {
            scanf("%d", &m2);
            m[i] = m2;
            if (m2 <= m1) {
                y += m1-m2;
                max = (m1-m2 > max)? m1-m2 : max;
            }
            m1 = m2;
        }
        z = 0;
        for (i = 0; i < N-1; i++) {
            if (m[i] - max > 0) z += max;
            else z += m[i];
        }
        printf("Case #%d: %d %d\n", x, y, z);
    }
    return 0;
}
