#include<deque>
#include<stdio.h>

int main(void) {
  int T = 0;
  int x = 0;
  scanf("%d\n", &T);
  for (int i = 1; i <= T; i++) {
    std::deque<char> d;
    while ((x = getchar()) != EOF) {
      if (x == '\n') {
        break;
      }
      if (d.empty() || *d.begin() <= x) {
        d.push_front(x);
      } else {
        d.push_back(x);
      }
    }
    printf("Case #%d: ", i);
    for (auto it = d.begin(); it != d.end(); ++it) {
      printf("%c", *it);
    }
    printf("\n");
  }
  return 0;
}
