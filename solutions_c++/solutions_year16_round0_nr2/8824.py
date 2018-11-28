#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; ++t) {
    string s; cin >> s;
    vector<bool> bits;
    for (char c: s) {
      bits.push_back(c == '+');
    }
    bool flip = false;
    int count = 0;
    for (int i = bits.size() - 1; i >= 0; --i) {
      bool curr = bits[i] ^ flip;
      if (!curr) {
        count++;
        flip = !flip;
      }
    }
    printf("Case #%d: %d\n", t, count);
  }
  return 0;
}