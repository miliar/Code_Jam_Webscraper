#include <cstdint>
#include <iostream>
#include <string>
using namespace std;

// BEGIN CUT HERE
// helper functions begin
// END CUT HERE
template <typename T> inline T set_bit(const T &x, int index) {
  return x | ((T)1 << index);
}
// BEGIN CUT HERE
// helper functions end
// END CUT HERE

string solve() {
  int64_t N, X = 0;
  cin >> N;
  int mask = 0;
  for (int i=0; i<10000; ++i) {
    X += N;
    int64_t Y = X;
    while (Y > 0) {
      mask = set_bit(mask, Y%10);
      Y /= 10;
    }
    if (mask == (1<<10)-1) {
      return std::to_string(X);
    }
  }
  return "INSOMNIA";
}

int main() {
  ios_base::sync_with_stdio(false);

  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) {
    cout << "Case #" << tt << ": " << solve() << '\n';
  }
}
