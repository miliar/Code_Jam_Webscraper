#include <stdio.h>
#include <stdlib.h>
int fRound[4][4],sRound[4][4];
int main()
{
    freopen("A-small-attempt0.in","rt",stdin);
    freopen("A-small-attempt0.out","wt",stdout);
    int nTest,r1,r2;
    scanf("%d",&nTest);
    int ans;
    for(int test = 1; test<= nTest;test++)
    {
        scanf("%d",&r1);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&fRound[i][j]);
            }
        }
        scanf("%d",&r2);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&sRound[i][j]);
            }
        }
        int sameNumCount = 0;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(fRound[r1-1][i] == sRound[r2-1][j])
                {
                    sameNumCount++;
                    ans = fRound[r1-1][i];
                }
            }
        }
        printf("Case #%d: ",test);
        if(sameNumCount == 0)
        {
            printf("Volunteer cheated!\n");
        }
        else if(sameNumCount == 1)
        {
            printf("%d\n",ans);
        }
        else
        {
            printf("Bad magician!\n");

        }
    }
    return 0;
}

