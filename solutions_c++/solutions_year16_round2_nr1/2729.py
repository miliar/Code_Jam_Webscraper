#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

void solve(string &s) {
  VI dig(10);
  for (int i = 0; i < s.size(); ++i) {
    if (s[i] == 'Z') ++dig[0];
    if (s[i] == 'O') ++dig[1];
    if (s[i] == 'W') ++dig[2];
    if (s[i] == 'H') ++dig[3];
    if (s[i] == 'F') ++dig[4];
    if (s[i] == 'V') ++dig[5];
    if (s[i] == 'X') ++dig[6];
    if (s[i] == 'S') ++dig[7];
    if (s[i] == 'G') ++dig[8];
    if (s[i] == 'I') ++dig[9];
  }
  dig[7] -= dig[6];
  dig[5] -= dig[7];
  dig[4] -= dig[5];
  dig[3] -= dig[8];
  dig[1] -= (dig[2] + dig[0] + dig[4]);
  dig[9] -= (dig[5] + dig[6] + dig[8]);
  for (int i = 0; i < 10; ++i) {
    for (int j = 0; j < dig[i]; ++j) {
      cout << i;
    }
  }
  cout << "\n";
}// 0z 2w 6x 7s 5v 4f 8g 3h 1o 9n
//one two three four five six seven eight nine zero
int main() {

#ifdef LocalHost
  //freopen("input", "rt", stdin);
  freopen("A-large(1).in", "rt", stdin);
  freopen("output.txt", "w", stdout);
#endif
  int n; cin >> n;
  for (int t = 0; t < n; ++t) {
    string s;
    cin >> s;
    cout << "Case #" << t + 1 << ": ";
    solve(s);
  }
  return 0;
}
