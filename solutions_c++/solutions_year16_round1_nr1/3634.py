#include <iostream>

using namespace std;
int main(int argc, char** argv) {
  int T;
  cin >> T;

  for (int t = 1; t <= T; t++) {
    string S;
    cin >> S;

    string lastWord;

    lastWord = string(1, S[0]);
    for (int i = 1; i < S.length(); i++) {
      if (lastWord[0] <= S[i])
        lastWord = S[i] + lastWord;
      else
        lastWord += S[i];
    }

    cout << "Case #" << t << ": " << lastWord << endl;
  }
  return 0;
}
