#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

int main() {
  int T;
  T = 100;
  for (int I = 0; I < T; I++) {
    int r1, r2, m1[4][4], m2[4][4];
    cin >> r1;
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
	cin >> m1[i][j];
      }
    }
    cin >> r2;
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
	cin >> m2[i][j];
      }
    }
    int match = 0;
    int num = -1;
    int ns[17] = {0};
    for (int i = 0; i < 4; i++) {
      ns[m1[r1 - 1][i]] = 1;
    }
    for (int i = 0; i < 4; i++) {
      if (ns[m2[r2 - 1][i]] == 1) {
	match++;
	num = m2[r2 - 1][i];
      }
    }
    cout << "Case #" << I + 1 << ": ";
    if (match > 1) {
      cout << "Bad magician!" << endl;
    } else if (match < 1) {
      cout << "Volunteer cheated!" << endl;
    } else {
      cout << num << endl;
    }
  }
}
