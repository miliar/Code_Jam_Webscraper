#include <iostream>

using namespace std;

int main() {
  int t;
  cin >> t;

  string s;
  getline(cin, s);
  for (int i = 0; i < t; i++) {
    getline(cin, s);
    char curSeq = s[0];
    int numFlips = 0;
    int lastFlip = -1; 

    for (int j = 0; j < s.length(); j++) {
      if (s[j] != curSeq) {
        numFlips += 1;
        curSeq = curSeq == '+' ? '-' : '+';
      }
    }

    if (curSeq == '-') {
      numFlips += 1;
    }

    cout << "Case #" << (i+1) << ": " << numFlips << endl;
  }
  return 0;
}
