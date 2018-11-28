#include <iostream>
#include <algorithm>
using namespace std;

int tag[10];
int maxt=0;

void deal(int  N)
{
  int  tmp;
  int  t=0;
  int count=0;
  int ans=0;
  for(int i=0;i<10;++i) tag[i]=0;
  while(count<10)
  {
    ++t;
    ans+=N;
    tmp=ans;
    while(tmp)
    {
      if(tag[tmp%10]==0)
      {
	  tag[tmp%10]=1;
	  count++;
      }
      tmp/=10;
    }
  }
  if(t>maxt) maxt=t;
  printf("%d\n",ans);
  // printf("N=%d: ans=%d t=%d\n",N,ans,t);
}

int main()
{
  int  T,K,C,S;
  scanf("%d",&T);
  // fill_com(15);
  for(int i=1;i<=T;++i)
  {
    printf("Case #%d:", i);
    scanf("%d%d%d",&K,&C,&S);
    for(int j=1;j<=K;++j)
      {
	printf(" %d",j);
      }
    printf("\n");
    
  }
  //printf("%d\n",maxt);
  return 0;
}
