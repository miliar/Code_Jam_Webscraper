#include<cstdio>
#include<iostream>
#include<vector>

using namespace std;

short n, i;
char A[101], B[101];
short C[100][100], D[100];

void f(char *A, short *C) {
  char _[101];
  scanf("%s", _);
  A[0] = _[0];
  C[0] = 1;
  short j = 0;
  for(char *i = _+1; *i; i++)
    if(*i == A[j])
      C[j]++;
    else {
      A[++j] = *i;
      C[j] = 1;
    }
  A[++j] = '\0';
}

int main() {
  short nCase;
  scanf("%hd", &nCase);
  for(short iCase = 1; iCase<=nCase; iCase++) {
    bool mark = 1;
    scanf("%hd", &n);
    f(A, C[0]);
    for(int i = 1; i<n; i++) {
      f(B, C[i]);
      if(strcmp(A, B)) {
        mark = 0;
        printf("Case #%hd: Fegla Won\n", iCase);
        break;
      }
    }
    if(!mark)
      continue;
    int res = 0;
    for(i = 0; A[i]; i++) {
      for(int j = 0; j<n; j++)
        D[j] = C[j][i];
      sort(D, D+n);
      short median = D[n>>1];
      for(short j = 0; j<n; j++)
        res += abs(median-D[j]);
    }
    printf("Case #%hd: %d\n", iCase,  res);
  }
  return 0;
}