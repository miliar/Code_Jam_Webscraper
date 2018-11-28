#include <iostream>
#include <vector>
using namespace std;

int sq_root (int X) {
  for (int i = 1; i * i <= X; ++i) {
    if (i * i == X) return i;
  }
  return -1;
}

bool is_palin(int A) {
  vector<int> digits;
  digits.clear();
  while (A > 0) {
    digits.push_back(A % 10);
    A /= 10;
  }

  bool check = true;
  for (int i = 0; i < digits.size(); ++i) {
    if (digits[i] != digits[digits.size() - 1 - i]) check = false;
  }

  return check;
}

int main () {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int A, B;
    cin >> A >> B;
    int count = 0;
    for (int i = A; i <= B; ++i) {
      int sq = sq_root(i);
      if (sq == -1) continue;
      if (!is_palin(sq) || !is_palin(i)) continue;
      ++count;
    }
    cout << "Case #" << t << ": " << count << endl;
  }
}
