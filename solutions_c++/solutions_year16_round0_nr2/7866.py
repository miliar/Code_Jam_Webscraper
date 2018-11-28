#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    cin.get();
    for (int t = 0; t < n; t++) {
      int flips = 0;
      char c, lc;
      c = cin.get();
      lc = c;
      while (c != '\n') {
        if (lc != c) {
          flips++;
        }
        lc = c;
        c = cin.get();
      }
      if (lc == '-') {
        flips++;
      }
      cout << "Case #" << t+1 << ": " << flips << "\n";

    }

    return 0;
}