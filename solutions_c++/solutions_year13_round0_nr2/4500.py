#include <iostream>
#include <cmath>
#include <fstream>
#include <sstream>
#include <map>
#include <vector>
#include <algorithm>

const int MAXN = 105;
int mat[MAXN][MAXN];
struct cube {
  short x,y,h;
};

bool myc(const cube a, const cube b)
{
  return (a.h<b.h);
}

bool solve()
{
  int n, m;
  scanf("%d %d", &n, &m);
  for (int i=0; i<n; ++i)
    for (int j=0; j<m; ++j)
      scanf("%d", &mat[i][j]);

  std::vector<cube> mc(n*m);
  std::vector<bool> flag(n*m, false);
  for (int i=0; i<n; ++i)
    for (int j=0; j<m; ++j) {
      mc[i*m+j].x = i;
      mc[i*m+j].y = j;
      mc[i*m+j].h = mat[i][j];
    }
  
  sort(mc.begin(), mc.end(), myc);
  
  for (int i=0; i<n*m; ++i) {
    int x(mc[i].x), y(mc[i].y), h(mc[i].h);
    int j;
    if (flag[x*m+y]) continue;
    
    for (j=0; j<m; ++j) {
      if (mat[x][j]>h) break;
    }
    
    if (j<m) {
      int k;
      for (k=0; k<n; ++k) {
        if (mat[k][y]>h) break;
      }
      if (k==n) {
        for (k=0; k<n; ++k)
          flag[k*m+y] = true;
      }
    } else {
      int k;
      for (k=0; k<m; ++k)
        flag[x*m+k] = true;
    }
    
    if (!flag[x*m+y]) return false;
  }
  
  return true;
}

int main()
{
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);

  int n=0;
  scanf("%d", &n);

  for (int i=1; i<=n; ++i)
    printf("Case #%d: %s\n", i, (solve()?"YES":"NO"));

  fclose(stdin);
  fclose(stdout);
  
  return 0;
}
