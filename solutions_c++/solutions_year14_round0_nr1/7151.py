#include <iostream>
#include <cstdio>

using namespace std;

int nr[8];
int a[8][8];

int main()
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    int T;
    scanf ("%d", &T);
    for (int t = 1; t <= T; ++ t)
    {
        int ans1, ans2;
        scanf ("%d", &ans1);
        for (int i = 1; i <= 4; ++ i)
            for (int j = 1; j <= 4; ++ j)
                scanf("%d", &a[i][j]);
        for (int i = 1; i <= 4; ++ i)
            nr[i] = a[ans1][i];

        scanf("%d", &ans2);
        for (int i = 1; i <= 4; ++ i)
            for (int j = 1; j <= 4; ++ j)
                scanf("%d", &a[i][j]);

        int nrfound = 0, rasp;
        for (int i = 1; i <= 4; ++ i)
        {
            for (int j = 1; j <= 4; ++ j)
                if (nr[j] == a[ans2][i])
                {
                    rasp = nr[j];
                    ++nrfound;
                    j = 5;
                }
        }

        if (nrfound == 0)
            printf("Case #%d: Volunteer cheated!\n", t);
        if (nrfound == 1)
            printf("Case #%d: %d\n", t, rasp);
        if (nrfound > 1)
            printf("Case #%d: Bad magician!\n", t);
    }
    return 0;
}
