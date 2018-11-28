#include <iostream>

using namespace std;

int n;
string s;

int solve() {
  int q = 0, t, ans = 0;
  for (int i = 0; i < (int)s.size(); ++i) {
    t = s[i] - '0';
    if (t and i > q) {
      ans += i - q;
      q += i - q;
    }
    q += t;
  }
  return ans;
}

int main() {
  int tc;
  cin >> tc;
  for (int i = 0; i < tc; ++i) {
    cin >> n >> s;
    cout << "Case #" << i + 1 << ": ";
    cout << solve() << endl;
  }
  return 0;
}
