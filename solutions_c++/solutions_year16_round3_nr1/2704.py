#include <bits/stdc++.h>
using namespace std;

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ":";
    int n;
    cin >> n;
    vector<int> s(n);
    for (int j = 0; j < n; j++) {
      int k;
      cin >> k;
      s[j] = k;
      // s[k] = 'A' + j;
    }
    while (true) {
      int a = 0, b = 0, c = 0;
      int pa, pb, pc;
      for (int k = 0; k < n; k++) {
        int d = s[k];
        if (d > a) {
          c = b;
          pc = pb;
          b = a;
          pb = pa;
          a = d;
          pa = k;
        } else if (d > b) {
          c = b;
          pc = pb;
          b = d;
          pb = k;
        } else if (d > c) {
          c = d;
          pc = k;
        }
      }
      if (a == 0) {
        break;
      }
      if (a == b) {
        if (c == 0) {
          s[pa]--;
          s[pb]--;
          cout << ' ' << (char)('A' + pa) << (char)('A' + pb);
        } else {
          s[pa] -= 1;
          cout << ' ' << (char)('A' + pa);
        }
      } else {
        s[pa] -= 1;
        cout << ' ' << (char)('A' + pa);
      }
      // auto it1 = s.rbegin();
      // auto it2 = s.rbegin(); ++it2;
      // if (it1->first == 0) {
      //   break;
      // }
      // if (it1->first == it2->first) {
      //   cout << ' ' << it1->second << it2->second;
      //   it2
      // }
    }
    cout << endl;
  }
  return 0;
}
