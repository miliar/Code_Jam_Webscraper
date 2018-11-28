#include <stdio.h>

typedef unsigned long long lol;

int main()
{
    int a[17],t,x,k,r,i,j,ans;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        for(j=1;j<=16;j++)
            a[j] = 0;
        scanf("%d",&r);
        for(j=1;j<=4;j++)
        {
            if(j == r)
                for(k=0;k<4;k++)
                {
                    scanf("%d",&x);
                    a[x] = 1;
                }
            else
                scanf("%d %d %d %d",&k,&k,&k,&k);
        }
        scanf("%d",&r);
        for(j=1;j<=4;j++)
        {
            if(j == r)
                for(k=0;k<4;k++)
                {
                    scanf("%d",&x);
                    a[x] += 1;
                }
            else
                scanf("%d %d %d %d",&k,&k,&k,&k);
        }
        ans = 0;
        for(j=1;j<=16;j++)
        {
            if(a[j] > 1)
                if(ans != 0)
                {
                    ans = -1;break;
                }
                else
                    ans = j;

        }
        if(ans > 0)
            printf("Case #%d: %d\n",i,ans);
        else
            printf(ans==0?"Case #%d: Volunteer cheated!\n":"Case #%d: Bad magician!\n",i);


    }
    return 0;
}
