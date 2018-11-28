#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>

using std::cin; using std::cout;
using std::string; using std::endl;
using std::vector; using std::unordered_map;

typedef string::size_type str_sz;
typedef vector<int>::size_type vec_sz;

void processTestCase(int i) {
  int x, r, c;
  cin >> x >> r >> c;

  bool canAlwaysSolve = r * c % x == 0;

  if (canAlwaysSolve && x > 2) {
    canAlwaysSolve = c > 1 && r > 1;
  }

  if (canAlwaysSolve && x == 4) {
    canAlwaysSolve = r * c >= 12;
  }

  /*
  cout << i << " - X: " << x << " Grid: " << r << "x" << c <<
    " - canAlwaysSolve: " << canAlwaysSolve <<
    "" << endl;
    */
  cout << "Case #" << i + 1 << ": " <<
    (canAlwaysSolve ? "GABRIEL" : "RICHARD") << endl;
}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    processTestCase(i);
  }
  return 0;
}
