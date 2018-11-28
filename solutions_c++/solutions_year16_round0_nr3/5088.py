#include <iostream>
#include <string>
#include <boost/multiprecision/cpp_int.hpp>

using namespace boost::multiprecision;
using namespace std;

int main(void) {
  int T, N, J;
  cin >> T >> N >> J;

  cout << "Case #1:\n";

  for (int i = 0; i < J; ++i) {
    string s = "1";
    for (int digit = 0; digit < N/2-2; ++digit)
      if (i & (1 << digit)) s += "1"; else s += "0";
    s += "1"; s += s;

    cout << s;
    for (int base = 2; base <= 10; ++base) {
      cpp_int x = 1; for (int j = 1; j <= N/2; ++j) x *= base;
      cout << " " << 1 + x;
    }
    cout << "\n";
  }

  return 0;
}
