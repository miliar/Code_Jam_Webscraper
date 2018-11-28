#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<queue>
#include<cstring>
#include<cstdlib>
#include<cmath>
using namespace std;
int main(){
  int T, N;
  vector<bool> digit(10);
  int digitChange = 0;
  scanf("%d", &T);
  for(int i=1; i<=T; i++){
    digitChange = 0;
    for(int j=0; j<10; j++)
      digit[j] = false;
    scanf("%d", &N);
    if(N == 0){
      printf("Case #%d: INSOMNIA\n", i);
      continue;
    }
    int k = 0;
    int n = 0;
    do{
      n += N;
      k = n;
      for(;k >= 1;){
        if(digit[k % 10] == false){
          digitChange++;
          digit[k % 10] = true;
        }
        k /= 10;
      }
      if(digitChange == 10)
        break;
    }while(1);
    printf("Case #%d: %d\n", i, n);
  }
  return 0;
}
