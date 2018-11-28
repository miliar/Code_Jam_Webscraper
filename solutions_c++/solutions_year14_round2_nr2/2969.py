#include<iostream>
#include<stdio.h>
using namespace std;
int a,b,k,t;

int main()
{long long int count,sum;
int p;
  //  freopen("ans2.txt","w",stdout);
   // freopen("B-small-attempt0.in","r",stdin);
    scanf("%d",&t);
    for(int p=1;p<t;p++)
    {
          int i,j;
          sum=0;
          count=0;
          scanf("%d %d %d",&a,&b,&k);
          for(i=0;i<a;i++)
          {
              for(j=0;j<b;j++)
              {
                  if((i&j)<k)
                  count++;
              }
          }
          printf("Case #%d: %lld\n",p,count);
    }
    return 0;
}
