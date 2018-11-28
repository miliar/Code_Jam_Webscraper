#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cassert>
using namespace std;
typedef long long ll;

#define REP(i,n) for(int i = 0; i < (int)(n); ++i)
#define FOR(i,k,n) for(int i = (k); i < (int)(n); ++i)
#define FOREQ(i,k,n) for(int i = (k); i <= (int)(n); ++i)
#define FORIT(i,c) for(__typeof((c).begin())i=(c).begin(); i!=(c).end(); ++i)
#define SZ(v) (int)((v).size())
#define MEMSET(v,h) memset((v),(h),sizeof(v))

bool pal(ll n) {
  auto s = to_string(n);
  REP(i, s.size() / 2) if(s[i] != s[s.size() - 1 - i]) return false;
  return true;
}

int main() {
  int T; cin >> T;
  for(int t = 1; t <= T; ++t) {
    ll a, b; cin >> a >> b;
    ll cnt = 0;
    for(ll x = ceil(sqrt(a)); x * x <= b; ++x) {
      if(pal(x) && pal(x * x)) ++cnt;
    }
    cout << "Case #" << t << ": ";
    cout << cnt << endl;
  }
}
