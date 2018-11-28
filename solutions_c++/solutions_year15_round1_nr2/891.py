#include<cstdio>
long long h[1005];
int main()
{
    freopen("2015_1A_A_l.in","r",stdin);
    freopen("2015_1A_A_l.out","w",stdout);
    int T;
    long long n,x,mn,mx,md,all;
    scanf("%d",&T);
    for(int I=1;I<=T;I++)
    {
        mn=0; mx=100000000000000;
        scanf("%lld%lld",&n,&x);
        for(int i=1;i<=n;i++)
            scanf("%lld",&h[i]);
        while(mn<=mx)
        {
            md=(mx+mn)/2;
            all=0;
            for(int i=1;i<=n;i++)
                all+=md/h[i]+1;
            if(all<x)
                mn=md+1;
            else if(mn!=md)
                mx=md;
            else
                break;
        }
        //printf("=> %d\n",md);
        for(int i=n;i>0;i--)
            if(md%h[i]==0)
                if(all>x)
                    all--;
                else
                {
                    printf("Case #%d: %d\n",I,i);
                    break;
                }


    }
}
