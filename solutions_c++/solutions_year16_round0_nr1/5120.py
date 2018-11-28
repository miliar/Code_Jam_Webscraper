#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

const char INPUT[] = "HelloWorld.inp";
const char OUTPUT[] = "HelloWorld.out";

int main() {
  freopen(INPUT, "r", stdin);
  freopen(OUTPUT, "w", stdout);

  int numTest;
  cin >> numTest;

  for (int idTest = 0; idTest < numTest; ++ idTest) {
    int n;
    bool isDigitAppeared[10];
    int countAppearDigit = 0;
    for (int digit = 0; digit < 10; ++ digit) {
      isDigitAppeared[digit] = false;
    }
    cin >> n;
    if (n == 0) {
      cout << "Case #" << idTest + 1 << ": INSOMNIA" << endl;
      continue;
    }

    int turn = 1;
    while (countAppearDigit < 10) {
      int tmp = turn * n;
      while (tmp > 0) {
        if (isDigitAppeared[tmp % 10] == false) {
          isDigitAppeared[tmp % 10] = true;
          ++ countAppearDigit;
        }
        tmp /= 10;
      }
      ++ turn;
    }

    cout << "Case #" << idTest + 1 << ": " << (turn - 1) * n << endl;
  }

  return 0;
}
