#include<cstdio>
#include<iostream>
#include<algorithm>
#define For(i,lb,ub) for(int i=lb;i<ub;i++)
using namespace std;
int main()
{
  int t;
  cin>>t;
  for(int T=1;T<=t;T++)
  {
    char s[1005];
    int smax;
    scanf("%d %s",&smax,s);
    long long int add=0,count=(s[0]-'0');
    For(i,1,smax+1)
    {
      int v = (s[i]-'0');
      if(count<i)
      {
	add+=(i-count);
	count = i;
      }
      count+=v;
    }
    printf("Case #%d: %lld\n",T,add);
  }
  return 0;
}