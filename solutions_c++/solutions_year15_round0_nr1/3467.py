#include <iostream>
#include <fstream>

using namespace std;

int main() {
  ifstream cin("input.txt");
  ofstream cout("output.txt");
  int tests;
  cin >> tests;
  string s;
  int n;
  for (int test = 0; test < tests; ++test) {
    cin >> n >> s;
    int ans = 0, cur = 0;
    for (int i = 0; i < (int) s.length(); ++i) {
      if (s[i] != '0' && i > cur) {
        ans += (i - cur);
        cur = i;
      }
      cur += (s[i] - '0');
    }
    cout << "Case #" << test + 1 << ": " << ans << '\n';
  }
  return 0;
}
