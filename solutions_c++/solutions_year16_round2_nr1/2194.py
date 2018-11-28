#include <cstdio>
#include <iostream>

#define ZERO "ZERO"
#define ONE "ONE"
#define TWO "TWO"
#define THREE "THREE"
#define FOUR "FOUR"
#define FIVE "FIVE"
#define SIX "SIX"
#define SEVEN "SEVEN"
#define EIGHT "EIGHT"
#define NINE "NINE"

using namespace std;

void remove(string &S, const char *letters) {
  for (; *letters; letters++) {
    size_t pos = S.find_first_of(*letters);
    S.erase(pos, 1);
  }
}

int findAndRemove1(string &S) {
  int len = S.length();
  for (int i = 0; i < len; i++) {
    switch (S[i]) {
      case 'Z':
        remove(S, ZERO);
        return 0;
      case 'W':
        remove(S, TWO);
        return 2;
      case 'U':
        remove(S, FOUR);
        return 4;
      case 'X':
        remove(S, SIX);
        return 6;
      case 'G':
        remove(S, EIGHT);
        return 8;
    }
  }
  return -1;
}

int findAndRemove2(string &S) {
  int len = S.length();
  for (int i = 0; i < len; i++) {
    switch (S[i]) {
      case 'O':
        remove(S, ONE);
        return 1;
      case 'T':
        remove(S, THREE);
        return 3;
      case 'F':
        remove(S, FIVE);
        return 5;
      case 'S':
        remove(S, SEVEN);
        return 7;
    }
  }
  return -1;
}

int findAndRemove3(string &S) {
  int len = S.length();
  for (int i = 0; i < len; i++) {
    switch (S[i]) {
      case 'N':
        remove(S, NINE);
        return 9;
    }
  }
  return -1;
}

int main(int argc, char **argv) {
  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; t++) {
    string S;
    cin >> S;

    int digits[10] = {0};
    while (true) {
      int d = findAndRemove1(S);
      if (d == -1) {
        break;
      } else {
        digits[d]++;
      }
    }

    while (true) {
      int d = findAndRemove2(S);
      if (d == -1) {
        break;
      } else {
        digits[d]++;
      }
    }

    while (true) {
      int d = findAndRemove3(S);
      if (d == -1) {
        break;
      } else {
        digits[d]++;
      }
    }

    cout << "Case #" << t << ": ";
    for (int i = 0; i <= 9; i++) {
      for (int j = 0; j < digits[i]; j++) {
        cout << i;
      }
    }
    cout << endl;
  }

  return 0;
}
