#include<iostream>
#include<cstdio>
#include<cmath>
#define gi(a) gar=scanf("%d",&a)
#define For(i,lb,ub) for(int i=lb;i<ub;i++)
int gar;
using namespace std;
long long int reverse(long long int a)
{
  long long int r = 0;
  while(a!=0)
  {
    r*=10;
    r+=(a%10);
    a/=10;
  }
  return r;
}
bool ispalin(long long int a)
{
  return (a == reverse(a));
}
int main()
{
  int test;
  int t;
  scanf("%d",&t);
  test = t;
  For(T,1,t+1) 
  {
    long long int a,b;
    scanf("%lld %lld",&a,&b);
    int count = 0;
    for(long long int i=ceil(sqrt(a));i<=floor(sqrt(b));i++){
      if(ispalin(i) && ispalin(i*i))
	count ++;
    }
    printf("Case #%d: %d\n",T,count);
  }
  return 0;
}