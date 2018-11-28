#include<bits/stdc++.h>
using namespace std;
typedef long long int lli;
int arr[15];
//lli dp[1000000+100];
int func(lli p)
{
   while(p)
   {
        arr[p%10]=1;
        p/=10;
   }
   for(int i=0;i<=9;++i)
   {
        if(!arr[i])
        {
            return 0;
        }
   }
   return 1;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    int t,p=1;
    scanf("%d",&t);
    while(t--)
    {
      lli n;
      scanf("%lld",&n);
      memset(arr,0,sizeof(arr));

      if(n==0)
      {
        printf("Case #%d: INSOMNIA\n",p++);
      }
      else
      {
        lli ans=n,k=2;
        while(!func(ans))
        {
            ans=n*k;k++;
        }
        printf("Case #%d: %lld\n",p++,ans);
      }

    }
    return 0;
}
