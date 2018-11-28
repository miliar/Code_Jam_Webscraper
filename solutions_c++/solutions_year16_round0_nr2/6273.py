#include <iostream>
#include <string>
using namespace std;

void dw(size_t caseNo) {
  string S;
  cin >> S;
  S.append("+");
  size_t ans = 0;
  for (int i = 0; i + 1 < S.length(); i++) {
    if (S[i] != S[i + 1]) {
      ans++;
    }
  }
  cout << "Case #" << caseNo << ": " << ans << endl;
}

int main() {
  size_t T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    dw(i);
  }
  return 0;
}

