#include <iostream>
using namespace std;
int  T,K,C,S;

int solve()
{
  if(C*S<K) return 0;
  int  begin=0;
  long long  pos=0;
  for(int j=1;j*C<=K;++j)
  {
    pos=0;
    for(int d=0;d<C;++d)
    {
      pos*=K;
      pos+=begin+d;
    }
    printf(" %lld",pos+1);
    begin+=C;
  }
  if(K%C!=0)
  {
    pos=0;
    for(int d=0;d<C;++d)
    {
      pos*=K;
      if(begin+d<K)
      {	
	  pos+=begin+d;
      }
    }
    printf(" %lld",pos+1);
  }
  printf("\n");
  return 1; 
}
int main()
{

  scanf("%d",&T);
  for(int i=1;i<=T;++i)
  {
    scanf("%d%d%d",&K,&C,&S);
    printf("Case #%d:", i);
    if(solve()==0)
    {
	printf(" IMPOSSIBLE\n");
    }
  }
  //printf("%d\n",maxt);
  return 0;
}
