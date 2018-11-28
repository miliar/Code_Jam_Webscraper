
#include <iostream>
#include <string>
using namespace std;

int main() {
  int T; cin >> T;
  for (int i = 1; i <= T; i++) {
    string s; cin >> s;
    int count = 0;
    for (int j = 1; j < s.length(); j++) {
      if (s[j] == s[j-1]) continue;
      count++;
    }
    if (s[s.length()-1] == '-')
      count++;
    cout << "Case #" << i << ": " << count << endl; 
  }
  return 0;
}

