#include <stdio.h>

int T;
int N,M;
int A[110][110];
int v[110][110];

const char* solve() {
  for (int ix = 0; ix < N; ++ix) {
    for (int jx = 0; jx < M; ++jx) {
      v[ix][jx] = 0;
    }
  }
 
  for (int ix = 0; ix < N; ++ix) {
    int max = 0;
    for (int jx = 0; jx < M; ++jx) {
      if (max < A[ix][jx]) {
        max = A[ix][jx];
      }
    }

    for (int jx = 0; jx < M; ++jx) {
      if (A[ix][jx] == max) {
        v[ix][jx] = 1;
      }
    }
  }

  for (int jx = 0; jx < M; ++jx) {
    int max = 0;
    for (int ix = 0; ix < N; ++ix) {
      if (max < A[ix][jx]) {
        max = A[ix][jx];
      }
    }
    
    for (int ix = 0; ix < N; ++ix) {
      if (A[ix][jx] == max) {
        v[ix][jx] = 1;
      }
    }
  }

  for (int ix = 0; ix < N; ++ix) {
    for (int jx = 0; jx < M; ++jx) {
      if (v[ix][jx] == 0 ) {
        return "NO";
      }
    }
  }

  return "YES";
}

int main () {
  scanf("%d", &T);

  for (int i = 0; i < T; ++i) {
    scanf("%d %d", &N, &M);
    for (int ix = 0; ix < N; ++ix) {
      for (int jx = 0; jx < M; ++jx) {
        scanf("%d", &A[ix][jx]);
      }
    }

    printf("Case #%d: %s\n", i+1, solve());
  }
  
  return 0;
}
