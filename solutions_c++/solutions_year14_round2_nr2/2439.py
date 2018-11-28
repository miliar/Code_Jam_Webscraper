#include <iostream>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int testcase = 1; testcase <= T; ++testcase) {
    int A, B, K;
    cin >> A >> B >> K;

    int ans = 0;
    for (int i = 0; i < A; ++i) {
      for (int j = 0; j < B; ++j) {
        if ((i & j) < K)
          ++ans;
      }
    }
    
    cout << "Case #" << testcase << ": " << ans << endl;
  }
  return 0;
}
