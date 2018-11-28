#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<string>
#include<set>
#include<queue>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;

#define pb push_back
#define mp make_pair
#define x first
#define y second
#define FOR(it,c) for(typeof(c) it = ((c).begin()); it != ((c).end()) ; ++it)
#define LL long long
LL rd[20];
LL nu[20];
LL E, n, R;
LL ans;

int dfs(int nowE, int dep, LL tt){
  tt -= nowE;
  if(tt<0)return 0;

  rd[dep] = nowE;

  if(dep==n){
    LL total = 0;
    for(int i=0;i<n;i++){
      total += (rd[i]*nu[i]);
    }
    ans = max(ans, total);
    return 0;
  }
  tt += R;
  tt = min(tt,E);
  for(int i=0;i<=tt;i++)
    dfs(i,dep+1, tt);
  return 0;
}

int main()
{
  int tn;
  int z;
  cin >> tn;
  for(z=1;z<=tn;z++){
    cin >> E >> R >> n;
    for(int i=0;i<n;i++)
      cin >> nu[i];
    ans = 0;
    for(int i=0;i<=E;i++)
      dfs(i,0,E);
    cout << "Case #" << z << ": " << ans << endl;
  }
  return 0;
}
