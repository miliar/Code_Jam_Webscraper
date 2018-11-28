#include<stdio.h>
int main()
{
    int t,ix,x1,x2,m,ar[5][5],br[5][5],i,j,k;
    scanf("%d",&t);

    for(m=0;m<t;m++)
    {
        scanf("%d",&x1);

        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            scanf("%d",&ar[i][j]);


            scanf("%d",&x2);

        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            scanf("%d",&br[i][j]);


            k=0;

        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(ar[x1-1][i]==br[x2-1][j])
                {
                    k++;
                    ix=i;
                }
            }
        }


        if(k==0)
        printf("Case #%d: Volunteer cheated!\n",m+1);

        else if(k==1)
        printf("Case #%d: %d\n",m+1,ar[x1-1][ix]);

        else
        printf("Case #%d: Bad magician!\n",m+1);

    }

    return 0;
}
