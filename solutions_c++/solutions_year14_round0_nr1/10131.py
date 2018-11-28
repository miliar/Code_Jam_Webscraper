#include<stdio.h>
#include<stdlib.h>

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,i;

    scanf("%d",&t);

    for(i=1;i<=t;i++)
    {
        int count[17]={0};
        int N=2,x,a,j,k,nc=0,b;

        while(N--)
        {
            scanf("%d",&x);

            for(j=1;j<=4;j++)
            {
                for(k=1;k<=4;k++)
                {
                    scanf("%d",&a);

                    if(j==x)
                        count[a]++;
                }
            }
        }

        for(j=1;j<=16;j++)
        {
         //   printf("%d ",count[j]);
            if(count[j]==2)
            {
                nc++;
                b=j;
            }
        }
        //printf("\n");

        if(nc==1)
            printf("Case #%d: %d\n",i,b);
        else if(nc>1)
            printf("Case #%d: Bad magician!\n",i);
        else
            printf("Case #%d: Volunteer cheated!\n",i);
    }
    return 0;
}
