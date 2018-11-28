#include <cstdio>

using namespace std;

int main(){
  int T,K,C,S;
  
  scanf("%d",&T);
  
  for(int tc = 1;tc <= T;++tc){
    scanf("%d %d %d",&K,&C,&S);
    
    printf("Case #%d:",tc);
    
    if(C == 1){
      if(S < K) printf(" IMPOSSIBLE\n");
      else{
        for(int i = 1;i <= K;++i)
          printf(" %d",i);
        printf("\n");
      }
    }else{
      if(S < (K + 1) / 2) printf(" IMPOSSIBLE\n");
      else{
        for(int i = 0;i < K;i += 2){
          int pos = K * i + i + 1;
          if(i == K - 1 && K % 2 == 1) --pos;
          printf(" %d",pos + 1);
        }
        printf("\n");
      }
    }
  }

  return 0;
}
