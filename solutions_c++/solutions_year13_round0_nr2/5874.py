#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;
#define MAXN 103

int a[MAXN][MAXN];
int curr[MAXN][MAXN];
int n, m;

int check(int x, int y, int dx, int dy, int cmp) {
  for(; x < n && y < m; x += dx, y += dy) {
    if(a[x][y] > cmp)
      return 0;  
  }
  return 1;
}

void set_val(int x, int y, int dx, int dy, int val) {
  for(; x < n && y < m; x += dx, y += dy) {
    a[x][y] = val;  
  }  
}

void run() {
  scanf("%d%d", &n, &m);
  for(int i = 0; i < n; ++i)
    for(int j = 0; j < m; ++j)
      scanf("%d", &a[i][j]);
  
  for(int i = 0; i < n; ++i) {
    for(int j = 0; j < m; ++j) {
      if(1 == a[i][j]) {
        if(!check(i, 0, 0, 1, 1) && !check(0, j, 1, 0, 1)) {
          printf("NO\n");
          return;  
        }  
      }  
    }  
  }
  printf("YES\n");
}

int main() {
  int T;
  scanf("%d", &T);
  for(int i = 0; i < T; ++i) {
    printf("Case #%d: ", i+1);
    run();
  }
  return 0;  
}
