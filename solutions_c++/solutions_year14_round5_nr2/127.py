#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

const int MAXN = 105;

int p, q, n;
int h[MAXN], g[MAXN];

int dp[MAXN][MAXN*2][MAXN*10];

int f (int x, int dmg, int pt){
  if (x == n) return 0;
  if (dmg <= 0) return f(x+1, h[x+1], pt);
  int &ret = dp[x][dmg][pt];
  if (ret != -1) return ret;

  if (pt){
    int nxt = f(x, dmg - p, pt-1);
    if (p >= dmg) nxt += g[x];
    ret = max(ret, nxt);
  }

  ret = max(ret, f(x, dmg - q, pt+1));
  return ret;
}

void solve (){
  scanf("%d%d%d", &p, &q, &n);
  for (int i = 0; i < n; ++i)
    scanf("%d%d", &h[i], &g[i]);

  memset(dp, -1, sizeof dp);
  printf("%d\n", f(0, h[0], 1));
}

int main (void){
  int tc; scanf ("%d", &tc);
  for (int i = 1; i <= tc; ++i){
    printf("Case #%d: ", i);
    solve();
  }

  return 0;
}


