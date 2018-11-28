#include <iostream>
#include <string>
#include <deque>

using namespace std;

string solve(string s) {
  deque<int> q;
  string r;
  for (int i = 0; i < s.size(); i++) {
    if (q.empty() || s[i] >= q.front()) {
      q.push_front(s[i]);
    } else {
      q.push_back(s[i]);
    }
  }
  for (auto &e : q) {
    r.push_back(e);
  }
  return r;
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T ; t++) {
    string s;
    cin >> s;
    cout << "Case #" << t << ": " << solve(s) << endl;;
  }
    return 0;
}
