#include <iostream>
#include <string>
using namespace std;

int solve(string s) {
  int num_iter = 0;
  int i = 0;
  while (i < s.length()) {
    if (s[i] == '+') {
      i++;
    } else {
      int beg_i = i;
      while (s[i] == '-') {
        i++;
      }   
      if (beg_i == 0) {
        num_iter = 1;
      } else {
        num_iter += 2;
      }   
    }   
  }
  return num_iter;
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; i++) {
    string s;
    cin >> s;
    cout << "Case #" << i << ": " << solve(s) << endl;
  }
  return 0;
}

