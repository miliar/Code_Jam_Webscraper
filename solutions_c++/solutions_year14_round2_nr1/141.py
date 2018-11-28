#include <algorithm>
#include <iostream>
#include <queue>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

#include <set>

using namespace std;

void solve(int cs){
  const int m = getInt();
  vector<string> v(m);
  vector<int> p(m);

  REP(i,m) cin >> v[i];

  printf("Case #%d: ", cs);

  int ans = 0;

  while(p[0] != (int)v[0].size()){
    vector<int> cnts(m);
    const char c = v[0][p[0]];

    REP(i,m){
      while(p[i] != (int)v[i].size() &&  v[i][p[i]] == c){
	p[i]++;
	cnts[i]++;
      }
    }

    const int mn = *min_element(cnts.begin(), cnts.end());
    if(mn == 0) goto fail;

    const int mx = *max_element(cnts.begin(), cnts.end());
    int cand = mx * m;
    REP(i,mx+1){
      int tmp = 0;
      REP(j,m) tmp += std::abs(cnts[j] - i);
      cand = min(cand, tmp);
    }

    ans += cand;
  }

  REP(i,m) if(p[i] != (int)v[i].size()) goto fail;

  printf("%d\n", ans);
  return;

 fail:;
  puts("Fegla Won");

}

int main(){
  const int n = getInt();
  REP(i,n) solve(i + 1);
  return 0;
}
