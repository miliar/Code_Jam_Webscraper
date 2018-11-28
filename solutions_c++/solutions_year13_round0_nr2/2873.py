#include <iostream>
using namespace std;

int main() {
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    int m, n, H = 0, smallest = 1000;
    scanf("%d %d", &m, &n);
    int a[100][100], mask[100][100];
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        scanf("%d", &a[i][j]);
        mask[i][j] = 1;
        if (a[i][j] > H) H = a[i][j];
        if (a[i][j] < smallest) smallest = a[i][j];
      }
    }
    bool okay = true;
    for (int h = smallest; h <= H; h++) {
      //cout << "h: " << h << endl;
      // check for valid paths on current height
      for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
          if (a[i][j] == h && mask[i][j]) {
            // check horizontal
            bool hor = true;
            for (int y = 0; y < n; y++) {
              if (mask[i][y] && a[i][y] > h) {
                hor = false;
                break;
              }
            }
            // check vert
            bool vert = true;
            for (int x = 0; x < m; x++) {
              if (mask[x][j] && a[x][j] > h) {
                vert = false;
                break;
              }
            }
            if (hor) {
              for (int y = 0; y < n; y++) {
                mask[i][y] = 0;
              }
            } else if (vert) {
              for (int x = 0; x < m; x++) {
                mask[x][j] = 0;
              }
            } else {
              okay = false;
              break;
            }
          }
        }
        if (!okay) break;
      }
    }
    printf("Case #%d: ", t);
    if (okay) printf("YES\n");
    else printf("NO\n");
  }
  return 0;
}