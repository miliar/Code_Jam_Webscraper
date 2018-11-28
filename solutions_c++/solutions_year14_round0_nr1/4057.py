#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int main() {
  int t;
  cin >> t;
  for (int ct = 0; ct < t; ++ct) {
    int a1, a2;
    int cards1[4][4];
    int cards2[4][4];
    cin >> a1;
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        cin >> cards1[i][j];
      }
    }
    cin >> a2;
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        cin >> cards2[i][j];
      }
    }
    int cnt = 0;
    int card = -1;
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        if (cards1[a1-1][i] == cards2[a2-1][j]) {
          card = cards1[a1-1][i];
          ++cnt;
        }
      }
    }
    cout << "Case #" << (ct+1) << ": ";
    if (cnt == 0) {
      cout << "Volunteer cheated!";
    }
    else if (cnt == 1) {
      cout << card;
    }
    else {
      cout << "Bad magician!";
    }
    cout << endl;
  }
  return 1;
}
