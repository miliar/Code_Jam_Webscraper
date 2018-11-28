#include <iostream>
#include <string>

using namespace std;

int main() {
  int numCases; cin >> numCases;
  string asdf; getline(cin, asdf);
  for (int thisCase = 1; thisCase <= numCases; ++thisCase) {
    string s; getline(cin, s);
    string t = ""; t += s[0];
    for (int i = 1; i < s.size(); ++i) {
      if (s[i] < t[0]) t += s[i];
      else t = s.substr(i, 1) + t;
    }
    cout << "Case #" << thisCase << ": " << t << endl;
  }
  return 0;
}
