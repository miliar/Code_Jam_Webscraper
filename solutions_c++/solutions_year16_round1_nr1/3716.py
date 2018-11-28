#include <iostream>
#include <string>
using namespace std;

string fun(string S) {
  if (S.length() == 1) {
    return S;
  }
  string max_s = fun(S.substr(0, S.length() - 1));
  char c = S[S.length() -1];
  string s1 = max_s + c;
  string s2 = c + max_s;
  return s1 > s2 ? s1 : s2;
}

int main() {
  int T = 0;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    string S;
    cin >> S;
    cout << "Case #" << i << ": " << fun(S) << endl;
  }
}
