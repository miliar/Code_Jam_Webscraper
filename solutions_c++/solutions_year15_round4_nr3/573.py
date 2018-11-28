#include <algorithm>
#include <map>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <queue>
#include <set>
#include <unordered_set>
#include <sstream>

using namespace std;

vector<string> getStrs(){
  string line;
  getline(cin, line);
  stringstream ss(line);
  string s;
  vector<string> ret;
  while(ss >> s) ret.push_back(s);
  return ret;
}

int getI(){
  return atoi(getStrs()[0].c_str());
}

int main(){
  const int T = getI();

  REP(t,T){
    const int n = getI();
    vector<vector<string> > ss(n);
    REP(i,n) ss[i] = getStrs();

    int next = 0;
    map<string, int> ids;
    vector<vector<int> > si(n);
    REP(i,n) REP(j,ss[i].size()){
      const string &s = ss[i][j];
      if(ids.count(s) == 0) ids[s] = next++;
      si[i].push_back(ids[s]);
    }

    const int m = ids.size();

    vector<int> em(m);
    vector<int> fm(m);
    REP(i,si[0].size()) em[si[0][i]] = 1;
    REP(i,si[1].size()) fm[si[1][i]] = 1;

    int ans = 100000000;
    REP(k,1<<(n - 2)){
      vector<int> e = em;
      vector<int> f = fm;

      REP(i,n - 2){
	vector<int> &p = (k & (1 << i)) == 0 ? e : f;
	for(int j : si[i + 2]) p[j] = 1;
      }

      int cnt = 0;
      REP(i,m) cnt += e[i] & f[i];
      ans = min(ans, cnt);
    }
    // printf("n=%d\n", n);
    printf("Case #%d: %d\n", t + 1, ans);
  }

  return 0;
}
