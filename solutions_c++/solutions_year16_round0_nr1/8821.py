#include <bits/stdc++.h>
#define ll long long

using namespace std;

int main()
{
    int t,d=0;
    scanf("%d",&t);
    while(t--)
    {
        d++;
        int n,i;
        scanf("%d",&n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",d);
            continue;
        }
        ll num=(ll)n;
        ll dp[10];
        for(i=0;i<10;i++)
            dp[i]=0;
        ll cn=10;
       while(1)
       {

           ll x=num;
           while(x)
           {
               ll dv=x%10;
               x=x/10;
               if(dp[dv]==0)
               {
                   dp[dv]=1;
                   cn--;
               }
           }
           if(cn==0)
            break;

           num=num+n;
       }
       printf("Case #%d: %lld\n",d,num);

    }
    return 0;
}
