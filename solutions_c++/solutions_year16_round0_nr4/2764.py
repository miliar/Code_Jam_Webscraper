#include <iostream>
#include <stdio.h>
using namespace std;
int main()
{
  int T,t,K,C,S;
  unsigned long long kc=1, d, i;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    kc=1;
    cin>>K>>C>>S;
    for(i=0;i<C;i++)
      kc*=K;
    if(K!=1)
      d=(kc-1)/(K-1);
    else
      d=1;
    printf("Case #%d: ",t);
    for(i=1;i<=kc;i+=d)
      cout<<i<<" ";
    cout<<endl;
  }
  return 0;
}
