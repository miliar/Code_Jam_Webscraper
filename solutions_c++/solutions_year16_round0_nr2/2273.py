#define NDEBUG
#include <algorithm>
#include <iostream>
#include <string>
#include <utility>
using namespace std;


string move(string str, int n) {
  reverse(str.begin(), str.begin() + n);
  for (int i=0; i<n; ++i) {
    str[i] = str[i] == '+' ? '-' : '+';
  }
  return str;
}

int solve() {
  string str;
  cin >> str;
  const int n = (int)str.size();
  int ans = 0;
  for (int j=n-1; j>=0; --j) {
    if (str[j] == '-') {
      int i;
      for (i=0; str[i] == '+'; ++i) ;
      if (i > 0) {
        ++ans;
        str = move(str, i);
      }
      ++ans;
      str = move(str, j+1);
    }
  }
  return ans;
}

int main() {
  ios_base::sync_with_stdio(false);

  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) {
    cout << "Case #" << tt << ": " << solve() << '\n';
  }
}
