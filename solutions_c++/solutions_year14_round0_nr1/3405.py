#include<stdio.h>
#include<stdlib.h>

int flag[20];
int grid[6][6];

int main()
{
    freopen("magic.in","rt",stdin);
    freopen("magic.out","wt",stdout);
    int i,j,tcase,t,r,c,result;
    scanf("%d",&tcase);
    for(t=1;t<=tcase;t++)
    {
        for(i=1;i<=16;i++)
            flag[i] = 0;
        c = 0;
        result = 0;
        scanf("%d",&r);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&grid[i][j]);
        for(i=1;i<=4;i++)
            flag[grid[r][i]]++;
        scanf("%d",&r);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&grid[i][j]);
        for(i=1;i<=4;i++)
            flag[grid[r][i]]++;
        for(i=1;i<=16;i++)
            if(flag[i] == 2)
            {
                c++;
                result = i;
            }

        printf("Case #%d: ",t);
        if(c == 0)
            printf("Volunteer cheated!\n");
        else if(c == 1)
            printf("%d\n",result);
        else
            printf("Bad magician!\n");
    }
    return 0;
}

