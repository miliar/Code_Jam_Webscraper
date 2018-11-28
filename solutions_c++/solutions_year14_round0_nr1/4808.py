#include <stdio.h>

int main()
{
    int seq1[4][4], seq2[4][4], row1[4], row2[4];
    int i, j, test, t, r1, r2, n=1, flag = 0, pos;

    freopen("test.in", "r", stdin);
    freopen("mt.out", "w", stdout);

    scanf("%d",&test);

    for(t=1;t<=test;t++)
    {
        scanf("%d",&r1);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&seq1[i-1][j-1]);

        scanf("%d",&r2);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&seq2[i-1][j-1]);

        for(i=0;i<4;i++)
        {
            row1[i] = seq1[r1-1][i];
            row2[i] = seq2[r2-1][i];
        }

        flag = 0; pos = 20;

        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(row1[i] == row2[j])
                {
                    flag++;
                    pos = row1[i];
                }
            }
        }

        if(flag==0)
            printf("Case #%d: Volunteer cheated!\n",t);
        else if(flag==1)
            printf("Case #%d: %d\n",t,pos);
        else
            printf("Case #%d: Bad magician!\n",t);

    }
    return 0;
}
