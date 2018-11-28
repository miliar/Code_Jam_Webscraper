#include <iostream>

using namespace std;

int main() {
  int T;
  cin >> T;

  for (int t = 1; t <= T; t++) {
    string S;
    cin >> S;

    string last_word = string(1, S[0]);

    for (int i = 1; i < S.length(); i++) {
      if (S[i] >= last_word[0]) {
        last_word = S[i] + last_word;
      } else {
        last_word += S[i];
      }
    }

    cout << "Case #" << t << ": " << last_word << endl;
  }
}