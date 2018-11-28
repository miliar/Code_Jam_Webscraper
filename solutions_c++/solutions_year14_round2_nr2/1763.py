#include <bits/stdc++.h>

using namespace std;

int64_t A, B, K;

void Input() {
  cin >> A >> B >> K;
}

void Solve() {
  int res = 0;
  for (int a = 0; a < A; a++) {
    for (int b = 0; b < B; b++) {
      int win = a & b;
      if (win < K) res++;
    }
  }
  printf("%d", res);
}

int main(int argc, char **argv) {
  int T;
  scanf("%d", &T);

  for (int test_case = 1; test_case <= T; ++test_case) {
    Input();
    printf("Case #%d: ", test_case);
    Solve();
    printf("\n");
  }
  return 0;
}
