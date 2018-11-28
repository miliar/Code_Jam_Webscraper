#include "cstdio"
void proc(int n){
  long long c;
  scanf("%lld",&c);
  if(c==0){
    printf("Case #%d: INSOMNIA",n);
    return;
  }
  int count = 0;
  int tick[10] = {0,0,0,0,0,0,0,0,0,0};
  long long mult = 1;
  while(true){
    long long tmp = c * mult;
    while(tmp>0){
      if(!tick[tmp%10]){
        tick[tmp%10]=1;
        count++;
      }
      tmp/=10;
    }
    if(count==10)break;
    mult++;
  }
  printf("Case #%d: %lld",n,c*mult);
  return;
}
int main(int argc, char const *argv[]) {
  int q;
  scanf("%d",&q);
  for (size_t i = 0; i < q; i++) {
    proc(i+1);
    printf("\n");
  }
  return 0;
}
