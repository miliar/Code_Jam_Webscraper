#include<stdio.h>

int a[12];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("large.txt","w",stdout);
    int b,i,m,n,t,res,cnt,co=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&m);
        for(i=0;i<=10;i++)
            a[i]=1;
        cnt=0;
        if(m==0)
            printf("Case #%d: INSOMNIA\n",co++);
        else
        {
            for(i=1;;i++)
            {
                n=m*i;
                res=n;
                while(n>0)
                {
                    b=n%10;
                    n=n/10;
                    if(a[b])
                    {
                        cnt++;
                        a[b]=0;
                    }
                }
                if(cnt==10)
                    break;
            }
            printf("Case #%d: %d\n",co++,res);
        }
    }
    return 0;
}
