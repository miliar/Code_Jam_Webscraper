#include <iostream>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    int A, B, K;
    cin >> A >> B >> K;
    int res = 0;
    for (int i = 0; i < A; i++) {
      for (int j = 0; j < B; j++) {
        if ((i & j) < K) {
          res++;
        }
      }
    }

    cout << "Case #" << i << ": " << res << endl;
  }
}
