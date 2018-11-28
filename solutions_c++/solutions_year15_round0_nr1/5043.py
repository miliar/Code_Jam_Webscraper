#include <iostream>
#include <string>
#include <cassert>
#include <algorithm>

using namespace std;

int char_to_int(char c) {
  assert('0' <= c && c <= '9' && "c is not a char");
  return int(c - '0');
}

int solve(string s) {
  int stood_up = 0;
  int invited = 0;
  for (int n = 0; n < s.size(); ++n) {
    int invited_now = max(n - stood_up, 0);
    invited += invited_now;
    stood_up += invited_now;
    stood_up += char_to_int(s[n]);
  }

  return invited;
}

int main(){
  int cases;
  cin >> cases;

  for (int n = 1; n <= cases; ++n) {
    int count;
    string s;
    cin >> count >> s;

    cout << "Case #" << n << ": " << solve(s) << "\n";
  }
}
