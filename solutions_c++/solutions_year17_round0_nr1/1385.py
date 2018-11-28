#include <stdio.h>
#include <cstring>

int n,k;
char arr[1001];

void run(int iter){
  scanf("%s", arr);
  int l = strlen(arr);

  scanf("%d", &k);
  n = 0;
  for(int i=0;i<l;i++){
    if(arr[i] == '+') continue;
    if(i+k-1>=l){
      printf("Case #%d: IMPOSSIBLE\n", iter);
      return;
    }
    n++;
    for(int j = i; j<i+k; j++){
      if(!arr[j]) break;
      arr[j] = arr[j]=='+'?'-':'+';
    }
  }

  printf("Case #%d: %d\n", iter, n);
}

int main(){
  int t;
  scanf("%d", &t);
  for(int i=0;i<t;i++){
    run(i+1);
  }
}
