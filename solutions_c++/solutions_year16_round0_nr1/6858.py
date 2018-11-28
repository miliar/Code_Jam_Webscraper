#include<cstdio>
#include<cstring>
#include<cstdlib>
bool hit[200];

bool fill(int x){
  while(x > 0){
    hit[x%10] = true;
    x/=10;
  }
  for(int i =0; i <10;i++){
    if (!hit[i])
      return false;
  }
  return true;
}

void work(){
  int N;
  scanf("%d",&N);
  memset(hit,0,sizeof(hit));
  for(int i = 1; i <=10000;i++){
    if (fill(i*N)){
      printf("%d\n", i*N);
      return;
    }
  }
  printf("INSOMNIA\n");
}
int main()
{
  int K;
  scanf("%d",&K);
  for(int i =1; i <=K;i++){
    printf("Case #%d: ",i);
    work();
  }
}
