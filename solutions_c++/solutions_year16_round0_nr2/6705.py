#include<stdio.h>

int main(){
  int i, n, total;
  char curr, prev;
  scanf("%d\n", &n);
  for(int i = 1; i < n+1; i++){
    total = 0;
    prev = curr = getchar();
    while(1){
      if(curr == '\n'){
        if(prev == '-'){
          total++;
        }
        printf("Case #%d: %d\n", i, total);
        break;
      }
      if(prev!=curr){
        total++;
      }
      prev = curr;
      curr = getchar();
    }
  }
  return 0;
}