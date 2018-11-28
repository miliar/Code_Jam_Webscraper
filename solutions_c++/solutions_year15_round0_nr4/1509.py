#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
const double PI = acos(-1);
const double EPS = 1e-7;

#define PB push_back
#define MP make_pair
#define FOR(_i, _from, _to) for (int (_i) = (_from), (_batas) = (_to); (_i) <= (_batas); (_i)++)
#define REP(_i, _n) for (int (_i) = 0, (_batas) = (_n); (_i) < (_batas); (_i)++)
#define SZ(_x) ((int)(_x).size())

int tc;

bool richardWin(int X, int R, int C) {
  // define R >= C
  if (C > R) swap(C, R);
  
  if (X >= 7) return true;
  if ((R*C) % X) return true;
  if (X > R) return true;
  if (X - C > C) return true;
  if (X > C) {
    if (X - C - 1 >= C-1) {
      int sisa = X-(C+1)-(C-1);
      for (int kiri = 0; kiri <= sisa; kiri++) {
        int kosongKiri = C-1 - kiri;
        int kosongKanan = R*C - (C+1)-(C-1)-(kosongKiri) - (sisa - kiri);
        bool valid = true;
        for (int i = (C+1); i <= R; i++) {
          if ((kosongKiri % X == 0) && (kosongKanan % X == 0)) {
            valid = false;
            break;
          }
        }
        if (valid) return true;
      }
    }
  }
  return false;
}

void solve() {
  int X, R, C;
  scanf("%d %d %d", &X, &R, &C);
  
  printf("Case #%d: ", tc);
  if (richardWin(X, R, C)) puts("RICHARD");
  else puts("GABRIEL");
}

int main() {
  int T;
  scanf("%d", &T);
  for (tc = 1; tc <= T; tc++) solve();
	return 0;
}
