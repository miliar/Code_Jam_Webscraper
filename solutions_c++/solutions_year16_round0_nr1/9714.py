#include <stdio.h>
#include <string.h>

int T;
int chk[10];

int main() {
  int TT;
  long long n,m,k;
  int i;
  scanf("%d",&T);
  for(TT=1;TT<=T;TT++){
    scanf("%lld",&n);
    if(n==0){
      printf("Case #%d: INSOMNIA\n",TT);
      continue;
    }
    memset(chk,0,sizeof(chk));
    for(m=1;;m++){
      k=n*m;
      while(k){
        chk[k%10]=1;
        k/=10;
      }
      for(i=0;i<10;i++)if(!chk[i])break;
      if(i==10)break;
    }
    printf("Case #%d: %lld\n",TT,n*m);
  }
}
