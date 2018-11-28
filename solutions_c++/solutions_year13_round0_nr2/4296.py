#include <cstdio>
#include <cstring>
#include <algorithm>

#define MAX 110

using namespace std;

int n,m;

int v[MAX][MAX];

int ml[MAX], mc[MAX];

int main() {
  int tt;
  scanf("%d", &tt);
  for (int t = 1; t <= tt; t++) {
    scanf("%d %d", &n, &m);
    for (int i = 0; i<n; i++)
      for (int j = 0; j<m; j++)
	scanf("%d", &v[i][j]);
    
    for (int i = 0; i<n; i++) {
      ml[i] = v[i][0];
      for (int j = 0; j<m; j++)
	ml[i] = max(ml[i], v[i][j]);
    }

    for (int i = 0; i<m; i++) {
      mc[i] = v[0][i];
      for (int j = 0; j<n; j++)
	mc[i] = max(mc[i], v[j][i]);
    }

    bool poss = true;
    for (int i = 0; i<n && poss; i++)
      for (int j = 0; j<m && poss; j++) {
	if (v[i][j] < ml[i] && v[i][j] < mc[j])
	  poss = false;
      }
    
    if (poss)
      printf("Case #%d: YES\n", t);
    else
      printf("Case #%d: NO\n", t);
    
  }
  return 0;
}
