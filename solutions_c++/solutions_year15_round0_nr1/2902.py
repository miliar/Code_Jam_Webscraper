#include <iostream>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; ++t) {
    int S;
    cin >> S >> ws;
    int cum = 0;
    int used = 0;
    for (int i = 0; i < S + 1; ++i) {
      char val;
      cin >> val;
      val -= '0';
      int diff = 0;
      if (val) diff = std::max(i - cum, 0);
      cum += val + diff;
      used += diff;
    }
    cout << "Case #" << t + 1 << ": " << used << endl;
  }
}

