#include <iostream>
using namespace std;

int D, P[1024];

int caseMain() {
  cin >> D;
  int lower = 1, upper = 0;
  for (int i = 0; i < D; ++i) {
    cin >> P[i];
    upper = max(upper, P[i]);
  }

  while (lower < upper) {
    int mid = (lower + upper) / 2;

    bool good = false;
    for (int eat = 1; eat <= mid && !good; ++eat) {
      int move = mid - eat;

      for (int i = 0; i < D && move >= 0; ++i) {
        move -= (P[i] + eat - 1) / eat - 1;
      }
      if (move >= 0) {
        good = true;
      }
    }

    if (good) {
      upper = mid;
    } else {
      lower = mid + 1;
    }
  }

  return upper;
}

int main(int argc, const char* argv[]) {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    cout << "Case #" << i + 1 << ": ";
    cout << caseMain() << endl;
  }
  return 0;
}
