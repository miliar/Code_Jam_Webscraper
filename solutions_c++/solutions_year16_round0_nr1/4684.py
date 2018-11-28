#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#define forn(n) for(int i=0;i<n;i++)
typedef long long LL;
int barbers[1000];
using namespace std;
int N;
int hit_count;
int digit[10];
void init(){
  hit_count = 0;
  int i;
  for (i =0 ;i < 10; i++){
    digit[i] = 0;
  }
}

void check_digit(LL target){
  int remainder;
  do{
    remainder = target % 10;
    target = target / 10;
    if (digit[remainder] == 0) {
      digit[remainder] = 1;
      hit_count++;
    }
  }while(target != 0);
}
int solve(int case_num){
  cin >> N;
  init();
  if (N == 0){
    printf("Case #%d: INSOMNIA\n", case_num);
    return 0 ;
  }
  int iter = 1;
  LL result;
  while (hit_count != 10){
    result = N * iter;
    check_digit(result);
    iter ++;
  }
  printf("Case #%d: %lld\n", case_num, result);
  return 0 ;
}

int main(){
  int T, i;
  scanf("%d", &T);
  for (i = 1; i<=T; ++i )
    solve(i);
  return 0;
}
