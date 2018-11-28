#include<iostream>
#include<stdio.h>
#include<math.h>

using namespace std;
#define ll long long int
int main()
{
ll t,n,i,j,pt,nt;
int fl;
scanf("%lld",&t);

for(i=1;i<=t;i++)
{
  fl=0;
  int a[10]={};
  scanf("%lld",&n);
  j=1;
  while(1)
  {
    nt=n*j;
    if(pt==nt)
    {
      fl=1;
      break;
    }
    pt=nt;
      while(nt>0)
      {
        a[nt%10]++;
        nt/=10;
      }
      if(a[0]>0 &&a[1]>0 &&a[2]>0 &&a[3]>0 &&a[4]>0 &&a[5]>0 &&a[6]>0 &&a[7]>0 &&a[8]>0 &&a[9]>0)
        {
          break;
        }
        j++;
  }
printf("Case #%lld: ",i);
if(fl==1)
{
  printf("INSOMNIA");
}
else
{
  printf("%lld",pt);
}
if(i!=t)
  printf("\n");
}

  return 0;
}
