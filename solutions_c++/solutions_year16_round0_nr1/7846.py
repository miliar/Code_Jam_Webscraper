#include <stdio.h>
#include <string>
#include <iostream>
#include <algorithm>
#include <math.h>
#define MOD 1000000007
#define ll long long
#define slld(t) scanf("%lld",&t)
#define sd(t) scanf("%d",&t)
#define pd(t) printf("%d\n",t)
#define plld(t) printf("%lld\n",t)
using namespace std;
int main()
{
  int t;
  sd(t);
  for(int j=1;j<=t;j++)
  {  
    int n;
    int a[11]={0};
    int count=0;
    sd(n);
    if (n==0) printf("Case #%d: INSOMNIA\n",j);
    else 
    {
      int i=1,check=0;
      count=0;
      while(check==0)
     { 
      //pd(count);
      count=0;
        int temp = n*i,temp2;
        while(temp)
        {
          temp2 = temp%10;
          a[temp2]++;
          temp/=10;
        }
        i++;
        for(int k=0;k<10;k++)
        {
          if(a[k]>0) count++;
        }
        if(count>9) check=1;
      }
      //pd(i);
      i--;
      n=n*i;
      printf("Case #%d: %d\n",j,n);
    }  
  }
}
  