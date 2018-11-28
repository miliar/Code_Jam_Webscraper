#include<bits/stdc++.h>
#define LL long long
using namespace std;
LL t,i,j,k,l,n,cnt,ans,a[15],x;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%lld",&t);
    for(l=1;l<=t;l++)
    {
        ans=-1;
        scanf("%lld",&n);
        memset(a,0,sizeof(a));
        cnt=0;
        for(i=1;i<=1000000;i++)
        {
            x=n*i;
            if(x==0)
            {
                if(a[x%10]==0)
                {
                    a[x%10]=1;
                    cnt++;
                    if(cnt==10)
                    {
                        ans=n*i;
                        break;
                    }
                }
            }
            while(x>0)
            {
                if(a[x%10]==0)
                {
                    a[x%10]=1;
                    cnt++;
                    if(cnt==10)
                    {
                        ans=n*i;
                        break;
                    }
                }
                x/=10;
            }
            if(cnt==10)
            {
                break;
            }
        }
        if(ans==-1)
        {
            printf("Case #%lld: INSOMNIA\n",l);
        }
        else
        {
            printf("Case #%lld: %lld\n",l,ans);
        }
    }
    return 0;
}
