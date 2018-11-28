#include <cstdio>
#include <cstring>

inline int max(int a, int b) { return (a>b)?a:b; }

bool solve() {
  int N, M, A[110][110], colmax[110], rowmax[110];
  scanf("%d %d", &N, &M);

  for(int i=1;i<=N;i++) {
    for(int j=1;j<=M;j++) {
      scanf("%d", &A[i][j]);
    }
  }

  for(int i=1;i<=N;i++) {
    rowmax[i] = 1;
    for(int j=1;j<=M;j++) rowmax[i] = max(rowmax[i], A[i][j]);
  }

  for(int j=1;j<=M;j++) {
    colmax[j] = 1;
    for(int i=1;i<=N;i++) colmax[j] = max(colmax[j], A[i][j]);
  }
  
  for(int i=1;i<=N;i++) {
    for(int j=1;j<=M;j++) {
      if(A[i][j] < rowmax[i] && A[i][j] < colmax[j]) return false;
    }
  }

  return true;
}

int main() {
  int T;
  scanf("%d", &T);

  for(int t=1;t<=T;t++)
    printf("Case #%d: %s\n", t, solve()?"YES":"NO");

  return 0;
}
