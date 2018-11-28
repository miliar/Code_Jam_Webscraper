#include<iostream>
#include<vector>
#include<string.h>
#include<set>
#include<algorithm>
#include<math.h>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

#define s(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
typedef unsigned long long int ll;
ll a[1000005];
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
   ll t,i,j,n,test,ac,p,c=0,c2=0;
    cin>>t;
    for(test=1;test<=t;test++)
   {
       c=0;c2=0;
      cin>>ac>>n;

      for(i=0;i<n;i++)
      cin>>a[i];
      sort(a,a+n);

          if(ac==1)
          {
              printf("Case #%lld: %lld\n",test,n);
              continue;
          }
      else{
      p=ac;
      i=0;
      while(i<n)
      {
          if(p>a[i]){
              p+=a[i];
              i++;
          }
          else if(p+p-1>a[i])
          {
              p=p+p-1+a[i];
              c++;
              i++;
          }
          else
          {
              c++;
              p=p+p-1;
          }
      }
      p=ac;
      i=0;
      while(i<n)
      {
          if(p>a[i])
          {
              p+=a[i];
              i++;
          }
          else if(p+p-1>a[i])
          {
              p=p+p-1+a[i];
              c2++;
              i++;
          }
          else
          {
              c2++;
              n--;
          }
      }
      printf("Case #%lld: %lld\n",test,min(c,c2));
      }
   }

   return 0;
}
