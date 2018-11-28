#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <string>

using namespace std;

int Len;

string flip(string s, int cnt) {
  for (int i = 0; i < cnt / 2; i++) {
    char c = s[i];
    s[i] = s[cnt - 1 - i];
    s[cnt - 1 - i] = c;
  }
  for (int i = 0; i < cnt; i++) {
    if (s[i] == '+') s[i] = '-'; else s[i] = '+';
  }
  return s;
}

string bits(int x) {
  string ret;
  for (int i = 0; i < Len; i++) {
    if (x & (1 << i)) ret += "1"; else ret += "0";
  }
  return ret;
}

int getBest(string str) {
  map<string, int> d;
  vector<string> que;
  int st2 = 0, len = str.size();
  que.push_back(str);
  int ql = 0;
  string finish = "";
  for (int i = 0; i < len; i++) {
    finish += '+';
  }
  while (que.size() > ql) {
    string cur = que[ql];
    int cur_d = d[cur];
    //cout << "cur:" << cur << " dist:" << d[cur] << endl;
    if (cur == finish) {
      return cur_d;
    }
    ql++;

    // try possible next moves.
    for (int i = 1; i <= len; i++) {
      string nx = flip(cur, i);
      //cout << "nx:" << nx << " after flipping:" << i << endl;
      if (d.find(nx) != d.end()) {
        continue;
      }
      d[nx] = cur_d + 1;
      que.push_back(nx);
      if (nx == finish) {
        return d[nx];
      }
    }
  }
  return -1;
}

int main() {
  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    string s;
    cin >> s;
    Len = s.size();
    //cout << "start:" << s << endl;
    int res = getBest(s);
    cout << "Case #" << (i + 1) << ": " << res << endl;
  }

  return 0;
}
