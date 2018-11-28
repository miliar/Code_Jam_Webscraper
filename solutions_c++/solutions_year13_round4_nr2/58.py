#include <cstdio>

long long MIN(int n,long long P)
{
  if(!n){
    return 0ll;
  }
  long long K=1ll<<n-1;
  long long A;
  if(P<K){
    A=2*MIN(n-1,P);
  }
  else if(P==2*K){
    A=2*K-1;
  }
  else{
    A=2*K-2;
  }
  return A;
}

int main()
{
  int T;
  scanf("%d",&T);
  for(int C=1;C<=T;C++){
    int n;
    long long P;
    scanf("%d%lld",&n,&P);
    //P--;
    printf("Case #%d: %lld %lld\n",C,P==(1ll<<n)?(1ll<<n)-1:(1ll<<n)-MIN(n,(1ll<<n)-P)-2,MIN(n,P));
  }
  return 0;
}
