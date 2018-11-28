#include <iostream>
using namespace std;

char a[4][4];

int solve() {
  int d = 0;
   // raw, column のみ調べる
  int x1 = 0, x2 = 0,  o1 = 0, o2 = 0;
  for (int i = 0; i < 4; i++) {
    x1 = x2 = o1 = o2 = 0;
    for (int j = 0; j < 4; j++) {
      if (a[j][i] == 'X') x1++;
      else if (a[j][i] == 'O') o1++;
      else if (a[j][i] == 'T') {
	x1++;
	o1++;
      }
      else d = 1; 
      if (a[i][j] == 'X') x2++;
      else if (a[i][j] == 'O') o2++;
      else if (a[i][j] == 'T') {
	x2++;
	o2++;
      }
      else d = 1; 
      // printf("i: %d j: %d x1: %d x2: %d o1: %d o2: %d\n", i, j, x1, x2, o1, o2);
    }
    if (x1 == 4 || x2 == 4) return 0;
    else if (o1 == 4 || o2 == 4) return 1;
  }

  // diagonal を調べる
  x1 = x2 = o1 = o2 = 0;
  for (int i = 0; i < 4; i++) {
    if (a[i][i] == 'X') x1++;
    else if (a[i][i] == 'O') o1++;
    else if (a[i][i] == 'T') {
      x1++;
      o1++;
    }
    else d = 1;
    // printf("i: %d x1: %d o1: %d\n", i, x1, o1);
  }
  for (int i = 3; i >= 0; i--) {
    int j = 3 - i;
    if (a[j][i] == 'X') x2++;
    else if (a[j][i] == 'O') o2++;
    else if (a[j][i] == 'T') {
      x2++;
      o2++;
    }
    else d = 1;
    // printf("i: %d j: %d x2: %d o2: %d\n", i, j, x2, o2);
  }
  if (x1 == 4 || x2 == 4) return 0;
  else if (o1 == 4 || o2 == 4) return 1;
  else if (d == 1) return 3;

  return 2;
}

int main() {
  int t, ans;
  cin >> t;
  for (int i = 1; i <= t; i++) {
    for (int j = 0; j < 4; j++) {
      cin >> a[j][0] >> a[j][1] >> a[j][2] >> a[j][3];
    }
    ans = solve();
    switch (ans) {
    case 0: printf("Case #%d: X won\n", i);
      break;
    case 1: printf("Case #%d: O won\n", i);
      break;
    case 2: printf("Case #%d: Draw\n", i);
      break;
    case 3: printf("Case #%d: Game has not completed\n", i);
      break;
    }
  }
  return 0;

}
