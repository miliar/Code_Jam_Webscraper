#include<stdio.h>
#include<iostream>
using namespace std;

bool is_complete(bool check_ary[])
{
  for(int i = 0; i < 10; i++){
    if (check_ary[i] == false) return false;
  }
  return true;
}

int count_cheep(int num)
{
  int last_num, i;
    i = 1;
  bool check_ary[10] = {false};
  while(true){
    int target = num * i;
    while(true){
      if(target == 0) break;
      int amari = target % 10;
      check_ary[amari] = true;
      target = target / 10;
    }
    bool check = is_complete(check_ary);
    if(check == true) return num * i;
    i++;

  }
  return last_num;
}

int main()
{
  int N, A[100];

  scanf("%d", &N);
  for (int i = 0; i < N; i++){
    scanf("%d", &A[i]);
  }

  for(int i = 0; i < N; i++){
    if(A[i] == 0){
      printf("Case #%d: INSOMNIA\n", i + 1);
      continue;
    }
    int result = count_cheep(A[i]);
    printf("Case #%d: %d\n", i + 1, result);
  }
  return 0;
}