#include <iostream>
#include <utility>
#include <vector>
#include <string>
using namespace std;

enum {k0, k1, kI, kJ, kK};

int f[5][5] = { {k0, k0, k0, k0, k0},
                {k0, k1, kI, kJ, kK}, {k0, kI, -k1, kK, -kJ}, {k0, kJ, -kK, -k1, kI}, {k0, kK, kJ, -kI, -k1}};

int CharToInt(char c) {
  if (c == 'i') {
    return kI;
  }
  if (c == 'j') {
    return kJ;
  }
  if (c == 'k') {
    return kK;
  }
  return -1;
}

int main() {
  int test_count;
  cin >> test_count;
  for (int test_index = 0; test_index < test_count; ++test_index) {
    int l, x;
    string s;
    cin >> l >> x >> s;
    string t;
    for (int i = 0; i < x; ++i) {
      t += s;
    }
    int i_pos = t.size();
    int k_pos = -1;
    int g = 1;
    for (int i = 0; i < t.size(); ++i) {
      int sign = g < 0 ? -1 : 1;
      g = abs(g);
      g = f[g][CharToInt(t[i])] * sign;
      if (g == kI) {
        i_pos = min(i_pos, i);
      }
      if (g == kK) {
        k_pos = i;
      }
    }
    string res = i_pos < k_pos && g == -k1 ? "YES" : "NO";
    cout << "Case #" << test_index + 1 << ": " << res << "\n";
  }
  return 0;
}
