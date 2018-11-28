#include <iostream>
using std::cin;
using std::cout;
#include <string>

void solve() {
  std::string pile;
  cin >> pile;
  char prev = '+';
  unsigned answer = 0;
  for (unsigned i = pile.length(); i > 0; ) {
    --i;
    if (pile[i] != prev) {
      ++answer;
    }
    prev = pile[i];
  }
  cout << answer << '\n';
}

int main() {
  unsigned T;
  cin >> T;
  for (unsigned i = 0; i < T; ++i) {
    cout << "Case #" << i + 1 << ": ";
    solve();
  }
}
