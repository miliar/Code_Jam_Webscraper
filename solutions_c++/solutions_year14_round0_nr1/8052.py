#include <cstdio>

int main()
{
    int T;

    freopen("date.in","r", stdin);
    freopen("date.out", "w", stdout);
    scanf("%d",&T);
    for (int Case = 1; Case <= T; ++Case)
    {
        int first_ans, second_ans, first_arrange[5][5], second_arrange[5][5];
        scanf("%d", &first_ans);
        for (int i = 1; i <= 4; ++i)
            for (int j = 1; j <= 4; ++j)
                scanf("%d", &first_arrange[i][j]);
        scanf("%d", &second_ans);
        for (int i = 1; i <= 4; ++i)
            for (int j = 1; j <= 4; ++j)
                scanf("%d", &second_arrange[i][j]);

        int matching = 0, finded;
        for (int j = 1; j <= 4; ++j)
        {
            for (int j1 = 1; j1 <= 4; ++j1)
                if (second_arrange[second_ans][j] == first_arrange[first_ans][j1])
                    ++matching, finded = second_arrange[second_ans][j];
        }
        if (matching == 1)
            printf("Case #%d: %d\n", Case, finded);
            else
            if(matching == 0)
                printf("Case #%d: Volunteer cheated!\n", Case);
                else
                printf("Case #%d: Bad magician!\n", Case);

    }

    return 0;
}

