#include<bits/stdc++.h>
#define ll long long int
using namespace std;

bool visit[20];

bool check()
{
    for(ll i=0; i<10; i++)
        if(!visit[i])
            return false;
    return true;
}

int main()
{
    freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);

    ll t,T,n,m,i,j,ans,a;
    scanf("%lld",&T);
    //while(scanf("%lld",&n)!=EOF)
    for(t=1; t<=T; t++)
    {
        scanf("%lld",&n);
        memset(visit,false,sizeof visit);
        ans=n;
        for(i=1; i<=10000; i++)
        {
            ans=n*i;
            m=ans;
            while(m>0)
            {
                a=m%10;
                m=m/10;
                visit[a]=true;
            }
            if(check())
                break;

        }
        if(check())
            printf("Case #%lld: %lld\n",t,ans);
        else
            printf("Case #%lld: INSOMNIA\n",t);
    }
    return 0;
}

