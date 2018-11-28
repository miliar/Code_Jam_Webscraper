#include<stdio.h>
#include<string.h>
#include<vector>
#include<iostream>

#include<algorithm>
#include<set>
#define max 2000000
using namespace std;

typedef long long int ll;



int main()
{ll i,j,k,t,n,m,mini;
char c;
scanf("%lld",&t);
for(i=1;i<=t;i++)
{mini=0;
    scanf("%lld%c%lld",&n,&c,&m);
    
    if(m%2!=0 && m!=1)
    printf("Case #%lld: impossible\n",i);
    else if(n>m)
    printf("Case #%lld: impossible\n",i);
    else
    {
    while(m!=n)
    {
    if(m>n)
    {if(m%2!=0)
    {printf("Case #%lld: impossible\n",i);
    goto end;
    }
           m=m/2;mini++;}
    else
   { n=n/2;
    mini--;
    }
    }
   
     printf("Case #%lld: %lld\n",i,mini);   
    
        }   
         end:;   }

          return 0;
    }
