#include<stdio.h>
#include<string.h>

int flag[15],cnt;

int main()
{
    int t,ti,n,i,j;
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(ti=1; ti<=t; ++ti)
    {
        scanf("%d",&n);
        cnt=0;
        memset(flag,0,sizeof(flag));
        if(n)
        {
            for(i=n; ; i+=n)
            {
                j=i;
                while(j)
                {
                    if(!flag[j%10])
                    {
                        flag[j%10]=1;
                        ++cnt;
                    }
                    j/=10;
                }
                if(cnt==10)
                    break;
            }
            printf("Case #%d: %d\n",ti,i);
        }
        else
            printf("Case #%d: INSOMNIA\n",ti);
    }
    return 0;
}
