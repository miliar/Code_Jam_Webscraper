#include <algorithm>
#include <queue>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <set>
#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

using namespace std;

int solve1(const int n, const vector<int> &v){
  int ans = 0;
  REP(i,n-1) ans += max(0, v[i] - v[i + 1]);
  return ans;
}

int solve2(const int n, const vector<int> &v){
  int rate = 0;

  REP(i,n-1) if(v[i] != v[i + 1]) rate = 1;
  if(rate == 0) return rate;

  REP(i,n-1) rate = max(rate, v[i] - v[i + 1]);

  int ans = 0;
  REP(i,n-1){
    ans += max(0, min(rate, v[i]));
  }

  return ans;
}

int main(){
  const int T = getInt();

  REP(t,T){
    const int n = getInt();
    vector<int> v(n);
    REP(i,n) v[i] = getInt();
    printf("case #%d: %d %d\n", t + 1, solve1(n, v), solve2(n, v));
  }

  return 0;
}










