#include <iostream>
#include <queue>
#include <set>

using namespace std;

#define LL long long

bool isHappy(string &s) {
  for (char c : s)
    if (c == '-') return false;
  return true;
}

char neg(char c) {
  if (c == '-') return '+';
  return '-';
}

string flip(string &s, int i) {
  string ss = s;
  int m = i/2;
  if (i%2 == 0) --m;
  for (int j = 0; j <= m; ++j) {
    std::swap(ss[j], ss[i-j]);
    ss[j] = neg(ss[j]);
    ss[i-j] = neg(ss[i-j]);
  }
  if (i%2 == 0) ss[i/2] = neg(ss[i/2]);
  return ss;
}

int main() {
  int T; cin>>T;
  for (int t=1; t <= T; ++t) {
    string s; cin >> s;
    queue<string> que;
    set<string> checked;

    que.push(s);
    LL time = 0;
    bool happy = false;
    while (!happy) {
      queue<string> children;
      while (!que.empty() && !happy) {
        string ss = que.front();
        happy = isHappy(ss);
        checked.insert(ss);
        int m;
        for (m = ss.size()-1; m >= 0 && ss[m] == '+'; --m) {}
        for (int i = 0; i <= m; ++i) {
          string sss = flip(ss, i);
          if (checked.find(sss) == checked.end())
            children.push(sss);
        }
        que.pop();
      }
      if (happy) continue;
      time ++;
      que.swap(children);
    }
    printf("Case #%d: %lld\n", t, time);
  }

  return 0;
}
