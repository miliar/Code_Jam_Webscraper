#include <iostream>
#include <string>
#include <set>
using namespace std;


string solve(int N) {
  if (N == 0) return "INSOMNIA";
  set<int> d;
  for (int i = 1; ; ++i) {
    int x = i * N;
    for (int y = x; y > 0; y /= 10) {
      d.insert(y % 10);
    }
    if (d.size() == 10) return to_string(x);
  }
}

int main() {
  int T; cin >> T;
  for (int tt = 1; tt <= T; ++tt) {
    int N; cin >> N;
    cout << "Case #" << tt << ": " << solve(N) << "\n";
  }
  return 0;
}
