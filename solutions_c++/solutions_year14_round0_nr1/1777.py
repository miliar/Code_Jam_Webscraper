#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    int used[16];
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        printf("Case #%d: ", i + 1);
        for (int j = 0; j < 16; j++)
            used[j] = 0;
        int r1, r2;
        scanf("%d", &r1);
        r1--;
        for (int j = 0; j < 4; j++)
            for (int k = 0; k < 4; k++)
            {
                int elem;
                scanf("%d", &elem);
                if (j == r1)
                    used[elem - 1]++;
            }

        scanf("%d", &r2);
        r2--;
        for (int j = 0; j < 4; j++)
            for (int k = 0; k < 4; k++)
            {
                int elem;
                scanf("%d", &elem);
                if (j == r2)
                    used[elem - 1]++;
            }

        int cnt = 0;
        int ans = 0;
        for (int j = 0; j < 16; j++)
            if (used[j] == 2)
            {
                cnt++;
                ans = j + 1;
            }

        if (cnt > 1)
            printf("Bad magician!\n");
        if (cnt == 0)
            printf("Volunteer cheated!\n");
        if (cnt == 1)
            printf("%d\n", ans);

    }
    return 0;
}
