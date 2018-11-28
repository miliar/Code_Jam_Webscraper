#include <iostream>

using namespace std;

int main() {
  int T;
  cin >> T;

  for (int tst = 0; tst < T; tst++) {
    string s;
    int k;
    cin >> s >> k;
    int n = int(s.size()), res = 0;
    bool good = true;

    for (int i = 0; i < n; i++) {
      if (s[i] == '-') {
        if (i + k > n) {
          cout << "Case #" << tst + 1 << ": IMPOSSIBLE\n";
          good = false;
          break;
        }

        for (int j = i; j < i + k; j++) {
          s[j] = (s[j] == '+' ? '-' : '+');
        }
        res++;
      }
    }
    if (good) {
      cout << "Case #" << tst + 1 << ": " << res << '\n';
    }
  }
}
