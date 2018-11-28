#include <iostream>

using namespace std;

#define SMAX 1024

char line[SMAX];

int main() {
  int T;
  scanf("%d\n", &T);
  for (int t = 1; t <= T; t++) {
    int sm;
    int borr = 0;
    int curr = 0;
    scanf("%d %s\n", &sm, line);
    for (int i = 0; i <= sm; i++) {
      if (curr >= i) {
        curr += (line[i] - '0');
      }
      else {
        borr += i - curr;
        curr += line[i] - '0' + i - curr;
      }
    }
    printf("Case #%d: %d\n", t, borr);
  }
  return 0;
}
