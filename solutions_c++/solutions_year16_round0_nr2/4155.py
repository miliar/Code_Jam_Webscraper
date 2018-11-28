#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main(int argc, char const *argv[]) {
  int t;
  cin >> t;
  for (size_t c = 1; c <= t; c++) {
    string s;
    cin >> s;
    reverse(s.begin(), s.end());
    int cnt = 0;
    int len = s.length();
    char now, prev = s[0];
    if (prev == '-') {
        cnt++;
    }
    for (size_t j = 1; j < len; j++) {
      now = s[j];
      if (now != prev) {
        cnt++;
      }
      prev = now;
    }
    cout << "Case #" << c << ": " << cnt << endl;
  }
  return 0;
}
