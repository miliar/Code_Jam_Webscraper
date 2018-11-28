#include <iostream>
using namespace std;

int main() {
  int tmp;
  //short table[11][2] = {{0, 0}, {0, 1}, {0, 2}, {0, 3}, {1, 2}, {1, 3}, {1, 3}, {2, 3}, {2, 3}, {2, 3}, {3, 3}};
  short table[1001][1001];
  for (int i=1; i<= 1000; ++i) {
    for (int j=1; j<= 1000; ++j) {
      if (i >= j) {
        table[i][j] = 0;
        continue;
      }
      table[i][j] = j;
      for (int k = 1; k <= j/2; ++k) {
        tmp = table[i][k] + table[i][j - k] + 1;
        if (tmp < table[i][j]) {
          table[i][j] = tmp;
        }
      }
    }
  }
  int T, D;
  int P[1001];

  cin >> T;
  for (int k = 1; k <= T; ++k) {
    cin >> D;
    int bound = 0, Tmax = 0;

    for (int i = 0; i < D; ++i) {
      cin >> P[i];
      if (P[i] > bound) {
        bound = P[i];
      }
    }
    Tmax = bound;
    while(--bound >= 1) {
      tmp = bound;
      for (int i = 0; i < D; ++i) {
        tmp += table[bound][P[i]];
      }
      if (tmp < Tmax)
        Tmax = tmp;
    }

    cout << "Case #" << k << ": " << Tmax << endl;
  }

  return 0;
}
