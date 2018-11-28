#include <iostream>
#include <set>

using namespace std;

int main() {
  int t;
  cin >> t;
  for (int ci = 1; ci <= t; ++ci) {
    long long n;
    cin >> n;

    cout << "Case #" << ci << ":";
    set<int> s, ans;
    s.insert(n);

    long long v = n;
    while (v > 0) {
      ans.insert(v % 10);
      v /= 10;
    }
    if (ans.size() == 10) {
      cout << " " << n << endl;
      continue;
    }

    for (int i = 2;; ++i) {
      long long v = n * i;
      if (s.find(v) != s.end()) {
        cout << " INSOMNIA" << endl;
        break;
      }

      s.insert(v);
      while (v > 0) {
        ans.insert(v % 10);
        v /= 10;
      }

      if (ans.size() == 10) {
        cout << " " << n * i << endl;
        break;
      }
    }
  }

  return 0;
}
