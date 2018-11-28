#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int t; cin >> t;
  for (int tc = 1; tc <= t; ++tc) {
    string s; cin >> s;
    reverse(s.begin(), s.end());
    char current = '+';
    long switches = 0;
    for (string::iterator i = s.begin(); i != s.end(); ++i) {
      if (*i != current) {
	++switches;
	current = *i;
      }
    }
    cout << "Case #" << tc << ": " << switches << endl;
  }
}
