#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <set>
using namespace std;

int main() {
  int T, TC = 1, n;
  int a[4], mark[17];
  scanf("%d", &T);
  while (T--) {
    memset(mark, 0, sizeof(mark));
    scanf("%d", &n);
    for (int i=0; i<4; i++) {
      for (int j=0; j<4; j++) {
        scanf("%d", &a[j]);
        if (i==n-1) {
          mark[a[j]] = 1;
        }
      }
    }
    int ans = -1;
    scanf("%d", &n);
    for (int i=0; i<4; i++) {
      for (int j=0; j<4; j++) {
        scanf("%d", &a[j]);
        if (i==n-1 && mark[a[j]] == 1) {
          if (ans == -1) ans = a[j];
          else ans = -2;
        }
      }
    }
    printf("Case #%d: ", TC++);
    if (ans == -1) puts("Volunteer cheated!");
    else if (ans == -2) puts("Bad magician!");
    else printf("%d\n", ans);
  }
}