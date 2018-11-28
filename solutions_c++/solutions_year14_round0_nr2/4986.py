#include<bits/stdc++.h>
typedef long long int ll;
using namespace std;
int main()
{
     int t;
     long long int k=1;
     double c,f,x,cookies=2;
     double val1,ans=0,val2;
     scanf("%d",&t);
     while(t--)
     {
          scanf("%lf %lf %lf",&c,&f,&x);
          while(1)
          {
               val1=c/cookies+x/(cookies+f);
               val2=x/cookies;

               if(val1>val2)
                {
                     ans+=x/(cookies);

                     break;
                }
                else
                ans+=c/cookies;

                cookies+=f;
          }
          printf("Case #%lld: %.8lf\n",k,ans);
          ans=0,cookies=2;
          k++;
     }
     return 0;
}
