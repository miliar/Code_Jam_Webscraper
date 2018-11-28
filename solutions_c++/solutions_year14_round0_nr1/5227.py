#include <iostream>
#include <cstdio>
#include <memory.h>
using namespace std;

const int maxn = 5;
int m1[maxn][maxn], m2[maxn][maxn];
int a,b;

void read() {
  scanf("%d",&a);
  for (int i=0;i<4;i++) {
    for (int j=0;j<4;j++) {
      scanf("%d",&m1[i][j]);
    }
  }

  scanf("%d",&b);
  for (int i=0;i<4;i++) {
    for (int j=0;j<4;j++) {
      scanf("%d",&m2[i][j]);
    }
  }
  a--;
  b--;
  return;
}

void solve() {
  int cnt = 0;
  int bj = -1;
  for (int i=0;i<4;i++) {
    for (int j=0;j<4;j++) {
      if (m1[a][i] == m2[b][j]) {
        bj = i;
        cnt++;
      }
    }
  }
  if (cnt == 0) {
    puts("Volunteer cheated!");
  } else if (cnt == 1) {
    printf("%d\n", m1[a][bj]);
  } else {
    puts("Bad magician!");
  }
  return;
}

int main() {
  //freopen("data.in", "r", stdin);
  //freopen("A-small-attempt0.in", "r", stdin);
  //freopen("data.out", "w", stdout);
  int cas;
  scanf("%d",&cas);
  for (int i=1;i<=cas;i++) {
    printf("Case #%d: ", i);
    read();
    solve();
  }
  return 0;
}
