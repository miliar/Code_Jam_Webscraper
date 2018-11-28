#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main () {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int test, c = 0;
  string s;

  cin >> test;

  getline(cin, s);

  while (test > 0) {
    c++;
    test--;
    vector<int> a;
    int ans = 0;

    getline(cin, s);

    int n = s.length();

    for (int i = 0; i < n; ++i) {
      if (s[i] == '-') {
        a.push_back(1);
      } else {
        a.push_back(0);
      }
    }

    while (true) {
      int sum = 0;
      for (int i = 0; i < n; ++i) {
        sum += a[i];
        // cout << a[i] << " ";
      }
      // cout << endl;

      if (sum == 0) {
        break;
      }

      for (int i = n-1; i >= 0; --i) {
        if (a[i] == 1) {
          for (int j = 0; j <= i; ++j) {
            a[j] = a[j] ^ 1;
          }
          break;
        }
      }
      ans++;
    }

    cout << "Case #" << c << ": " << ans << endl;
  }

  return 0;
}
