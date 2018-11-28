
#include <bits/stdc++.h>
using namespace std;

int main() {
  int t;
  cin >> t;
  char s[1002];
  cin.getline(s, 1002);
  for (int i = 1; i <= t; ++i) {
    cin.getline(s, 1002);
    int l = cin.gcount();
    deque<char> d;
    d.push_front(s[0]);
    for (int j = 1; j < l - 1; j++) {
       if (s[j] >= d[0]) {
          d.push_front(s[j]);
       } else {
          d.push_back(s[j]);
       }
    }
    cout << "Case #" << i << ": ";
    for (deque<char>::iterator it = d.begin(); it != d.end(); ++it) {
       cout << (*it);
    }
    cout << endl;
  }
  return 0;
}

