#include <iostream>
#include <fstream>

using namespace std;

const int LIM = 1001;

int p[LIM];

int main() {
  ifstream cin("input.txt");
  ofstream cout("output.txt");
  int tests;
  cin >> tests;
  for (int test = 0; test < tests; ++test) {
    int d;
    cin >> d;
    fill(p, p + LIM, 0);
    for (int i = 0; i < d; ++i) {
      cin >> p[i];
    }
    int ans = LIM;
    for (int i = 1; i < LIM; ++i) {
      int cur_ans = 0, steps = 0;
      for (int j = 0; j < d; ++j) {
        if (p[j] > i) {
          int tmp = p[j] - i;
          cur_ans += tmp / i;
          tmp %= i;
          if (tmp != 0)
            ++cur_ans;
        }
        steps = max(steps, p[j]);
      }
      steps = min(steps, i);
      cur_ans += steps;
      ans = min(ans, cur_ans);
    }
    cout << "Case #" << test + 1 << ": " << ans << '\n';
  }
  return 0;
}
