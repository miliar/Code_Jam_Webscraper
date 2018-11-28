#include <stdio.h>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <limits.h>
#include <queue>


using namespace std;

unordered_map<string, unsigned> m;

unsigned int get_ans (queue<string> q) {
  while (q.empty() == false) {
    string s = q.front();
    q.pop();
    unsigned v = m.find(s)->second;

    string r = string(s.size(), '+');
    if (r == s) {
      return v;
    }
    r = string(s.size(), '-');
    if (r == s) {
      return v + 1;
    }

    for (int i = 1; i <= s.size(); ++i) {
      string u = s.substr(0, i);
      reverse(u.begin(), u.end());
      string k = "";
      for (int j = 0; j < u.size(); ++j) {
        if (u.at(j) == '+') {
          k += '-';
        } else {
          k += '+';
        }
      }
      string t = k;
      if (i < s.size()) {
        t += s.substr(i);
      }

      if (m.find(t) == m.end()) {
        m.emplace(t, v + 1);
        q.emplace(t);
      }
    }
  }
}

int main() {
  int T;
  scanf("%d", &T);

  for (int i = 1; i <= T; ++i) {
    printf("Case #%d: ", i);

    string s;
    cin >> s;

    m.clear();
    m.emplace(s, 0);

    queue<string> q;
    q.emplace(s);

    printf("%u\n", get_ans(q));
  }

  return 0;
}
