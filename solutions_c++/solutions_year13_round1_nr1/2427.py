#include<cstdio>
#include<iostream>
#include<cmath>
using namespace std;
int main()
{
  long long int r,t,i,j=1,k,count,test;
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  scanf("%lld",&test);
  while(test--)
  {
    count=0;
    scanf("%lld %lld",&r,&t);
    k=((r+1)*(r+1))-(r*r);
    while(k<=t)
    {
      count++;
      t=t-k;
      r=r+2;
      k=((r+1)*(r+1))-(r*r);
    }
    printf("Case #%lld: %lld\n",j++,count);
  }
  return 0;
}
