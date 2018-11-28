#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#define forn(n) for(int i=0;i<n;i++)
typedef long long LL;
int barbers[1000];
using namespace std;
int solve(int case_num){
  char plus_or_minus;
  plus_or_minus=getchar();
  char current = plus_or_minus;
  int result = 0;
  while ((plus_or_minus=getchar()) != '\n'){
    if (current != plus_or_minus){
      current = plus_or_minus;
      result++;
    }
  }
  if (current == '-') result++;
  printf("Case #%d: %d\n", case_num, result);
  return 0;
}

int main(){
  int T, i;
  scanf("%d", &T);
  getchar();
  for (i = 1; i<=T; ++i )
    solve(i);
  return 0;
}
