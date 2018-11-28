#include <iostream>

using namespace std;

int main(int argc, char** argv) {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    int S, K, C;
    cin >> K;
    cin >> C;
    cin >> S;
    cout << "Case #" << i << ": ";
    if (S != K) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      for (int j = 1; j <= K; ++j) {
        cout << j << " ";
      }
      cout << endl;
    }
  }
  return 0;
}
