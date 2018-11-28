#include<stdio.h>
#include<string.h>
#include<vector>
#include<iostream>

#include<algorithm>
#include<set>
#define max 200000
using namespace std;

typedef long long int ll;


int main()
{int i,j,k,t,n,m,l;
scanf("%d",&t);
for(j=1;j<=t;j++)
{int sum=0;
          scanf("%d%d%d",&n,&m,&k);
for(i=0;i<n;i++)
{
                 for(l=0;l<m;l++)
                 {if((i&l)<k)
                 sum++;
                 }
                 }

  printf("Case #%d: %d\n",j,sum); 
                        
}
          return 0;
    }
