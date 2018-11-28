#include <stdio.h>

int main()
{
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        int n;
        int a[4][4];
        int m;
        int b[4][4];
        scanf("%d", &n);
        n--;
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
                scanf("%d", &a[i][j]);
        scanf("%d", &m);
        m--;
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
                scanf("%d", &b[i][j]);
        int cnt = 0;
        int val = 0;
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
                if (a[n][i] == b[m][j])
                {
                    cnt++;
                    val = a[n][i];
                }
        if (cnt == 0)
            printf("Case #%d: Volunteer cheated!\n", cas);
        else if (cnt == 1)
            printf("Case #%d: %d\n", cas, val);
        else
            printf("case #%d: Bad magician!\n", cas);
    }

    return 0;
}
