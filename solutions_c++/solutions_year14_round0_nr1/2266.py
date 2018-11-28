#include<cstdio>
#include<iostream>

using namespace std;

int main()
{
    //freopen("ans.txt","w",stdout);
   // freopen("B-small-attempt1.in","r",stdin);
    int t;
    scanf("%d",&t);
    int grid1[4][4],grid2[4][4],num1,num2;
    int i,j,k;
   for(k=1;k<=t;k++)
    {
        int ctr=0,ans=0;
        scanf("%d",&num1);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&grid1[i][j]);
            }
            getchar();
        }
        scanf("%d",&num2);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&grid2[i][j]);
            }
            getchar();
        }
        --num1;
        --num2;

        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(grid1[num1][i]==grid2[num2][j])
               {if(ctr==0)
                   ans=grid1[num1][i];
                   ctr++;
               }
            }
        }
        if(ctr==1)
        printf("Case #%d: %d\n",k,ans);
        else if(ctr==0)
         printf("Case #%d: Volunteer cheated!\n",k);
         else
         printf("Case #%d: Bad magician!\n",k);
    }
    return 0;
}
