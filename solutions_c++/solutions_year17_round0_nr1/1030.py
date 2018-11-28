#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <string>

using namespace std;

template<typename T> T next() { T tmp; cin >> tmp; return tmp; }

void solve() {
  string s = next<string>();
  int k = next<int>();
  int res = 0;
  for (int i = 0; i <= s.size() - k; ++i) {
    if (s[i] == '-') {
      for (int j = i; j < i + k; ++j) {
        s[j] = s[j] == '-' ? '+' : '-';
      }
      res++;  
    }
  }
  for (int i = std::max((int)s.size() - k, 0); i < s.size(); ++i) {
    if (s[i] == '-') {
      cout << "IMPOSSIBLE\n";
      return;
    }
  }
  cout << res << "\n"; 
}

int main() {
  int n = next<int>();
  for (int i = 1; i <= n; ++i) {
    cout << "Case #" << i << ": ";
    solve();
  } 
  return 0;
}
