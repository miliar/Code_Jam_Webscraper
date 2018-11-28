#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main() {
  int A,
      B,
      K,
      T,
      ans;

  cin >> T;

  for (int i = 0; i < T; ++i) {
    ans = 0;
    
    cin >> A >> B >> K;

    for (int j = 0; j < A; ++j) {
      for (int k = 0; k < B; ++k) {
        if ((j&k) < K) {
          ++ans;
        }
      }
    }

    cout << "Case #" << i+1 << ": " << ans << endl;
  }

  return 0;
}
