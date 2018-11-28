#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <map>
#include <iostream>

using namespace std;
const int MAX_N = 200;
int copia[MAX_N][MAX_N], visited[MAX_N][MAX_N], t[MAX_N][MAX_N];
int n, m;

int fill(int num, int a, int b, int k, int p) {
  if (a < 0 || b < 0 || a == n || b == m) {
    return 1;
  }
  if (t[a][b] > num) return 0;
  if (fill(num, a+k, b+p, k, p)) {
    copia[a][b] = num;
    return 1;
  } 
  return 0;
}

void clear() {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      visited[i][j] = 0;
    }
  }
}

int solve() {
  for (int i = 0; i < n; i++) 
    for (int j = 0; j < m; j++) copia[i][j] = 100;
  
  for (int i = 99; i >= 1; i--) {
    for (int j = 0; j < n; j++) {
      fill(i, j, 0, 0, 1);
      fill(i, j, m-1, 0, -1);
    }
    
    for (int j = 0; j < m; j++) {
      fill(i, 0, j, 1, 0);
      fill(i, n-1, j, -1, 0);
    }
  }

  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++) 
      if (t[i][j] != copia[i][j]) return 0;
    
  return 1;
	 
}
int main() {
  int T;
  scanf("%d",&T);
  for (int cases = 1; cases <= T; cases++) {
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
      for (int j = 0; j < m; j++)
	scanf("%d",&t[i][j]);
    printf("Case #%d: ", cases);
    if (solve()) printf("YES\n");
    else printf("NO\n");
  }
  return 0;
}
