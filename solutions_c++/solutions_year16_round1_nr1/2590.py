#include <iostream>
#include <string>
using namespace std;

int main() {

  int T;
  cin >> T;

  for (int t = 0; t < T; t++) {
    string S;
    cin >> S;

    string S2;

    for (int i = 0; i < S.size(); i++) {
      if (S[i] >= S2[0]) {
        S2 = S[i] + S2;
      } else {
        S2 = S2 + S[i];
      }
    }

    cout << "Case #" << t + 1 << ": " << S2 << endl;
  }


  return 0;
}
