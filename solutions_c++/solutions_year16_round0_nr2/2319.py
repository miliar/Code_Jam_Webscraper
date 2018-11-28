#include <algorithm> 
#include <iostream>
#include <vector>
#include <string>
using namespace std;


int main() {
  int T;
  cin >> T;
  string s;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    cin >> s;
    int c = 0;
    if (s[0] == '-') c++;
    int i = 0;
    while (i < s.size() && s[i] == '-') i++;
    while (i < s.size()) {
      if (s[i] == '-') {
        c += 2;
        while (i < s.size() && s[i] == '-') i++;
      } else {
        i++;
      }
    }
    cout << c << endl;
  }
}
