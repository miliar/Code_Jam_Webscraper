#include <iostream>
#include <string>
using namespace std;

int T, K;


int main() {
  cin >> T;
  for (int i = 0; i < T; i++) {
    int n_flips = 0;
    string pancakes;

    cin >> pancakes >> K;

    // flipped[i] is true if pancake is flipped of starting position
    bool flipped[pancakes.length()];
    for (int j = 0; j < pancakes.length(); j++) {
      flipped[j] = false;
    }

    for (int k = 0; k < pancakes.length(); k++) {
      char side = pancakes[k];
      bool must_flip = (side == '-') == !flipped[k];
      if (must_flip) {
        // this pancake must be flipped,
        // and the flip has to start here.

        if (k+K > pancakes.length()) {
          n_flips = -1;
          break;
        }

        n_flips++;
        // flip next K-1 pancakes
        for (int s = k+1; s < k+K; s++) {
          flipped[s] = !flipped[s];
        }
      }
    }
    if (n_flips == -1) {
      cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
    } else {
      cout << "Case #" << i+1 << ": " << n_flips << endl;
    }
 }
}
