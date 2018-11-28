#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <sstream>

using namespace std;

string s;
int score[1005];
bool used[1005];

string solve() {
  if (s.length() == 1) {
    return s;
  }

  int n = s.length();
  memset(used, 0, sizeof(used));
  stringstream ss;
  score[0] = s[0] - 'A';
  for (int i = 1; i < n; ++i) {
    score[i] = max(score[i-1], s[i] - 'A');
  }

  for (int i = n-1; i >= 0; --i) {
    if ((int)(s[i] - 'A') == score[i]) {
      ss << s[i];
      used[i] = true;
    }
  }

  for (int i = 0; i < n; ++i) {
    if (!used[i])
      ss << s[i];
  }
  return ss.str();
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> s;
    cout << "Case #" << i << ": " << solve() << endl;
  }
  return 0;
}
