#include <iostream>
using namespace std;

int main() {
  int t;
  cin >> t;
  for (int z = 1; z <= t; ++z) {
    string s;
    cin >> s;
    s += '+';
    int c = 0;
    for (int i = 1; i < int(s.size()); ++i) if (s[i] != s[i - 1]) ++c;
    cout << "Case #" << z << ": " << c << endl;
  }
}