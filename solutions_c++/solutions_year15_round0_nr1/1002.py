#include <iostream>
#include <string>
using namespace std;

int solve() {
  int sol = 0, now = 0;
  int n;
  string s;
  cin >> n >> s;
  for (int i = 0; i <= n; i++) {
    if (s[i] - '0' > 0 && now < i) {
      sol += i - now;
      now = i;
    }
    now += s[i] - '0';
  }
  return sol;
}

int main() {
  int _;
  cin >> _;
  for (int i = 1; i <= _; i++) {
    printf("Case #%d: %d\n", i, solve());
  }
}
