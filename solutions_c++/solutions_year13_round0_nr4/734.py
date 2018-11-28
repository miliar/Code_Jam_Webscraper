#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
using namespace std;

#define pb push_back
typedef vector<int> vi;
const int N = 21;

struct node {
  int t;
  vi k;
}r[N];

int n, k;
map<int, int> dp[1 << N];
int pre[1 << N];

void init() {
  for (int i = 0; i < (1 << N); i++) dp[i].clear(), pre[i] = -1;
  cin>>k>>n;
  for (int i = 0; i < k; i++) {
    int x;
    cin>>x;
    dp[0][x]++;
  }
  for (int i = 0; i < n; i++) {
    int t, kk;
    cin>>t>>kk;
    r[i].t = t;
    r[i].k = vi();
    for (int j = 0; j < kk; j++) {
      int x;
      cin>>x;
      r[i].k.pb(x);
    }
  }
}

vi getans(int p) {
  vi ret;
  while (1) {
    if (!p) return ret;
    int nxt = pre[p];
    
    for (int i = 0; i < n; i++) {
      int x = p & (1 << i);
      int y = nxt & (1 << i);
      if (x != y) {
        ret.pb(i + 1);
        break;
      }
    }
    
    p = nxt;
  }
}

vi solve() {
  queue<int> que;
  que.push(0);
  while(!que.empty()) {
    int now = que.front();
    //printf("%d\n", now);
    que.pop();
    for (int i = 0; i < n; i++) {
      if (now & (1 << i)) continue;
      if (!dp[now][r[i].t]) continue;
      int nxt = now | (1 << i);
      if (dp[nxt].size()) continue;
      map<int, int> tmp = dp[now];
      tmp[r[i].t]--;
      for (int j = 0; j < r[i].k.size(); j++) {
        tmp[r[i].k[j]]++;
      }
      dp[nxt] = tmp;
      pre[nxt] = now;
      que.push(nxt);
      if (nxt == ((1 << n) - 1)) {
        return getans(nxt);
      }
    }
  }
  return vi();
}

int main() {
  freopen("d.in", "r", stdin);
  //freopen("d.out", "w", stdout);
  int T;
  cin>>T;
  for (int i = 1; i <= T; i++) {
    init();
    vi r = solve();
    printf("Case #%d:", i);
    if (!r.size()) printf(" IMPOSSIBLE\n");
    else {
      for (int j = r.size() - 1; j >= 0; j--) {
        printf(" %d", r[j]);
      }
      printf("\n");
    }
  }
}