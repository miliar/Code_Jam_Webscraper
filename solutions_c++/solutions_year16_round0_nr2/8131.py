#include <iostream>
using namespace std;

int bestFlipCount(string S, int i = 0) {
  if (i == S.size()) {
    for (int j = 1; j < S.size(); ++j) {
      if (S[j] != S[j - 1]) {
        return 999999999;
      }
    }
    if (S[0] == '-') return 1;
    else return 0;
  }

  string flippedS = S;
  for (int j = 0; j <= i; ++j) {
    if (flippedS[j] == '-') {
      flippedS[j] = '+';
    } else {
      flippedS[j] = '-';
    }
  }
  reverse(flippedS.begin(), flippedS.begin() + i + 1);

  int flip = bestFlipCount(flippedS, i + 1) + 1;
  int dontFlip = bestFlipCount(S, i + 1);
  return min(flip, dontFlip);
}

int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    string S;
    cin >> S;
    int flipCount = bestFlipCount(S);

    cout << "Case #" << i << ": " << flipCount << endl;
  }
}
