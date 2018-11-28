#include <iostream>
#include <vector>

using namespace std;

int FixPancakes(string s) {
  if (s.size() == 0) return 0;
  if (s.size() == 1) {
    if (s[0] == '+') return 0;
    if (s[0] == '-') return 1;
  }
  if (s[s.size() - 1] == '+') {
    return FixPancakes(s.substr(0, s.size() - 1));
  }
  // Start from behind and find the first +.
  int neg_pos = s.size() - 1;
  for (; neg_pos >=0; neg_pos--) {
    if (s[neg_pos] == '+') break;
  }
  if (neg_pos == -1) return 1;
  return 2 + FixPancakes(s.substr(0, neg_pos + 1));
}

int main(int argc, char** argv) {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    string S;
    cin >> S;
    cout << "Case #" << i << ": " << FixPancakes(S) << endl;
  }
  return 0;
}
