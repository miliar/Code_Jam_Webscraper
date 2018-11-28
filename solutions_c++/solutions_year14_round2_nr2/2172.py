#include<iostream>
#include<string.h>
#include<list>
#include<cmath>
#include<cstdio>
#include<fstream>
int main()
{
  freopen("B-small-attempt1.in","r",stdin);
  freopen("B.txt","w",stdout);
  int T;
  scanf("%d",&T);
  for(int t=0;t<T;++t)
  {
  
  int A;
  int B;
  int K;
  scanf("%d",&A);
  scanf("%d",&B);
  scanf("%d",&K);  
  int sum=0;
  for(int i=0;i<B;++i)
  for(int j=0;j<A;++j)
  {if((i&j)<K)
  ++sum;
  }
	printf("Case #%d: %d\n",t+1,sum) ;
}
}
