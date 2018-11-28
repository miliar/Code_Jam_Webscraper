#include <stdio.h>
#include <string>
#include <iostream>


using namespace std;

unsigned get_ans(string s) {
  string r = string(s.size(), '+');
  if (s == r) {
    return 0;
  }
  r = string(s.size(), '-');
  if (s == r) {
    return 1;
  }

  unsigned ans = 0;
  char c = s.at(0);
  for (int i = 1; i < s.size(); ++i) {
    if (s.at(i) == c) {
      continue;
    } else {
      ans++;
      c = (c == '-') ? '+' : '-';
    }
  }

  return c == '-' ? ans + 1 : ans;
}


int main() {
  int T;
  scanf("%d", &T);

  for (int i = 1; i <= T; ++i) {
    printf("Case #%d: ", i);

    string s;
    cin >> s;

    printf("%u\n", get_ans(s));
  }

  return 0;
}
