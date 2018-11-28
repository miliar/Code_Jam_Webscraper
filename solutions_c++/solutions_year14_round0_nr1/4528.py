#include <iostream>

using namespace std;

void solve(int TEST) {
  int table1[4][4];
  int table2[4][4];

  int a1, a2;

  cin >> a1;
  for (int i = 0; i < 4; ++i) for (int j = 0; j < 4; ++j) cin >> table1[i][j];

  cin >> a2;
  for (int i = 0; i < 4; ++i) for (int j = 0; j < 4; ++j) cin >> table2[i][j];

  --a1;
  --a2;

  int z = 0;
  int simao = 0;
  for (int i = 0; i < 4; ++i) {
    int k = 0;
    for (int j = 0; j < 4; ++j) {
      if (table1[a1][i] == table2[a2][j]) {
        simao = table1[a1][i];
        k++;
      }
    }

    if (k > 0) {
      z++;
    }
  }

  if (z == 0)
  printf("Case #%d: Volunteer cheated!\n", TEST);
  else if (z == 1)
  printf("Case #%d: %d\n", TEST, simao);
  else
  printf("Case #%d: Bad magician!\n", TEST);
}

int main() {
  int n = 0;

  cin >> n;
  for (int i = 0; i < n; i++) {
    solve(i+1);
  }
}

