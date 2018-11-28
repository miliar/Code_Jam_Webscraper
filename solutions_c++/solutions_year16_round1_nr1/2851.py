#include <bits/stdc++.h>

using namespace std;

int main() {
  deque<char> dq;
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    cout << "Case #" << (i + 1) << ": ";
    string s;
    cin >> s;
    for (int j = 0; j < s.size(); ++j) {
      if (dq.empty()) dq.push_back(s[j]);
      else {
        if (s[j] < dq.front()) dq.push_back(s[j]);
        else dq.push_front(s[j]);
      }
    }
    while (!dq.empty()) {
      cout << dq.front();
      dq.pop_front();
    }
    cout << endl;
  }
  return 0;
}
