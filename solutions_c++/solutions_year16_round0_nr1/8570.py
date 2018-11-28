#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
bool ch(bool vis[]){
    bool ans=true;
   for(int i=0;i<10;i++)
       ans&=vis[i];
   return ans;
}
int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int t;
    ll n;
    scanf("%d",&t);
    for(int test=1;test<=t;test++)
    {
      printf("Case #%d: ",test);
      bool vis[10];
      memset(vis,0,sizeof(vis));
      scanf("%lld",&n);
      if(n==0)
      printf("INSOMNIA\n");
      else
      {
          ll temp=n;
          ll ans;
          int i=1;
          while(1)
            {
                n=(ll)(i)*temp;
                while(n>0)
                {
                   vis[n%10]=true;
                   n/=10;
                }
                i++;
                if(ch(vis))
                  {
                    ans=(ll)(i-1)*temp;
                    break;
                  }
            }
            printf("%lld\n",ans);
      }
    }
    return 0;
}
