#include<bits/stdc++.h>
using namespace std;
int main()
{ long long int i,j,m,dig,numb,n,t;
  scanf("%lld",&t);
  for(i=1;i<=t;i++)
  { scanf("%lld",&n);
    numb=0;
    if(n==0)
     printf("Case #%lld: INSOMNIA\n",i);
    else
     { j=1;int hash[10]={0};
       while(1)
       { m=n*j;
          if(numb<10)
          {while(m>0)
            { dig=m%10;
              if(hash[dig]==0)
               numb++;
              hash[dig]++;
              m/=10;
            }
          }
          else
           break;
         j++;
       }
       printf("Case #%lld: %lld\n",i,n*(j-1));
     }

  }
return 0;
}
