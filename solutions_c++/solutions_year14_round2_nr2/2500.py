#include <iostream>
#include <cstdio>
#include <cstdlib>

int main(){
  int T,t=0, A, B, i, j, K;
  int a[1000], b[1000];
  scanf("%d", &T);  
  while(t++<T){
    scanf("%d%d%d", &A, &B, &K);
    int count = 0;
    for (i=0;i<A;i++)
      for(j=0;j<B;j++)
      {
	if((i&j)<K)count++;
      }
    printf("Case #%d: %d\n", t, count);
  }
}