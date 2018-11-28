#include<bits/stdc++.h>
using namespace std;
int main()
{
  int t;
  scanf("%d",&t);
  for(int j=1;j<=t;j++)
  {
    long long int n;
    scanf("%lld",&n);
    if(n==0)
    {
      printf("Case #%d: INSOMNIA\n",j);
      continue;
    }
    set<int> s;
    for(int i=1;i<100000;i++)
    {
      long long temp=i*n;
      while(temp!=0)
      {
	s.insert(temp%10);
	temp=temp/10;
      }
      if(s.size()==10)
      {
	printf("Case #%d: %lld\n",j,i*n);
	break;
      }
      //printf("%lld ",i*n);
    }
    //printf("\n");
  }
  return 0;
}