/*************************************************************************
    > File Name: c.cpp
    > Author: implus
    > Mail: 674592809@qq.com
    > Created Time: 日  5/11 19:04:15 2014
 ************************************************************************/

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<string>
#include<set>
#include<queue>
#include<stack>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define ls (rt<<1)
#define rs (rt<<1|1)
#define lson l,m,ls
#define rson m+1,r,rs

int mp[22][22];
int go[22][22];
int n, m, T, k;


int dir[4][2] = {-1, 0, 0, 1, 1, 0, 0, -1};
bool in(int x, int y){
  return 0 <= x && x < n && 0 <= y && y < m;
}

void dfs(int x, int y){
  go[x][y] = 1;
  for(int i = 0; i < 4; i++){
    int nx = x + dir[i][0], ny = y + dir[i][1];
    if(!in(nx, ny)) continue;
    if(go[nx][ny] == 0 && mp[nx][ny] != 1)
      dfs(nx, ny);
  }
}

int ok(int n, int m){
  memset(go, 0, sizeof(go));
  for(int i = 0; i < n; i++) {
    if(go[i][m - 1] == 0 && mp[i][m - 1] != 1){
      dfs(i, m - 1);
    }
    if(go[i][0] == 0 && mp[i][0] != 1){
      dfs(i, 0);
    }
  }
  for(int j = 0; j < m; j++){
    if(go[0][j] == 0 && mp[0][j] != 1){
      dfs(0, j);
    }
    if(go[n - 1][j] == 0 && mp[n - 1][j] != 1){
      dfs(n - 1, j);
    }
  }
  int ans = 0;
  for(int i = 0; i < n; i++)
    for(int j = 0; j < m; j++) ans += go[i][j];
  return n * m - ans;
}

int main(){
  scanf("%d", &T);
  int icase = 1;
  while(T--){
    scanf("%d%d%d", &n, &m, &k);
    int S = n * m;
    int ans = k;
    for(int s = 0; s < (1<<S); s++){
      memset(mp, 0, sizeof(mp));
      int cnt = 0;
      for(int i = 0; i < S; i++) if(s & (1<<i)){
        mp[i / m][i % m] = 1;
        cnt++;
      }
      if(ok(n, m) == k){
        ans = min(ans, cnt);
      }
    }
    printf("Case #%d: %d\n",icase++, ans);
  }
  return 0;
}
