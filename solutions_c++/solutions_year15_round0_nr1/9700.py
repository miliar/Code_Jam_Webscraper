#include<stdio.h>
int main()
{
    int t,x=1,i,sum,counter,m,a[1001];
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&m);
        for(i=0;i<=m;i++)
            scanf("%1d",&a[i]);

        sum=0;
        counter=0;

        for(i=0;i<=m;i++)
        {
            if(counter<i)
                {
                    sum++;
                    counter++;
                }
            counter+=a[i];
        }
        printf("Case #%d: %d\n",x++,sum);
    }
    return 0;
}
