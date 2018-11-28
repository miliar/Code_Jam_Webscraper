#include <cstdio>

int T,K,C,S;


void process(int k, int c, int s){
  if(c == 1){
    if(s >= k){
      for(int i=1;i<=k;i++)
        printf(" %d",i);
      printf("\n");
    }
    else
      printf(" IMPOSSIBLE\n");
  }
  else{
    if(s < (k+1)/2){
      printf(" IMPOSSIBLE\n");
    }
    else{
      int n = (k+1) / 2;
      for(int i=1;i<=n;i++){  // when n % 2 == 1
        int one = (i-1) * 2 + 1;
        int two = one + 1;
        int target = (i-1) * 2 * k + two;
        if(two > k)
          target = k;
        printf(" %d", target);
      }
      printf("\n");
    }
  }
}

int main(){
  scanf("%d",&T);

  for(int i=0;i<T;i++){
    scanf("%d %d %d",&K,&C,&S);
    printf("Case #%d:",i+1);
    process(K,C,S);
  }
}