#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_set>
#include <unordered_map>

using namespace std;

int T;

int main() {
  cin >> T;
  for (int ti = 1; ti <= T; ++ti) {
    string s;
    cin >> s;
    char p = '0';
    int ans = 0;
    for (int i = 0; i < s.length(); ++i) {
      if (s[i] != p) {
        ans++;
        p = s[i];
      }
    }
    if (s[s.length()-1] == '+')
      ans--;
    cout << "Case #" << ti << ": " << ans << endl;
  }
  return 0;
}
