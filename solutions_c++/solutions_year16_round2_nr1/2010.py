#include <bits/stdc++.h>

using namespace std;

int O[] = {0, 2, 4, 1, 3, 5, 6, 7, 8, 9};
const char U[] = "ZOWRUFXSHI";
const char *A[10] = {
  "ZERO",
  "ONE",
  "TWO",
  "THREE",
  "FOUR",
  "FIVE",
  "SIX",
  "SEVEN",
  "EIGHT",
  "NINE"
};

void solveCase()
{
  char S[2222];
  char* ptr = S;
  int temp[200] = {0,};
  int answer[10] = {0,};
  scanf("%s\n", S);

  while (*ptr) {
    temp[*ptr]++;
    ptr++;
  }

  for (int i=0; i<=9; i++) {
    int c = O[i];
    answer[c] = temp[U[c]];
    for (const char *p = A[c]; *p; p++) {
      temp[*p] -= answer[c];
    }
  }

  for (int i=0; i<=9; i++) {
    for (int j=0; j<answer[i]; j++) {
      printf("%d", i);
    }
  }
  printf("\n");
}

int main ()
{
  int T;
  scanf("%d\n", &T);
  for (int i=1; i<=T; i++) {
    printf("Case #%d: ", i);
    solveCase();
  }
  return 0;
}
