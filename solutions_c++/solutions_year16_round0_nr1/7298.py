#include <cmath>
#include <cstdio>
#include <vector>
#include <stdio.h>
#include <algorithm>
typedef long long int big;
using namespace std;
int main() 
{
   big t,n,i,w,m=0,count,r;
    big a[10];
        scanf("%lld",&t);
    for(w=1;w<=t;w++)
        {
          scanf("%lld",&n);
          if(n==0)
            printf("Case #%lld: INSOMNIA\n",w);
          else
              {
              for(i=0;i<10;i++)
                a[i]=0;
              count=0;
              r=1;
           while(count!=10)
           {
             count=0;
             m=n*r;
             r++;
             while(m!=0)
             {
                 a[m%10]=1;
                 m/=10;
             }
             for(i=0;i<10;i++)
             {
                 if(a[i]==1)
                     count++;
             }
           }
              printf("Case #%lld: %lld\n",w,(r-1)*n);
          }
        }
    

    return 0;
}