#include <bits/stdc++.h>
using namespace std;

int a[1002], n, r;
string s;

void gcj() {
  cin >> n >> s;
  a[0] += s[0]-'0';
  for (int i = 1; i < s.length(); i++) {
    a[i] = a[i-1];
    int d = a[i]-i;
    if (d < 0) {
      r -= d;
      a[i] -= d;
    }
    a[i] += (s[i]-'0');
  }
  cout << r << "\n";
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    cout << "Case #" << t << ": ";
    memset(a, 0, sizeof(a));
    r = 0;
    gcj();
  }
  return 0;
}
