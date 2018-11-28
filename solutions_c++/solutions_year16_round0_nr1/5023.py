#include <stdio.h>
#include <string.h>
#define LL long long

bool vis[10];
int cnt=0;

LL check(LL now, LL k)
{
    if(now>1e18) return -1;
    LL tmp=now;
    while(tmp>0)
    {
        if(!vis[tmp%10]) 
        {
            vis[tmp%10]=true;
            cnt++;
        }
        tmp/=10;
    }
    if(cnt<10)  return check(now+k,k);
    else
        return now;
}



int main()
{
    int i,j,m,n,t;
    LL k;
    freopen("a.in","r",stdin);
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        cnt=0;
        memset(vis,0,sizeof(vis));
        printf("Case #%d: ",i);
        scanf("%lld",&k);
        if(k==0)
        {
            puts("INSOMNIA");
            continue;
        }
        LL ans=check(k,k);
        if(ans<0) puts("INSOMNIA");
        else
            printf("%lld\n",ans);
    }
    fclose(stdin);
    return 0;
}


