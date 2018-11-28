#include <iostream>
#include <unordered_set>
using namespace std;

#define present(c, e) ((c).find((e)) != (c).end())

unordered_set<int> s;

void f(int n) {
  int x;
  do {
    x = n % 10;
    s.emplace(x);
    n /= 10;
  } while (n);
}

bool check() {
  for (int i = 0; i <= 9; ++i) {
    if (!present(s, i)) {
      return false;
    }
  }
  return true;
}

int solve(int n) {
  for (int i = 1; ; ++i) {
    int tmp = n*i;
    f(tmp);
    if (check()) {
      s.clear();
      return tmp;
    }
  }
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int t, n;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> n;
    if (!n) {
      cout << "Case #" << i << ": " << "INSOMNIA" << "\n";
    } else {
      cout << "Case #" << i << ": " << solve(n) << "\n";
    }
  }
}
