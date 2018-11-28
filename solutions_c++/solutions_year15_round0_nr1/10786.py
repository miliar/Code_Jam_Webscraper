#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char ans[10];


int main() {
  // Precompute all answers.


  // Process queries.
  int N;
  scanf(" %d", &N);
  for (int prob = 1; prob <= N; prob++) {
    int n, sum=0, m=0; 
    scanf(" %d %s", &n, ans);
    int num;
    for(int i=0;i<n+1;i++){
      num=ans[i]-'0';
      if(num>0 && sum<i){
        m+=i-sum;
        sum+=m;
      }
       sum+=num;

    }
    printf("Case #%d: %d\n", prob, m);
  }

  return 0;
}