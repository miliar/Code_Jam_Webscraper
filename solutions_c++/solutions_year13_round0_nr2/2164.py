#include <stdio.h>


int main() {
  int T;
  scanf(" %d",&T);
  for(int t=1; t<=T; t++) {
    int N,M;
    int grass[100][100];
    int min_line[100];
    int min_col[100];
    for(int i=0; i<100; i++) {
      min_line[i] = 0;
      min_col[i] = 0;
    }
    
    scanf(" %d %d", &N, &M);
    for (int i=0; i<N; i++) {
      for(int j=0; j<M; j++) {
        scanf(" %d", &grass[i][j]);
        if (grass[i][j] > min_line[i]) {
          min_line[i] = grass[i][j];
        }
        if (grass[i][j] > min_col[j]) {
          min_col[j] = grass[i][j];
        }
      }
    }
    
    int result = 0;
    for (int i=0; i<N; i++) {
      for (int j=0; j<M; j++) {
        if (grass[i][j] < min_line[i] && grass[i][j] < min_col[j]) {
          result = 1;
        }
      }
    }
    
    printf("Case #%d: ",t);
    if (result == 0) {
      printf("YES\n");
    } else {
      printf("NO\n");
    }
    
  }
}
