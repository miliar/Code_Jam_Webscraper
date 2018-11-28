// Author: Chi-Kit (George) LAM
#include <bits/stdc++.h>
using namespace std;
namespace jam{
  typedef long long LL;
  int InitJam() {
    cout.precision(9);
    return 0;
  }
} // namespace jam
using namespace jam;
int initjam = InitJam();

int R, C;
char A[200][200];
int M[400];

void locate(int s, int& x, int&y, int& dir) {
  if (s < C) {
    dir = 0; x = s; y = 0;
  } else if (s < C + R) {
    dir = 3; x = C - 1; y = s - C;
  } else if (s < 2 * C + R) {
    dir = 2; x = 2 * C + R - s - 1; y = R - 1;
  } else {
    dir = 1; x = 0; y = 2 * (C + R) - s - 1;
  }
}

bool search(int s) {
  int dir, x, y;
  locate(s, x, y, dir);
  int oldx, oldy;
  
  while ( x >= 0 && x < C && y >= 0 && y < R) {
    oldx = x;
    oldy = y;
    if (dir == 0) {
      if (A[y][x] == '/') {
        dir = 3; x -= 1;
      } else {
        A[y][x] = '\\';
        dir = 1; x += 1;
      }
    } else if (dir == 1) {
      if (A[y][x] == '\\') {
        dir = 0; y += 1;
      } else {
        A[y][x] = '/';
        dir = 2; y -= 1;
      }
    } else if (dir == 2) {
      if (A[y][x] == '/') {
        dir = 1; x += 1;
      } else {
        A[y][x] = '\\';
        dir = 3; x -= 1;
      }
    } else {
      if (A[y][x] == '\\') {
        dir = 2; y -= 1;
      } else {
        A[y][x] = '/';
        dir = 0; y += 1;
      }
    }
        //cout << x << y << dir << endl;
  }
  int tx, ty, tdir;
  locate(M[s], tx, ty, tdir);
  if ( oldx != tx || oldy != ty) {
    return false;
  }
  return true;
}

void solve(int T) {
  cout << "Case #" << T << ":" << endl;
  cin >> R >> C;
  for (int i=0; i<R+C; ++i) {
    int x, y;
    cin >> x >> y;
    M[x-1] = y-1;
    M[y-1] = x-1;
  }
  for (int i=0; i<R; ++i) {
    for (int j=0; j<C; ++j) {
      A[i][j] = ' ';
    }
  }
  stack<int> S;
  for (int i=0; i<2*(R+C); ++i) {
    if (M[i] > i) {
      S.push(i);
    } else {
      if (S.empty() || S.top() != M[i]) {
        cout << "IMPOSSIBLE" << endl;
        return;
      }
      S.pop();
      if (!search(M[i])) {
        cout << "IMPOSSIBLE" << endl;
        return;
      }
    }
  }
  
  for (int i=0; i<R; ++i) {
    for (int j=0; j<C; ++j) {
      cout << ((A[i][j] == ' ') ? '/' : A[i][j]);
    }
    cout << endl;
  }
}
int main(){
  int T;
  cin >> T;
  for (int i=0; i<T; ++i) {
    solve(i+1);
  }
  return 0;
}
