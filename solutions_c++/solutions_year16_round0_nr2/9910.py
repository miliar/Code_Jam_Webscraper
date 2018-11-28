#include <iostream>
#include <string>
using namespace std;

int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; ++t) {
    string S; cin >> S;
    S += '+';
    int res = 0;
    for (size_t i = 1; i < S.size(); ++i)
      if (S[i] != S[i-1]) ++res;
    cout << "Case #" << t << ": " << res << endl;
  }
}