#include <iostream>
#include <vector>
#include <deque>
#include <string>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    string s;
    cin >> s;
    deque<int> d;
    d.push_back(s[0]);
    for (int i = 1; i < s.size(); ++i) {
      if (d.front() <= s[i]) {
        d.push_front(s[i]);
      } else {
        d.push_back(s[i]);
      }
    }
    cout << "Case #" << t << ": " << string(d.begin(), d.end()) << endl;
  }
}
