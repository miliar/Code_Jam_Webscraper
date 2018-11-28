#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
using namespace std;

#define INF (1LL << 30)
typedef long long Int;
Int n, d, as, cs, rs, am, cm, rm;

Int ans[1000080];
Int s[1000080], m[1000080];
vector<Int> edge[1000080];

void dfs(Int x, Int mi = INF, Int ma = -INF){
  mi = min(mi, s[x]);
  ma = max(ma, s[x]);
  if(ma - mi > d)return;
  ans[max(ma - d, 0LL)]++;
  ans[mi + 1]--;
  for(Int i = 0;i < edge[x].size();i++){
    Int to = edge[x][i];
    dfs(to, mi, ma);
  }
}

void solve(){
  Int res = 0;
  cin >> n >> d;
  cin >> s[0] >> as >> cs >> rs;
  cin >> m[0] >> am >> cm >> rm;
  fill(ans, ans + 1000080, 0);
  for(Int i = 0;i <= n-1;i++)edge[i].clear();
  for(Int i = 1;i <= n-1;i++){
    s[i] = (s[i-1] * as + cs) % rs;
    m[i] = (m[i-1] * am + cm) % rm;
    edge[m[i]%i].push_back(i);
  }
  dfs(0);
  for(Int i = 0;i <= 1000000;i++){
    if(i)ans[i] += ans[i-1];
    res = max(res, ans[i]);
  }
  cout << res << endl;
  return;
}

int main(){
  Int T;
  cin >> T;
  for(Int t = 1;t <= T;t++){
    cout << "Case #" << t << ": ";
    solve();
  }
  return 0;
}
