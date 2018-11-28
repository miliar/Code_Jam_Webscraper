#include <algorithm>
#include <map>
#include <queue>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

#include <set>

using namespace std;

int main(){
  const int T = getInt();
  REP(t,T){
    const int n = getInt();
    map<int, int> m;
    REP(i,n*(2*n-1)) m[getInt()]++;
    vector<int> ans;
    for(const auto &p : m) {
      if(p.second % 2 == 1) ans.push_back(p.first);
    }
    sort(ans.begin(), ans.end());
    printf("Case #%d:", t + 1);
    for(int i : ans) printf(" %d", i);
    puts("");
  }
  return 0;
}
