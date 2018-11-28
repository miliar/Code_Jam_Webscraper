#include <bits/stdc++.h>
using namespace std;

const int MAXA = 2505;
int _T;
int N, X, ok[MAXA];

int main(){
  scanf("%d", &_T);
  for(int _t = 1; _t <= _T; _t++){
    printf("Case #%d:", _t);
    scanf("%d", &N);
    fill(ok, ok + MAXA, 0);
    for(int i = 0; i < 2 * N - 1; i++){
      for(int j = 0; j < N; j++){
        scanf("%d", &X);
        ok[X] ^= 1;
      }
    }
    for(int i = 0; i < MAXA; i++){
      if(ok[i]){
        printf(" %d", i);
      }
    }
    printf("\n");
  }
}
