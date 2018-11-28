#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll hash[1000000+6]={0};
ll func(ll tt,ll n)
{
  ll i;
    ll a[10]={0};
    ll cnt=0;
    for(i=1;i<100;i++)
    {
      ll tmp2=n*i;
     ll tmp = tmp2;
      while(tmp>0)
      {
        if(a[tmp%10]==0)
        {
          a[tmp%10]=1;
          cnt++;
        }
        tmp/=10;
        if(cnt==10)
        {
          hash[n]=tmp2;
          printf("Case #%lld: %lld\n",tt,hash[n]);
          return 0;
        }
      }

    }
    printf("INSOMNIA\n");
  return 0;
}

int main()
{
   ll i,j,k,m,n,t;
   scanf("%lld\n",&t);
   for(i=1;i<=t;i++)
   {
     scanf("%lld",&n);
     if(n==0)
       printf("Case #%lld: INSOMNIA\n",i);
     else
     {
       if(hash[n]!=0)
         printf("Case #%lld: %lld\n",i,hash[n]);
        else
       func(i,n);
     }
   }
   return 0;
}
