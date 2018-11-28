#include<bits/stdc++.h>
using namespace std;
typedef  long long int ll;
ll a[6][6];
ll c[6][6];
int main()
{
     ll k=1,t,i,j,a1,a2,cnt=0,ans=0;
     scanf("%lld",&t);
     while(t--)
     {

          scanf("%lld",&a1);
          for(i=1;i<=4;i++)
          {
               for(j=1;j<=4;j++)
               {
                    scanf("%lld",&a[i][j]);
               }
          }
          scanf("%lld",&a2);
          for(i=1;i<=4;i++)
          {
               for(j=1;j<=4;j++)
               {
                    scanf("%lld",&c[i][j]);
               }
          }
          for(i=1;i<=4;i++)
          {
               for(j=1;j<=4;j++)
               {
                    if(a[a1][i]==c[a2][j])
                    {
                         cnt++;
                         ans=a[a1][i];
                    }
               }
          }
          if(cnt==1)
          printf("Case #%lld: %lld\n",k,ans);
          else if(cnt>1)
          printf("Case #%lld: Bad magician!\n",k);
          else
          printf("Case #%lld: Volunteer cheated!\n",k);
          k++;
          cnt=0;

     }
     return 0;
}
