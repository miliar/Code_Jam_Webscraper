#include <iostream>
#include <string>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int x=1; x<=T; ++x) {
    string S;
    cin >> S;
    string y = "";
    for (int i = 0; i < S.size(); i++) {
      if (S[i] >= y[0]) {
        y = S[i] + y;
      } else {
        y = y + S[i];
      }
    }
    cout << "Case #" << x << ": " << y << endl;
  }
  return 0;
}
