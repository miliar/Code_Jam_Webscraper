#include<cstdio>
#include<iostream>
#include<cstring>
#include<cmath>
using namespace std;
int solve(int n)
{
    if(n==0) return -1;
    else
    {
        int a[12];
        memset(a,0,sizeof(a));
        int last=n;
        while(1)
        {
            int d=last;
            while(d)
            {
                a[d%10]=1;
                d/=10;
            }
            int ch=0;
            for(int i=0;i<10;i++) ch+=a[i];
            if(ch==10) return last;
            last+=n;
        }
    }
}
int main()
{
    freopen("A_large.in","r",stdin);
    freopen("A_large.out","w",stdout);
    int T,cas=0;scanf("%d",&T);
    while(T--)
    {
        int n;
        scanf("%d",&n);
        int ans=solve(n);
        if(ans==-1) printf("Case #%d: INSOMNIA\n",++cas);
        else printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}
