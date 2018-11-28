#include <iostream>

using namespace std;

#define MAXP 1024
#define MAXD 1024

int p[MAXD];
int d;
int maxp = 0;

int test(int n) {
  int time = 0;
  for (int i = 0; i < d; i++) {
    int left = p[i];
    while (left > n) {
      time++;
      left -= n;
    }
  }
  return time + n;
}

int main() {
  int T;
  scanf("%d\n", &T);
  for (int t = 1; t <= T; t++) {
    maxp = 0;
    scanf("%d", &d);
    for (int i = 0; i < d; i++) {
      scanf("%d", &(p[i]));
      maxp = max(maxp, p[i]);
    }
    int time = MAXP;
    for (int i = 1; i <= maxp; i++)
      time = min(time, test(i));
    printf("Case #%d: %d\n", t, time);
  }
  return 0;
}
