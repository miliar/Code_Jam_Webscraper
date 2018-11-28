#include <iostream>

using namespace std;

int main() {
  int t;
  cin >> t;
  for (int ci = 1; ci <= t; ++ci) {
    string s, res;
    cin >> s;

    res = s[0];
    for (int i = 1; i < s.size(); ++i) {
      if (res[0] > s[i]) res += s[i];
      else res = s[i] + res;
    }

    cout << "Case #" << ci << ": " << res << endl;
  }

  return 0;
};
