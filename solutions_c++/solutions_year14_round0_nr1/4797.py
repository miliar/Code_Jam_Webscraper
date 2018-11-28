#include<stdio.h>
int main()
{
    int t,l=1;
    scanf("%d",&t);
    for(l=1;l<=t;l++)
    {
        int r1,r2,a1[20]={0},a2[20]={0},ans[20]={0},x=0,i,j;
        scanf("%d",&r1);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                int k;
                scanf("%d",&k);
                if(i==r1)
                    a1[k]=1;
            }
        }
        scanf("%d",&r2);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                int k;
                scanf("%d",&k);
                if(i==r2)
                    a2[k]=1;
            }
        }
        for(i=1;i<=16;i++)
        {
            if(a1[i]&&a2[i])
            {
                ans[x]=i;
                x++;
            }
        }
        if(x==1)
            printf("Case #%d: %d\n",l,ans[0]);
        else if(x==0)
            printf("Case #%d: Volunteer cheated!\n",l);
        else
            printf("Case #%d: Bad magician!\n",l);

    }
    return 0;
}
