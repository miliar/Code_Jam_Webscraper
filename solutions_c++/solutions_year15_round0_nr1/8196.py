#include <stdio.h>

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out", "w", stdout);

    int t,smax,count=0,rq=0,i,j;
    scanf("%d",&t);

    for(i=0;i<t;i++)
    {
        scanf("%d",&smax);
        char str[smax+1];

        scanf("%s",&str);

        count=0;
        rq=0;

        for(j=0;j<smax+1;j++)
        {
            if(count>j || count==j)
                count=count+(str[j]-'0');

            else
            {
                rq=rq+j-count;
                count=count+j-count+(str[j]-'0');
            }

        }

        printf("Case #%d: %d\n",i+1,rq);

    }

    return 0;
}
