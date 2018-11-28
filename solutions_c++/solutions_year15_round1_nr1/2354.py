#include <iostream>
#include <string>
#include <stdio.h>


namespace {
  using namespace std;
  int T;
  int N;
  int M[1000];

  void input() {
    cin >> N;
    for (int i = 0; i < N; ++i) {
      cin >> M[i];
    }
  }

  void solve(int case_num) {
    int y = 0;
    int max_delta = 0;
    for (int i = 1; i < N; ++i) {
      int delta = M[i - 1] - M[i];
      if (delta > 0) y += delta;
      max_delta = max(max_delta, delta);
    }
    int z = 0;
    for (int i = 0; i < N - 1; ++i) {
      if (max_delta <= M[i]) z += max_delta;
      else z += M[i];
    }
    printf("Case #%d: %d %d\n", case_num, y, z);
  }
}

int main() {
  cin >> T;
  for (int t = 0; t < T; ++t) {
    input();
    solve(t + 1);
  }
  return 0;
}
