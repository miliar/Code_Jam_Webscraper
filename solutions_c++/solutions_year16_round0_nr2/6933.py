#include <iostream>
#include <string>

using namespace std;

int main() {
  auto solve = [](string s) -> int {
    int p = 0;
    int m = 0;

    int i = 0;
    int steps = 0;

    auto move = [&](char c) -> int {
      int old_i = i;
      while (i < s.size() && s[i] == c)
	++i;
      return i - old_i;
    };

    p += move('+');
    m += move('-');
    if (p == 0) {
      p = m + move('+');
      m = move('-');
      ++steps;
    }

    while (m != 0) {
      steps += 2;
      p += m + move('+');
      m = move('-');
    }

    return steps;
  };

  int cases;
  cin >> cases;

  for (int c = 1; c <= cases; ++c) {
    string in;
    cin >> in;

    cout << "Case #" << c << ": ";
    cout << solve(in) << "\n";
  }
}
