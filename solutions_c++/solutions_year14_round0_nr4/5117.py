#include <iostream>
#include <cstdio>
#include <memory.h>
#include <algorithm>
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
using namespace std;

const int maxn = 1010;
const int dir[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};
const int move[8][2] = {{-1,-1}, {-1,0}, {-1,1}, {0,-1}, {0,1}, {1,-1}, {1,0}, {1,1}};
int m,n,c;
int mat[maxn][maxn];

bool judge(int x, int y) {
  if (x >= 0 && y >= 0 && x < m && y < n) {
    return true;
  }
  return false;
}

void fillMat() {
  int cc = c;
  /*int x = 0, y = 0;
  int go = 0;
  while(c--) {
    mat[x][y] = 0;
    int tx = x + dir[go][0];
    int ty = y + dir[go][1];
    if (!judge(tx, ty) || mat[tx][ty] == 0) {
      go = (go + 1) % 4;
    }
    x += dir[go][0];
    y += dir[go][1];
  }*/
  for (int i=0;i<m;i++) {
    if (!cc) break;
    for (int j=0;j<n;j++) {
      mat[i][j] = 0;
      cc--;
      if (!cc) break;
    }
  }
  return;
}

bool check(int x, int y) {
  for (int i=0;i<8;i++) {
    int tx = x + move[i][0];
    int ty = y + move[i][1];
    if (judge(tx, ty) && mat[tx][ty] == -1) return true;
  }
  return false;
}

void solve() {
  memset(mat,-1,sizeof(mat));
  fillMat();

  for (int i=0;i<m;i++) {
    for (int j=0;j<n;j++) {
      if (mat[i][j] == 0) continue;
      int cnt = 0;
      for (int k=0;k<8;k++) {
        int tx = i + move[k][0];
        int ty = j + move[k][1];
        if (judge(tx, ty) && mat[tx][ty] == 0) {
          cnt++;
        }
      }
      if (cnt > 0) mat[i][j] = cnt;
    }
  }

  bool flag = true;
  for (int i=0;i<m;i++) {
    for (int j=0;j<n;j++) {
      if (mat[i][j] > 0 && !check(i,j)) {
        flag = false;
        break;
      }
    }
    if (!flag) break;
  }

  if (!flag) {
    int fuck = -1;
    int left = m*n-c;
    for (int i=2;i<=m;i++) {
      int tmp = left / i * i;
      if (tmp == left && left / i <= n && left > i) {
        fuck = i;
        break;
      }
    }
    if (fuck != -1) {
      for (int i=0;i<m;i++) {
        for (int j=0;j<n;j++) {
          if (i == 0 && j == 0) printf(".");
          else if (i < fuck && j < left / fuck) printf(".");
          else printf("*");
        }
        puts("");
      }
    } else {
      puts("Impossible");
    }
  } else {
    bool click = false;
    for (int i=0;i<m;i++) {
      for (int j=0;j<n;j++) {
        if (mat[i][j] == 0) printf("*");
        else if (mat[i][j] == -1 && !click) {printf("c"); click = true;}
        else printf(".");
      }
      puts("");
    }
  }

  return;
}

double naomi[maxn], ken[maxn];

void yamiedie() {
  for (int i=0;i<n;i++) {
    scanf("%lf", &naomi[i]);
  }
  for (int i=0;i<n;i++) {
    scanf("%lf", &ken[i]);
  }
  sort(naomi, naomi+n);
  sort(ken, ken+n);

  int ans1 = 0, ans2 = maxn;
  for (int i=0;i<n;i++) {
    for (int j=0;j<n;j++) {
      int c1 = 0, c2 = 0;
      for (int k=0;k<n;k++) {
        if (i+k < n && j+k < n) {
          if (naomi[i+k] > ken[j+k]) c1++;
          else c2++;
        }
        ans1 = MAX(ans1, c1);
        ans2 = MIN(ans2, n-c2);
      }
    }
  }
  printf("%d %d\n", ans1, ans2);
  return;
}

int main() {
  //freopen("data.in", "r", stdin);
  //freopen("D-small-attempt0.in", "r", stdin);
  //freopen("B-large.in", "r", stdin);
  //freopen("data.out", "w", stdout);
  int cas;
  scanf("%d",&cas);
  for (int i=1;i<=cas;i++) {
    //printf("Case #%d:\n", i);
    printf("Case #%d: ", i);
    scanf("%d",&n);
    //solve();
    yamiedie();
  }
  return 0;
}
