#include <iostream>
#include <algorithm>
#include <vector>

using std::cin;
using std::cout;
using std::vector;

int main() {
  std::ios::sync_with_stdio(false);

  int tests;
  cin >> tests;
  cin.ignore();
  for (int i = 0; i < tests; ++i) {
    std::string l;
    getline(cin, l);
    auto prev_char = *l.begin();
    int flips = 0;
    for (auto i = l.begin()+1; i < l.end(); ++i) {
      if (*i != prev_char) {
        ++flips;
        prev_char = *i;
      }
    }
    if (l.back() != '+') {
      ++flips;
    }
    cout << "Case #" << i + 1 << ": ";
    cout << flips << "\n";
  }
}
