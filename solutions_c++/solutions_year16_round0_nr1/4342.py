#include <iostream>
#include <vector>

using namespace std;

int main() {
  int tests;
  cin >> tests;
  for (int test = 1; test <= tests; ++test) {
    long long n, first;
    cin >> n;
    first = n;
    cout << "Case #" << test << ": ";
    if (n == 0) {
      cout << "INSOMNIA\n";
      continue;
    }
    vector<int> used(10, 0);
    int cnt = 0;
    while (true) {
      long long tmp = n;
      while (tmp > 0) {
        int last = tmp % 10;
        tmp /= 10;
        if (used[last] == 0)
          ++cnt;
        ++used[last];
      }
      if (cnt != 10)
        n += first;
      else
        break;
    }
    cout << n << '\n';
  }
  return 0;
}
