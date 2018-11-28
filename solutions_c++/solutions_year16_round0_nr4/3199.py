#include <iostream>
#include <cmath>

using namespace std;

void parse_and_solve(istream& in, ostream& out) {
  long unsigned k, c, s;
  in >> k >> c >> s;
  if (s < k) {
    out << "IMPOSSIBLE";
    // Cop out! Definitely not true!
  } else {
    long unsigned incriment = pow(k, c - 1);
    long unsigned init = 1;
    for (unsigned i = 0; i < k; ++i) {
      if (i > 0) {
        out << ' ';
      }
      out << init;
      init += incriment;
    }
  }
}

int main() {
  unsigned num;
  cin >> num;
  for (unsigned i = 1; i <= num; ++i) {
    cout << "Case #" << i << ": ";
    parse_and_solve(cin, cout);
    cout << '\n';
  }
  cout << flush;
}
