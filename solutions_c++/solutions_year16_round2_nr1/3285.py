#include <bits/stdc++.h>
using namespace std;

void p(char c, int k) {
    cout << string(k, c);
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": ";
    string s;
    cin >> s;
    int ZERO = 0;
    int ONE = 0;
    int TWO = 0;
    int THREE = 0;
    int FOUR = 0;
    int FIVE = 0;
    int SIX = 0;
    int SEVEN = 0;
    int EIGHT = 0;
    int NINE = 0;
    for (char &c : s) {
        if (c == 'Z')      ZERO++;
        else if (c == 'O') ONE++;
        else if (c == 'W') TWO++;
        else if (c == 'H') THREE++;
        else if (c == 'F') FOUR++;
        else if (c == 'V') FIVE++;
        else if (c == 'X') SIX++;
        else if (c == 'S') SEVEN++;
        else if (c == 'G') EIGHT++;
        else if (c == 'I') NINE++;
    }
    // ZERO, TWO, SIX, EIGHT done
    THREE -= EIGHT;
    SEVEN -= SIX;
    FIVE -= SEVEN;
    FOUR -= FIVE;
    ONE -= ZERO + TWO + FOUR;
    NINE -= FIVE + SIX + EIGHT;
    p('0', ZERO);
    p('1', ONE);
    p('2', TWO);
    p('3', THREE);
    p('4', FOUR);
    p('5', FIVE);
    p('6', SIX);
    p('7', SEVEN);
    p('8', EIGHT);
    p('9', NINE);
    cout << endl;
  }
  return 0;
}
