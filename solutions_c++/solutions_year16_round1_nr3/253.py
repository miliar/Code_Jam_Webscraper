#include <iostream>
#include <algorithm>
#include <queue>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

#include <set>

using namespace std;

int bff[1000];
int use[1000];
vector<int> ibff[1000];

int dfs(int i, int start, int prev = -1) {
  use[i] = 1;
  int ans = 1;
  const int next = bff[i];
  if(use[next]) {
    if(next == start || next == prev) {
      ans = 1;
    } else {
      ans = -10000;
    }
  } else {
    ans = 1 + dfs(next, start, i);
  }
  use[i] = 0;
  return ans;
}

int dfs2(int i, int prev) {
  use[i] = 1;
  int ans = 1;
  for(int next : ibff[i]) {
    if(!use[next] && next != prev)
      ans = max(ans, 1 + dfs2(next, i));
  }
  use[i] = 0;
  return ans;
}

int main(){
  const int T = getInt();
  REP(t,T){
    const int n = getInt();
    REP(i,n) bff[i] = getInt() - 1;
    REP(i,n) ibff[i].clear();
    REP(i,n) ibff[bff[i]].push_back(i);

    int pairwise = 0;
    REP(i,n) if(bff[bff[i]] == i)
      pairwise++;

    int ans = pairwise;
    REP(i,n) ans = max(ans, dfs(i, i));

    int tmp = 0;
    REP(i,n) if(bff[bff[i]] == i && i < bff[i]) {
      const int a = dfs2(i, bff[i]);
      const int b = dfs2(bff[i], i);
      tmp += a + b;
    }

    ans = max(ans, tmp);
    printf("Case #%d: %d\n", t + 1, ans);
  }
  return 0;
}
