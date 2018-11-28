#include <iostream>
#include <stdio.h>
using namespace std;


int n;

void deal()
{
    scanf("%d",&n);
    if(n==0)
    {
        puts("INSOMNIA"); return;
    }
    int ans=0;
    for(int i=1;;i++)
    {
        long long cur=1ll*i*n;
        while(cur)
        {
            ans|=1<<(cur%10);
            cur/=10;
        }
        if(ans==(1<<10)-1)
        {
            printf("%lld\n",1ll*i*n); return;
        }
    }
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("ans","w",stdout);
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        printf("Case #%d: ",i);
        deal();
    }
    return 0;
}
