#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <map>
#include <vector>
#include <string>
#include <cassert>

#define MIN(a,b) ((a) < (b) ? (a) : (b))

using namespace std;

int lawn[120][120];
int M, N;

int col_mow[120];
int row_mow[120];

int row_max (int i) {
  int max = -1;
  for (int j=0; j<M; j++) {
    if (max < lawn[i][j])
      max = lawn[i][j];
  }
  return max;
}

int col_max (int i) {
  int max = -1;
  for (int j=0; j<N; j++) {
    if (max < lawn[j][i])
      max = lawn[j][i];
  }
  return max;
}

int main () {
  int T;
  scanf ("%d", &T);

  for (int i=0; i<T; i++) {
    scanf ("%d %d", &N, &M);
    
    for (int j = 0; j < N; j++) {
      for (int k = 0; k < M; k++) {
        scanf ("%d", &lawn[j][k]);
      }
    }

    for (int j=0; j<N; j++) {
      row_mow[j] = row_max(j);
    }
    for (int j=0; j<M; j++) {
      col_mow[j] = col_max(j);
    }
    bool okay = true;
    for (int j = 0; j < N; j++) {
      for (int k=0; k<M; k++) {
        if (lawn[j][k] != MIN(row_mow[j], col_mow[k])) {
          okay = false;
          goto done;
        }
      }
    }
    done:
    cout << "Case #" << (i + 1) << ": " << (okay ? "YES" : "NO") << endl;
  }

  return 0;
}
