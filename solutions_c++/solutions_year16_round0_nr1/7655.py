#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

using digits_type = array<bool, 10u>;

void update(digits_type &digits, size_t n) {
  if (n == 0)
    digits[0] = true;

  while (n > 0) {
    digits[n % 10] = true;
    n /= 10;
  }
}

bool check(const digits_type &digits) {
  return all_of(digits.cbegin(), digits.cend(), [](bool d) { return d; });
}

void solve(const size_t case_number, const size_t n) {
  // cerr << "n: " << n << "\n";
  digits_type digits;
  digits.fill(false);

  cout << "Case #" << case_number << ": ";

  if (n == 0) {
    cout << "INSOMNIA\n";
    return;
  }

  for (auto i = 1u; i < 1000u; ++i) {
    auto x = i * n;
    // cerr << "\n"
    //     << "x: " << x << "\n";

    update(digits, x);
    if (check(digits)) {
      cout << x;
      break;
    }
  }

  cout << "\n";
}

int main() {
  auto t = 0u;

  cin >> t;
  assert(cin.good());

  for (auto i = 1u; i <= t; ++i) {
    auto n = 0u;
    cin >> n;
    assert(cin.good());
    solve(i, n);
  }
}
