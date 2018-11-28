#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int T, n;
int dat[20];

int main() {
  scanf("%d", &T);
  for (int ca = 1; ca <= T; ++ca) {
    scanf("%d", &n);
    memset(dat, 0, sizeof(dat));
    for (int i = 1; i <= 4; ++i) {
      for (int j = 1; j <= 4; ++j) {
        int x;
        scanf("%d", &x);
        dat[x] = (i == n);
      }
    }
    scanf("%d", &n);
    int cnt = 0, res;
    for (int i = 1; i <= 4; ++i) {
      for (int j = 1; j <= 4; ++j) {
        int x;
        scanf("%d", &x);
        dat[x] &= (i == n);
        cnt += dat[x];
        if (dat[x]) res = x;
      }
    }

    if (cnt == 1) {
      printf("Case #%d: %d\n", ca, res);
    } else if (cnt) {
      printf("Case #%d: Bad magician!\n", ca); 
    } else {
      printf("Case #%d: Volunteer cheated!\n", ca);
    }
    
  }
  return 0;
}
