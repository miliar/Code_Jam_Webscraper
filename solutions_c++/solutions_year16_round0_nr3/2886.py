#include <iostream>
#include <string.h>
#include <stdio.h>
#include <math.h>
using namespace std;
unsigned long long T,N,J;
unsigned long long d[20];
unsigned long long jud(unsigned long long x)
{
  unsigned long long i;
  unsigned long long s = sqrt((double)x) + 1;
  if(x==2)
    return 0;
  else
  {
    for(i=2; i<s&&i<x; i++)
    {
      if(x%i==0)
        return i;
    }
    return 0;
  }
}
unsigned long long trans(unsigned long long x, unsigned long long base)
{
  unsigned long long y=0;
  unsigned long long tbase = 1;
  while(x!=0)
  {
    y+=(x&1)*tbase;
    tbase *= base;
    x=x>>1;
  }
  return y;
}
int main()
{
  int t;
  unsigned long long i, j, max, b, k;
  unsigned long long a;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    cin>>N>>J;
    printf("Case #%d:\n",t);
    a   = 1+(1<<(N-1));
    max = (N==32)?0xffffffff:((1<<N)-1);
    for (j=0; j<J&&a<=max; a+=2)
    {
      for(b=2; b<=10; b++)
        if((d[b]=jud(trans(a, b)))==0)
          break;
      if(b==11)
      {
        for (i=1<<(N-1),k=N-1; i>0; i=i>>1,k--)
          cout<<((i&a)>>k);
        for (i=2; i<=10; i++)
          cout<<" "<<d[i];
        printf("\n");
        j++;
      }
    }
  }
  return 0;
}