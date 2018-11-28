#include<bits/stdc++.h>
#define ll long long int
using namespace std;

bool vis[10];

void check(ll n)
{
    while(n)
    {
        vis[n%10]=true;
        n/=10;
    }
}

int main()
{
    ll t,n;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%lld",&t);
    for(ll x1=1;x1<=t;x1++)
    {
        scanf("%lld",&n);
        memset(vis,false,sizeof(vis));
        if(n==0)
        {
            //scanf("%d",)
            printf("Case #%lld: INSOMNIA\n",x1);
        }
        else
        {
            ll i=1,prd;
            while(1)
            {
                prd=i*n;
                check(prd);
                i++;
                ll pos=0;
                //cout<<prd<<endl;
               for(int j=0;j<=9;j++)
               {
                if(vis[j]!=true)
                {
                    pos=1;
                    break;
                }
               }
               if(pos==0)
               {
                printf("Case #%lld: %lld\n",x1,prd);
                break;
               }
            }
        }
    }
    return 0;
}
