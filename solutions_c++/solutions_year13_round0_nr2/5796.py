#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int h[100][100];
int maxLeft[100][100];
int maxUp[100][100];
int maxRight[100][100];
int maxDown[100][100];
bool ok[100][100];

const char* solve() {
  memset(maxLeft, 0, sizeof(maxLeft));
  memset(maxRight, 0, sizeof(maxLeft));
  memset(maxDown, 0, sizeof(maxLeft));
  memset(maxUp, 0, sizeof(maxLeft));

  int n, m;
  scanf("%d %d", &n, &m);
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < m; j++) {
      scanf("%d", &h[i][j]);
      if (j) {
        maxLeft[i][j] = max(maxLeft[i][j-1], h[i][j]);
      } else {
        maxLeft[i][j] = h[i][j];
      }

      if (i) {
        maxUp[i][j] = max(maxUp[i-1][j], h[i][j]);
      } else {
        maxUp[i][j] = h[i][j];
      }
    }
  }

  for(int i = n-1; i >= 0; i--) {
    for(int j = m-1; j >= 0; j--) {
      if (j < m-1) {
        maxRight[i][j] = max(maxRight[i][j+1], h[i][j]);
      } else {
        maxRight[i][j] = h[i][j];
      }

      if (i < n-1) {
        maxDown[i][j] = max(maxDown[i+1][j], h[i][j]);
      } else {
        maxDown[i][j] = h[i][j];
      }
    }
  }

  for(int i = 0; i < n; i++) {
    for(int j = 0; j < m; j++) {
      int curr = h[i][j];
      bool ok = 0;

      if(!j || maxLeft[i][j-1] <= curr) {
        if(j == m-1 || maxRight[i][j+1] <= curr) {
          ok = 1;
        }
      }

      if(i == 0 || maxUp[i-1][j] <= curr) {
        if(i == n-1 || maxDown[i+1][j] <= curr) {
          ok = 1;
        }
      }

      if(!ok) return "NO";
    }
  }
  return "YES";
}

int main() {
  int t;
  scanf("%d", &t);
  for(int i = 0; i < t; i++) {
    printf("Case #%d: %s\n", i+1, solve());
  }
  return 0;
}
