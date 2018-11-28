#include <iostream>
#include <string>
#include <stdio.h>


namespace {
  using namespace std;
  int T;
  int Smax;
  string S;

  void input() {
    cin >> Smax;
    cin >> S;
  }

  void solve(int case_num) {
    int answer = 0;
    int sum = 0;
    for (int i = 0; i <= Smax; ++i) {
      const int s = S[i] - '0';
      if (sum < i) {
        answer += i - sum;
        sum += i - sum;
      }
      sum += s;
    }
    printf("Case #%d: %d\n", case_num, answer);
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
