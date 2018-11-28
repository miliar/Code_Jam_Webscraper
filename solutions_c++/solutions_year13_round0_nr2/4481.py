#include <stdio.h>
#include <string>
#include <stdlib.h>
#include <iostream>

using namespace std;

void go(int tc) {
  int w, h;
  cin >> h >> w;
  int map[h][w];
  for (int i=0; i<h; i++) {
    for (int j=0; j<w; j++) {
      cin >> map[i][j];
    }
  }

  for (int i=0; i<h; i++) {
    for (int j=0; j<w; j++) {
      int num = map[i][j];

      bool row = true;
      bool col = true;

      for (int k=0; k<w && row; k++)
        if (map[i][k] > num) row = false;
      for (int k=0; k<h && col; k++)
        if (map[k][j] > num) col = false;
      if (!row && !col) {
        printf("Case #%d: NO\n", tc);
        return;
      }
    }
  }

  printf("Case #%d: YES\n", tc);
}

int main() {
  int tc;
  cin >> tc;
  for (int i=0; i<tc; i++) {
    go(i+1);
  }
}

