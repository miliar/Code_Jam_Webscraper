#include <iostream>
#include <stack>
using namespace std;

char flip(char c) {
   return c == '+' ? '-' : '+';
}
int fun(string &s) {
  if (s.empty()) {
    return 0;
  }
  int counter = 0;
  int j = s.length() - 1;
  while (j >= 0) {
    while (j >= 0 && s[j] == '+') {
      --j;
    }
    if (j < 0) {
      break;
    }
    int i = 0;
    if (s[i] == '-') {
      ++counter;
      int k = i, l = j;
      while (k <= l) {
        char tmp = s[k];
        s[k] = flip(s[l]);
        s[l] = flip(tmp);
        ++k;
        --l;
      }
    } else {
      int k = i;
      while (s[k] == '+') {
	s[k] = '-';
	++k;
      }
      ++counter;
      int l = j;
      k = i;
      while (k <= l) {
        char tmp = s[k];
        s[k] = flip(s[l]);
        s[l] = flip(tmp);
        ++k;
        --l;
      }
      ++counter;      
    }
  }
  return counter;  
}
int main() {
  int T = 0;
  cin >> T;
  string s;
  for (int i = 1; i <= T; ++i) {
    cin >> s;
    cout << "Case #" << i << ": " << fun(s) << endl;
  }
}
