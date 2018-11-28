#include <cassert>
typedef long long ll;

#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }
inline ll getLL(){ ll s; scanf("%lld", &s); return s; }

#include <set>
using namespace std;

ll dfs1(ll cnt, int n, int round = 1){
  if(cnt == 0) return 0;
  return (1ll << (n - round)) + dfs1((cnt - 1) / 2, n, round + 1);
}

ll solve1(int n, ll p){
  ll low  = 0;
  ll high = (1ll << n) - 1;

  while(low <= high){
    const ll mid = (low + high) / 2;
    //printf("%lld (%lld %lld): %lld\n", mid, low, high, dfs1(mid, n));
    if(dfs1(mid, n) < p)
      low = mid + 1;
    else
      high = mid - 1;
  }
  return high;
}

ll dfs2(ll cnt, int n, int round = 1){
  //printf(" %lld %d %d (%lld)\n", cnt, n, round, 1ll << (n - round + 1));
  if(cnt == 0) return (1ll << (n - round + 1)) - 1;
  return dfs2((cnt - 1) / 2, n, round + 1);
}

ll solve2(int n, ll p){
  ll low  = 0;
  ll high = (1ll << n) - 1;

  while(low <= high){
    const ll mid = (low + high) / 2;
    // printf("2: %lld (%lld %lld): %lld\n", mid, low, high, dfs2(mid, n));
    const ll tmp = (1ll << n) - mid - 1;
    if(dfs2(tmp, n) < p)
      low = mid + 1;
    else
      high = mid - 1;
  }
  return high;
}

int main(){
  const int T = getInt();
  REP(cc, T){
    const int n = getInt();
    const ll m = getLL();
    printf("Case #%d: %lld %lld\n", cc + 1, solve1(n, m), solve2(n, m));
  }
  return 0;
}
