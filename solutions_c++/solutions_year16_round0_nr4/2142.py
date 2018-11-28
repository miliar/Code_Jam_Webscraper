#include <iostream>
#include <cmath>
using namespace std;

typedef unsigned long long int ll;

int main() {
  int T, K, C, S;
  cin >> T;

  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    cin >> K >> C >> S;
    if (K == S) {
      for (int i = 1; i <= K; ++i) {
        cout << i << " ";
      }
      cout << endl;
      continue;
    }

    if (C == 1 || ((K + 1) / 2) > S) {
      cout << "IMPOSSIBLE" << endl;
      continue;
    }

    for (int i = 0; i < ((K + 1) / 2); ++i) {
      ll base = pow(K, C - 1) * 2 * i;
      cout << base + 1 << " ";
    }
    cout << endl;

  }
}
