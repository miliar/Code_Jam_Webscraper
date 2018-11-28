#include <bits/stdc++.h>
using namespace std;
int r, c;
int m[10][10];
int dx[4] = {0, 0, -1, 1};
int dy[4] = {1, -1, 0, 0};
int ans[7][7];
int q;
set<string> sss;
void recur(int x, int y) {
  if (x == r + 1) {
    for (int i = 1; i <= r; i++) {
      for (int j = 1; j <= c; j++) {
        int count = 0;
        for (int k = 0; k < 4; k++) {
          int yy = j + dy[k];
          if (yy == c + 1) yy = 1;
          if (yy == 0) yy = c;
          count += (m[i + dx[k]][yy] == m[i][j]);
        }
        if (count != m[i][j]) {
          return ;
        }
      }
    }
    string s;
    for (int b = 0; b < c; b++) {
      s = "";
      for (int i = 1; i <= r; i++) {
        for (int j = 1; j <= c; j++) {
          s += 48 + m[i][((j - 1 + b) % c) + 1];
        }
      }
      //cout << s << "\n";
      if (sss.count(s)) {
        return ;
      }
    }
    sss.insert(s);
    q++;
    //printf("MATCH %d\n", q++);
    /*for (int i = 1; i <= r; i++) {
      for (int j = 1; j <= c; j++) {
        printf("%d", m[i][j]);
      }
      printf("\n");
    }*/
    return ;
  }
  if (y == c + 1) {
    for (int i = 1; i < x; i++) {
      for (int j = 1; j <= c; j++) {
        int count = 0;
        for (int k = 0; k < 4; k++) {
          int yy = j + dy[k];
          if (yy == c + 1) yy = 1;
          if (yy == 0) yy = c;
          count += (m[i + dx[k]][yy] == m[i][j]);
        }
        if (count != m[i][j]) {
          return ;
        }
      }
    }
    recur(x + 1, 1);
    return ;
  }
  if (m[x][y - 1] == 3 && m[x - 1][y - 1] != 3) {
    m[x][y] = 3;
    recur(x, y + 1);
    return ;
  }
  m[x][y] = 1;
  recur(x, y + 1);
  m[x][y] = 2;
  recur(x, y + 1);
  m[x][y] = 3;
  recur(x, y + 1);
}
int main() {
  for (r = 2; r <= 6; r++) {
    for (c = 3; c <= 6; c++) {
      sss.clear();
      q = 0;
      //printf("%d %d: ", r, c);
      recur(1, 1);
      ans[r][c] = q;
    }
  }
  int t;
  scanf("%d", &t);
  for (int tt = 1; tt <= t; tt++) {
    int r, c;
    scanf("%d %d", &r, &c);
    printf("Case #%d: %d\n", tt, ans[r][c]);
  }
  return 0;
}
