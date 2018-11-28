#include <cstdio>

int main(){
  int T,X,R,C,N;
  scanf("%d",&T);
  for(N=1;N<=T;N++){
    scanf("%d %d %d",&X,&R,&C);
    printf("Case #%d: %s\n",N, ((X < 7)&&((R*C)%X == 0)&&(R >= X-1)&&(C >= X-1)) ? "GABRIEL" : "RICHARD");
  }
  return 0;
}
