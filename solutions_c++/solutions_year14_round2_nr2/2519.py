using namespace std;
#include<iostream>
#include<stdio.h>

long long A, B, K;
long long i,j;
int main()
{
freopen ("B-small-attempt0.in","r",stdin);
freopen ("B-small-attempt0.out","w",stdout);

long t;
cin>>t;
for(long k=1;k<=t;k++)
{
  cin >>A>>B>>K;
  
  long long res=0;
  
  for(i=0;i<A;i++)
  {
    for(j=0;j<B;j++)
    {
       if((i&j)<K)
         res++;
    } 
  } 
  printf("Case #%d: %lld\n",k,res);
}
}

