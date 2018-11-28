#include <iostream>
#include <queue>
using namespace std;

string solve(string s) {
  deque<char> q;
  for (auto c : s) {
    if (q.empty())      q.push_front(c);
    else if (c >= q[0]) q.push_front(c);
    else                q.push_back(c);
  }
  string r;
  for (auto c : q) r.push_back(c);
  return r;
}

int main() {
  int n;
  cin >> n;
  for (int t = 1; t <= n; ++t) {
    string s;
    cin >> s;
    printf("Case #%d: %s\n", t, solve(s).c_str());
  }
  return 0;
}
