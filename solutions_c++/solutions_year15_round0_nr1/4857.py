#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

int main() {
  int nr_tests;

  cin >> nr_tests;

  for (int nrt = 1; nrt <= nr_tests; nrt++) {
    int n;
    cin >> n;

    vector<int> v;
    for (int i = 0; i <= n; i++) {
      char c;
      cin >> c;
      v.push_back(c - '0');
    }

    int li = 0, ls = 1000, found = -1;

    while (li <= ls) {
      int x = (li + ls) / 2;

      int cnt = v[0] + x;
      bool bad = false;
      for (int i = 1; i <= n; i++) {
        if (i <= cnt) {
          cnt += v[i];
        } else {
          bad = true;
        }
      }

      if (bad) {
        li = x + 1;
      } else {
        ls = x - 1;
        found = x;
      }
    }

    cout << "Case #" << nrt << ": " << found << "\n";
  }

  return 0;
}

