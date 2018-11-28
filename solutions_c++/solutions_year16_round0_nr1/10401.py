#include <cstdio>

int T, N;

int used[11];

int mark(int num, int round) {
  int tmp = 0;
  while (num) {
    int digit = num % 10;
    if (used[digit] != round) {
      used[digit] = round;
      tmp++;
    }
    num /= 10;
  }
  return tmp;
}

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    scanf("%d", &N);
    printf("Case #%d: ", t);
    if (N == 0) {
      puts("INSOMNIA");
      continue;
    }
    int sum = 0, tmp = N;
    while (sum < 10) {
      sum += mark(tmp, t);
      tmp += N;
    }
    printf("%d\n", tmp - N);
  }
  return 0;
}
