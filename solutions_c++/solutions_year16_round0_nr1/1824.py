#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

using int64 = long long;

int64 get_n(const int64 n) {
  if (n == 0) {
    return -1;
  }
  bitset<10> seen;
  auto n_k = 0;
  while (!seen.all()) {
    n_k += n;
    auto n_k_copy = n_k;
    while (n_k_copy != 0) {
      auto ones = n_k_copy % 10;
      seen.set(static_cast<size_t>(ones), true);
      n_k_copy /= 10;
    }
  }
  return n_k;
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    int64 inp;
    cin >> inp;
    auto ret = get_n(inp);
    cout << "CASE #" << i + 1 << ": ";
    if (ret == -1) {
      cout << "INSOMNIA";
    } else {
      cout << ret;
    }
    cout << '\n';
  }

  return 0;
}
