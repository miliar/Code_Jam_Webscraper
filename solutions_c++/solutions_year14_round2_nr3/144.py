#include <algorithm>
#include <iostream>
#include <queue>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

#include <set>

using namespace std;

void solve(int cs){
  const int n = getInt();
  const int m = getInt();

  vector<vector<int> > g(n, vector<int>(n, 0));
  vector<string> zip(n);

  REP(i,n) cin >> zip[i];

  REP(i,m){
    const int a = getInt() - 1;
    const int b = getInt() - 1;
    g[a][b] = g[b][a] = 1;
  }

  string ans(5 * n, '9');

  vector<int> v(n);
  REP(i,n) v[i] = i;
  do{
    string ret = "";
    int p = 0;

    REP(i,n){
      ret += zip[v[i]];

      if(i != 0){
	for(int j = i - 1; j >= 0; j--){
	  if(p & (1 << j)){
	    if(g[v[i]][v[j]] == 0){
	      p ^= 1 << j;
	    }else{
	      break;
	    }
	  }
	}
	if(p == 0) goto next;
      }
      p |= 1 << i;
    }

    // cout << "ret: " << ret << endl;
    ans = min(ans, ret);

  next:;
  }while(next_permutation(v.begin(), v.end()));

  printf("Case #%d: ", cs); cout << ans << endl;
}

int main(){
  const int n = getInt();
  REP(i,n) solve(i + 1);
  return 0;
}
