#include <iostream>
using std::cin;
using std::cout;
#include <string>
#include <vector>

void solve() {
  std::string S;
  cin >> S;
  std::vector<unsigned> letters(26, 0);
  for (int i = 0; i < S.length(); ++i) {
    ++letters[S[i] - 'A'];
  }
  std::vector<std::string> names = {"ZERO", "ONE", "TWO", "THREE", "FOUR",
    "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
  std::vector<unsigned> digits(10, 0);

  std::vector<unsigned> order = {0, 2, 4, 5, 6, 7, 8, 9, 1, 3};

  for (int i = 0; i < 10; ++i) {
    unsigned min = 1 << 20;
    int I = order[i];
    for (int j = 0; j < names[I].length(); ++j) {
      if (letters[names[I][j] - 'A'] < min) {
        min = letters[names[I][j] - 'A'];
      }
    }
    for (int j = 0; j < names[I].length(); ++j) {
      letters[names[I][j] - 'A'] -= min;
    }
    digits[I] = min;
  }

  for (int i = 0; i < 10; ++i) {
    for (int j = 0; j < digits[i]; ++j) {
      cout << i;
    }
  }
  cout << '\n';
}

int main() {
  unsigned T;
  cin >> T;
  for (unsigned i = 0; i < T; ++i) {
    cout << "Case #" << i + 1 << ": ";
    solve();
  }
}
