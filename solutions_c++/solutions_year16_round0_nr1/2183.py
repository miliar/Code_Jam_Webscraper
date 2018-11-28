#include <bits/stdc++.h>
using namespace std;

int _T;
int N, use[10];
long long res;

int main(){
  scanf("%d", &_T);
  for(int _t = 1; _t <= _T; _t++){
    printf("Case #%d: ", _t);
    fill(use, use + 10, 0);
    res = 0;
    scanf("%d", &N);
    if(N == 0){
      printf("INSOMNIA\n");
      continue;
    }
    while(*min_element(use, use + 10) == 0){
      res += N;
      long long k = res;
      while(k > 0){
        use[k % 10] = 1;
        k /= 10;
      }
    }
    printf("%lld\n", res);
  }
}
