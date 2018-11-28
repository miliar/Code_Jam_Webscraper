#include<iostream>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

int main()
{
  int tc;
  scanf("%d",&tc);
  for(int tcc=0;tcc<tc;tcc++)
  {
    char lst[2048];
    int maxshy=0;
    scanf("%d",&maxshy);
    int ans=0;
    int sum=0;
    scanf("%s",lst);
    for(int i=0;i<=maxshy;i++)
    {
      if(i>sum)
      {
        ans+=i-sum;
	sum+=i-sum;
      }
      sum+=lst[i]-'0';
    }
    printf("Case #%d: %d\n",tcc+1,ans);
  }
  return 0;
}
