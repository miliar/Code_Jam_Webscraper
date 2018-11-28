#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <vector>
#include <iomanip>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <ctime>
#include <functional>

#define pb push_back
#define mk make_pair
#define sqr(N) ((N)*(N))
#define F first
#define S second
#define maxn 101010

using namespace std;                         

typedef long long ll;

const int a1[] = {0, 0, 1, -1, 1, 1, -1, -1};
const int a2[] = {1, -1, 0, 0, 1, -1, -1, 1};

int i, j, t, r, c, m, n, f[55][55];
char matrix[55][55];
bool ok;

void write() {
  for(int i = 1; i <= r; i++) {
    for(int j = 1; j <= c; j++) {
      printf("%c", matrix[i][j]);
    }
    printf("\n");
  }
}

void go2(int i, int j) {
  f[i][j] = 1;
  bool ok = true;
  for(int t = 0; t < 8; t++) {
    int x, y;
    x = i + a1[t];
    y = j + a2[t];
    if(matrix[x][y] == '*') ok = false;
  }  
  if(ok)
    for(int t = 0; t < 8; t++) {
      int x, y;
      x = i + a1[t];
      y = j + a2[t];
      if(!f[x][y] && x > 0 && y > 0 && x <= r && y <= c) go2(x, y);
    }  
} 


bool check() {
  if(r * c - m == 1) return true;
  memset(f, 0, sizeof(f));
  int i, j, x, y;
  for(i = 1; i <= r; i++)
    for(j = 1; j <= c; j++) if(matrix[i][j] == 'c') x = i, y = j;
  for(i = 0; i < 8; i++) if(matrix[x + a1[i]][y + a2[i]] == '*') return false;
  go2(x, y);
  for(i = 1; i <= r; i++)
    for(j = 1; j <= c; j++) if(matrix[i][j] == '.' && !f[i][j]) return false;
  return true;
}



void go(int x, int y, int k) {
  if(ok) return;
  if(y > c) {
    x++;
    y = 1;
    if(x > r) {
      if(!k && check()) {
        write();
        ok = true;  
      } 
      return;
    }
  }
  if(matrix[x][y] == 'c') {
    go(x, y + 1, k);
  }
  else {
    if(k) {
      matrix[x][y] = '*';
      go(x, y + 1, k - 1);
    }
    matrix[x][y] = '.';
    go(x, y + 1, k);
  }
}

int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  scanf("%d", &t);
  for(int test = 1; test <= t; test++) {
    printf("Case #%d:\n", test);
    scanf("%d%d%d", &r, &c, &m);
    ok = false;
    for(i = 1; i <= r; i++)
      for(j = 1; j <= c; j++) if(!ok) {
        memset(matrix, 0, sizeof(matrix));
        matrix[i][j] = 'c';
        go(1, 1, m);
      }
    if(!ok) puts("Impossible");
  }
  return 0;
}         