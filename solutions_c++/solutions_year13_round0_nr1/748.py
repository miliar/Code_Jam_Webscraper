#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <numeric>
#include <utility>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

class Board {
  static const int N = 4;
  
  public:

  void read() {
    for (int i = 0; i < N; ++i)
      scanf("%s", board_[i]);
  }

  int status() const {
    if (checkWin('X')) return 1;
    if (checkWin('O')) return 2;
    return isFull() ? 0 : 3;
  }

  private:
  bool check(int i, int j, char p) const {
    return board_[i][j] == p || board_[i][j] == 'T';
  }

  bool checkWin(char p) const {
    for (int i = 0; i < N; ++i) {
      int j;
      for (j = 0; j < N; ++j) {
        if (!check(i, j, p)) break;
      }
      if (j == N) return true;
    }

    for (int i = 0; i < N; ++i) {
      int j;
      for (j = 0; j < N; ++j) {
        if (!check(j, i, p)) break;
      }
      if (j == N) return true;
    }
    int i;
    for (i = 0; i < N; ++i) {
      if (!check(i, i, p)) break;
    }
    if (i == N) return true;

    for (i = 0; i < N; ++i) {
      if (!check(i, N-i-1, p)) break;
    }
    if (i == N) return true;
    return false;
  }
  
  bool isFull() const {
    for (int i = 0; i < N; ++i)
      if (count(board_[i], board_[i] + N, '.'))
        return false;
    return true;
  }

  char board_[N][N+1];
};

int main() {
  int t;
  scanf("%d", &t);
  for (int ti = 1; ti <= t; ++ti) {
    Board b;
    b.read();
    printf("Case #%d: ", ti);
    switch (b.status()) {
      case 1:
      printf("X won\n");
      break;
      case 2:
      printf("O won\n");
      break;
      case 3:
      printf("Game has not completed\n");
      break;
      default:
      printf("Draw\n");
    }
  }
  return 0;
}
