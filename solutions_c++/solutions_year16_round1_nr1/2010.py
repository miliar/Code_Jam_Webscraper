#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#define forn(n) for(int i=0;i<n;i++)
#define SIZE 2010

typedef long long LL;
using namespace std;
int head, tail;
char head_char;
char result_pool[SIZE];
int size_of_S;
void init(){
  int i;
  for (i =0 ;i < SIZE; i++){
    result_pool[i] = '0';
  }
  head = 1004;
  tail = 1006;
  size_of_S = 1;
  head_char = '0';
}
void print_result(){
  int i ;
  for (i=head+1;i<=(size_of_S+head);i++){
    cout << result_pool[i];
  }
  printf("\n");
  return;
}
int solve(int case_num){
  init();
  char tmp;
  result_pool[1005] = getchar();
  head_char = result_pool[1005];
  while ((tmp=getchar()) != '\n'){
    size_of_S++;
    if (tmp < head_char){
      result_pool[tail] = tmp;
      tail++;
    }else{
      result_pool[head] = tmp;
      head--;
      head_char = tmp;
    }
  }
  printf("Case #%d: ", case_num);
  print_result();
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
