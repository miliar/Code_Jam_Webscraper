#include <cstdio>

using namespace std;

int find_first(int n) {
  int digits = 0;
  int current = n;
  while (true) {
    int test = current;
    while (test > 0) {
      digits |= 1 << (test%10);
      test /= 10;
    }
    if (digits == (1 << 10) - 1) {
      return current;
    }
    current += n;
  }
}

int main(int argc, char *argv[]) {
  int t;
  scanf("%d", &t);
  for (int i = 0; i < t; i++) {
    int n;
    scanf("%d", &n);
    if (n == 0) {
      printf("Case #%d: INSOMNIA\n", i+1);
      continue;
    }
    printf("Case #%d: %d\n", i+1, find_first(n));
  }
}
