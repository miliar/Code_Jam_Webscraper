#include <stdio.h>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

void get_ans (string p, string s, vector<string> & v) {
  if (p == "") {
    v.push_back(s);
  } else if (p.size() == 1) {
    get_ans("", p.at(0) + s, v);
    get_ans("", s + p.at(0), v);
  } else {
    get_ans(p.substr(1), p.at(0) + s, v);
    get_ans(p.substr(1), s + p.at(0), v);
  }
}

int main() {
  int T;
  scanf("%d", &T);

  for (int i = 1; i <= T; ++i) {
    printf("Case #%d: ", i);

    vector<string> v;
    string s;
    cin >> s;
    string c = s.substr(0, 1);

    for (int j = 1; j < s.size(); ++j) {
      if (s.at(j) >= c.at(0)) {
        c = s.at(j) + c;
      } else {
        c = c + s.at(j);
      }
    }

    printf("%s\n", c.c_str());
  }

  return 0;
}
