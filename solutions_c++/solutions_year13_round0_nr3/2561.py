#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <vector>
using namespace std;

#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
#define CLR(x,a) memset(x,a,sizeof(x))
#define setmin(a,b) a = min(a,b)
#define PB push_back
#define FORALL(i,v) for(typeof((v).end())i=(v).begin();i!=(v).end();++i)
#define MP make_pair
#define A first
#define B second
#define RF(i,a,b) for(int i=(a)-1;i>=(b);--i)
#define BEND(v) (v).begin(),(v).end()
#define SZ(v) int((v).size())
#define FORI(i,v) FOR(i,SZ(v))
typedef long double ld;
typedef long long ll;

ll rev(ll x) {
  ll y = 0;
  while (x) {
    y *= 10;
    y += x % 10;
    x /= 10;
  }
  return y;
}

bool ispal(ll x) {
  ll y = rev(x);
  return x == y;
}

vector<ll> fnsq;
void init() {
  assert(rev(1234) == 4321);

  for (ll x = 1; x <= 10 * 1000 * 1000LL; ++x) {
    if (ispal(x) && ispal(x*x)) fnsq.push_back(x*x);
  }

  assert(fnsq[0] == 1);
  assert(fnsq[1] == 4);
  assert(fnsq[2] == 9);
  assert(fnsq[3] != 16);
}

ll A,B;
void doit(int cas) {
  scanf(" %lld %lld", &A, &B);

  int ans = upper_bound(BEND(fnsq), B) - lower_bound(BEND(fnsq), A);
  printf("Case #%d: %d\n", cas+1, ans);
}

int T;
int main() {
  init();
  scanf(" %d", &T);
  FOR(cas,T) doit(cas);
  return 0;
}
