#include <algorithm>
#include <array>
#include <iostream>
#include <ios>
#include <istream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

unsigned get_digits(int n) {
  unsigned result = 0;
  while (n > 0) {
    int rem = n % 10;
    result |= 1 << rem;
    n /= 10;
  }

  return result;
}

int main(int argc, char *argv[]) {
  cout.precision(8); cout.setf(ios_base::showpoint);
  long t; cin >> t;

  for (long i = 1; i <= t; ++i) {
    long n; cin >> n;

    if (n == 0) {
      cout << "Case #" << i << ": " << "INSOMNIA" << endl;
      continue;
    }

    auto nprime = n;
    unsigned s = get_digits(n);
    while (s != 0x3ff) {
      nprime += n;
      s |= get_digits(nprime);
    }

    cout << "Case #" << i << ": " << nprime << endl;
  }

  return 0;
}
