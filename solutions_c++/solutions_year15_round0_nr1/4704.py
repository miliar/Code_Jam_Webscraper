#include <string>
#include <fstream>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
  ifstream cin("A-small-attempt1.in");
  ofstream cout("A.out");

  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int Smax;
    cin >> Smax;
    string S;
    cin >> S;
    int standing = 0, needed = 0;
    for (int i = 0; i < Smax + 1; i++) {
      if ((S[i] - '0' > 0) && standing < i) {
        needed += i - standing;
        standing += needed;
      }
      standing += S[i] - '0';
    }
    cout << "Case #" << t << ": " << needed << endl;
  }
  return 0;
}