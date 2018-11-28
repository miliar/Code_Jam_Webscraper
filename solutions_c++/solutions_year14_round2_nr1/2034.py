#include <iostream>
#include <string>
#include <vector>

using namespace std;

int calc (string s1, string s2, char c) {
  if (s1 == s2) return 0;

//  if (s1.length() == 0 || s2.length() == 0) return -1;
  
  int changes = 100000;

  if (s1.length() > 0 && s2.length() > 0 && s1[0] == s2[0]) {
    int res = calc(s1.substr(1), s2.substr(1), s1[0]);
    if (res >= 0) changes = min(changes, res);
  } else {
    if (s1.length() > 0 && c == s1[0]) {
      int res = calc(s1.substr(1), s2, c);
      if (res >= 0) changes = min(changes, res + 1);
    } else
    if (s2.length() > 0 && c == s2[0]) {
      int res = calc(s1, s2.substr(1), c);
      if (res >= 0) changes = min(changes, res + 1);
    } else
    if (s2.length() > 0 && c == s2[0]) {
      int res = calc(c + s1, s2, c);
      if (res >= 0) changes = min(changes, res + 1);
    } else
    if (s1.length() > 0 && c == s1[0]) {
      int res = calc(s1, c + s2, c);
      if (res >= 0) changes = min(changes, res + 1);
    }
  }

  return changes == 100000?-1:changes;
}

void solve(int t) {
  int n; cin >> n;
 
  vector<string> ss; 
  for (int i = 0; i < n; i++) {
    string s; cin >> s; ss.push_back(s);
  }
  
  int res = calc(ss[0], ss[1], '!');

  if (res < 0)
    cout << "Case #" << t << ": " <<  "Fegla Won" << endl;
  else
    cout << "Case #" << t << ": " <<  res << endl;
}

int main() {
  int tc; cin >> tc;
  
  for (int i = 1; i <= tc; i++) solve(i);

  return 0;
}
