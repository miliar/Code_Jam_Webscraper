#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ll t=0,s=0,i=0,co=1;
    scanf("%lld",&t);
    while(t--)
    {

        scanf("%lld",&s);
        char p[s+1];
        for(i=0;i<=s;i++)
        {
            scanf(" %ch ",&p[i]);
        }
        ll ps=0;
        ll ans=0;
        for(i=0;i<=s;i++)
        {
            ll temp = p[i] - '0';
          if(i<=ps && temp!=0)
                ps=ps+temp;
            else
              {
                  if(temp!=0)
                  {
                  ans+=i-ps;
                  ps=ps+ans+temp;
                  }

              }


              }

        printf("Case #%lld: %lld\n",co,ans);
        co++;
    }
}

