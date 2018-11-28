#include <iostream>

using namespace std;

int t = 0, a = 0, b = 0, k = 0;

int NewLotteryGame() {
  int numOfWins = 0;

  for (int i = 0; i < a; ++i) {
    for (int j = 0; j < b; ++j) {
      if ((i & j) < k) {
        numOfWins++;
      }
    }
  }

  return numOfWins;
}

int main() {
  cin >> t;

  for (int caseNum = 1; caseNum <= t; ++caseNum) {
    cin >> a >> b >> k;

    cout << "Case #" << caseNum << ": " << NewLotteryGame() << endl;
  }

  return 0;
}

