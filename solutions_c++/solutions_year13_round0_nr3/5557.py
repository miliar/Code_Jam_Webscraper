#include <iostream>

using namespace std;

typedef long long int64;

int64 start, end;

bool IsPalindrome(int64 val) {
  int digits[16];

  int idx = 0;
  while (val > 0) {
    digits[idx] = (val % 10);
    val /= 10;
    ++idx;
  }

  for (int aa = 0; aa < idx / 2; ++aa) {
    if (digits[aa] != digits[idx - aa - 1]) {
      return false;
    }
  }
  return true;
}

int Solve() {
  int solve = 0;

  for (int64 val = 0; val < 10000000; ++val) {
    const int sq = val * val;
    if (sq > end) {
      return solve;
    }
    if (sq < start) {
      continue;
    }
    if (IsPalindrome(val) && IsPalindrome(sq)) {
      ++solve;
    }
  }

  return solve;
}

int main() {

  int cases;
  cin >> cases;
  for (int cc = 0; cc < cases; ++cc) {
    cin >> start >> end;
    cout << "Case #" << (cc + 1) << ": " << Solve() << "\n";
  }

  return 0;
}
