#include <bits/stdc++.h>

using namespace std;
char ma[4][4];
int nma[4][4];
int n, vis[4], pos[4];
int dfs(int x){
  if (x == n){
    return 1;
  }
  int res = 1;
  int r = 0;
  for (int i = 0; i < n; ++ i){
    if (nma[pos[x]][i] && vis[i] == 0){
      r++;
      vis[i] = 1;
      //if (vis[0] == 1 && x == 1) printf("%d\n", dfs(x + 1));
      res &= dfs(x + 1);
      vis[i] = 0;
    }
  }

  if (r == 0) res = 0;
  return res;
}
int main(){
  freopen("out", "w", stdout);
  int t; scanf("%d", &t);
  while (t--){
    static int ca = 0;
    printf("Case #%d: ", ++ ca);
    scanf("%d", &n);
    for (int i = 0; i < n; ++ i){
        scanf("%s", ma[i]);
    }
    int ans = 20;
    for (int mask = 0; mask < (1 << (n * n)); ++ mask){
      int res = 0;
      for (int i = 0; i < n; ++ i){
        for (int j = 0; j < n; ++ j){
          nma[i][j] = (ma[i][j] == '1' ? 1 : 0);
          int x = i * n + j;
          if ((mask >> x) & 1){
             nma[i][j] = 1;
             res++;
           }
           //printf("%d ", nma[i][j]);
        }
      }
      //puts("");
      pos[0] = 0; pos[1] = 1;
      pos[2] = 2; pos[3] = 3;
      int r = 1;
      do{
        r &= dfs(0);
      }while (next_permutation(pos, pos + n));
      if (r == 1) ans = min(ans, res);
    //  break;
    }
    printf("%d\n", ans);
  }
}
