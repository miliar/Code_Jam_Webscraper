#include <iostream>
using namespace std;

string calc(string s) {
  int a[10] = {};
  int c[26] = {};
  for (string::size_type i = 0; i < s.size(); ++i) {
    c[s[i] - 65]++;
  }
  a[0] = c[25]; c[4] -= a[0]; c[14] -= a[0]; c[17] -= a[0]; c[25] -= a[0];
  a[2] = c[22]; c[19] -= a[2]; c[14] -= a[2]; c[22] -= a[2];
  a[4] = c[20]; c[5] -= a[4]; c[14] -= a[4]; c[20] -= a[4]; c[17] -= a[4];
  a[6] = c[23]; c[18] -= a[6]; c[8] -= a[6]; c[23] -= a[6];
  a[8] = c[6]; c[4] -= a[8]; c[8] -= a[8]; c[6] -= a[8]; c[7] -= a[8]; c[19] -= a[8];
  a[3] = c[17]; c[19] -= a[3]; c[7] -= a[3]; c[17] -= a[3]; c[4] -= a[3] * 2;
  a[5] = c[5]; c[5] -= a[5]; c[8] -= a[5]; c[21] -= a[5]; c[4] -= a[5];
  a[1] = c[14]; c[14] -= a[1]; c[13] -= a[1]; c[4] -= a[1];
  a[7] = c[18];
  a[9] = c[8];
  string ret = "";
  for (int i = 0; i < 10; ++i) {
    for (int j = 0; j < a[i]; ++j) {
      ret += 48 + i;
    }
  }
  return ret;
}

int main() {
  int T;
  string s;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    cin >> s;
    cout << "Case #" << i + 1 << ": " << calc(s) << endl;
  }
}
