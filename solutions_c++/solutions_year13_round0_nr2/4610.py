#include <cstdio>
#include <algorithm>
#define R 100

using namespace std;

int main() {
  int t;
  scanf("%d", &t);
  int n,m, l[R][R];
  int max_x[R];
  int max_y[R];
  
  for (int i=1; i<=t; ++i) {
    scanf("%d %d", &n, &m);
    for (int j=0; j<n; ++j) {
      for (int k=0; k<m; ++k) {
        scanf("%d", &l[j][k]);
      }
    }
    
    for (int j=0; j<n; ++j) {
      max_x[j] = 0;
      for (int k=0; k<m; ++k) {
        max_x[j] = max(max_x[j], l[j][k]);
      }
    }
    
    for (int k=0; k<m; ++k) {
      max_y[k] = 0;
      for (int j=0; j<n; ++j) {
        max_y[k] = max(max_y[k], l[j][k]);
      }
    }
    
    bool no = false;
    for (int j=0; j<n; ++j) {
      for (int k=0; k<m; ++k) {
        //printf("j:%d k:%d %d %d %d\n",j,k,l[j][k]);
        if (l[j][k]<max_x[j] && l[j][k]<max_y[k]) {
          no = true;
          break;
        }
      }
      if (no) break;
    }
    
    if (no)
      printf("Case #%d: NO\n", i);
    else
      printf("Case #%d: YES\n", i);
    
  }
  
}