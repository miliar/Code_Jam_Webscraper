#include <cstring>
#include <iostream>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

#include <set>

using namespace std;

int p;
int q;
int n;
int hp[100];
int g[100];

int dp[128][1024];

int solve(int pos, int rest){
  if(pos == n) return 0;
  if(dp[pos][rest] != -1) return dp[pos][rest];
  int ret = 0;

  for(int i = 1; ; i++){
    const int h = max(0, hp[pos] - (i - 1) * p);
    const int cnt = (h - 1) / q;
    if(rest + cnt < i){
      if(i * p >= hp[pos]) break;
      continue;
    }
    if(cnt * q + i * p < hp[pos]) continue;

    ret = max(ret, g[pos] + solve(pos + 1, rest + cnt - i));
    if(i * p >= hp[pos]) break;
  }

  ret = max(ret, solve(pos + 1, rest + (hp[pos] + q - 1) / q));

  // printf("%d %d: %d\n", pos, rest, ret);
  return dp[pos][rest] = ret;
}

int process(){
  p = getInt();
  q = getInt();
  n = getInt();

  REP(i,n){
    hp[i] = getInt();
    g[i] = getInt();
  }

  memset(dp, -1, sizeof(dp));
  return solve(0, 1);
}

int main(){
  const int t = getInt();
  REP(i,t){
    printf("Case #%d: %d\n", i + 1, process());
  }
  return 0;
}
