#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    for (int cases = 1; cases <= T; cases++)
    {
        int ans1, ans2;
        int card1[4][4], card2[4][4];
        scanf("%d", &ans1);
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                scanf("%d", &card1[i][j]);
            }
        }
        scanf("%d", &ans2);
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                scanf("%d", &card2[i][j]);
            }
        }
        ans1--, ans2--;
        int count[17] = {0};
        for (int j = 0; j < 4; j++)
        {
            count[card1[ans1][j]]++;
            count[card2[ans2][j]]++;
        }
        int found = 0, ans = 0;
        for (int i = 1; i <= 16; i++)
        {
            if (count[i] == 2)
            {
                ans = i;
                found++;
            }
        }
        if (ans == 0)
        {
            printf("Case #%d: Volunteer cheated!\n", cases);
        }
        else if (found > 1)
        {
            printf("Case #%d: Bad magician!\n", cases);
        }
        else
        {
            printf("Case #%d: %d\n", cases, ans);
        }
    }
    return 0;
}
