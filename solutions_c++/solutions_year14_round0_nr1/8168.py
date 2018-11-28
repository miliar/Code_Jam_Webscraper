#include <bits/stdc++.h>
using namespace std;

int arrange1[5][5];
int arrange2[5][5];

int ans1;
int ans2;

int row1[5];
int row2[5];

int T;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    scanf("%d", &T);

    for(int t = 1; t <= T; t++)
    {
        scanf("%d", &ans1);

        for(int i = 1; i <= 4; i++)
            for(int j = 1; j <= 4; j++)
                scanf("%d", &arrange1[i][j]);

        row1[1] = arrange1[ans1][1];
        row1[2] = arrange1[ans1][2];
        row1[3] = arrange1[ans1][3];
        row1[4] = arrange1[ans1][4];

        sort(row1+1, row1+5);

        scanf("%d", &ans2);

        for(int i = 1; i <= 4; i++)
            for(int j = 1; j <= 4; j++)
                scanf("%d", &arrange2[i][j]);

        row2[1] = arrange2[ans2][1];
        row2[2] = arrange2[ans2][2];
        row2[3] = arrange2[ans2][3];
        row2[4] = arrange2[ans2][4];

        sort(row2+1, row2+5);

        int counter = 0, target;

        for(int i = 1; i <= 4; i++)
            for(int j = 1; j <= 4; j++)
            {
                if(row1[i] == row2[j])
                    {
                        counter++;
                        target = row2[j];
                    }

            }

        if(counter  > 1)
            printf("Case #%d: Bad magician!\n", t);
        if(counter == 1)
            printf("Case #%d: %d\n", t, target);
        if(counter == 0)
            printf("Case #%d: Volunteer cheated!\n", t);




    }

    return 0;
}
