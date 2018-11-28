#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>

using namespace std;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

const ll MOD = 1000002013;
ll T, N, M;
map<ll, ll> start, end;


int main() {
  cin >> T;
  FOR(cs, 1, T+1) {
    cin >> N >> M;
    start.clear();
    end.clear();
    set<ll> locs;
    ll cost = 0;
    FOR(i, 0, M) {
      ll o, e, p;
      cin >> o >> e >> p;
      ll diff = e - o;
      ll price = (N*(N+1))/2 - ((N-diff)*(N-diff+1))/2;
      price %= MOD;
      cost = (cost + p * price) % MOD;
      start[o] += p;
      end[e] += p;
      locs.insert(o);
      locs.insert(e);
    }
    map<ll, ll> cur;
    ll res = 0;
    FORIT(it, locs) {
      ll x = *it;
      if (start.find(x) != start.end()) {
        cur[x] += start[x];
      }
      if (end.find(x) != end.end()) {
        ll num = end[x];
        for (map<ll, ll>::reverse_iterator it2 = cur.rbegin(); it2 != cur.rend() && num > 0; it2++) {
          ll xx = it2->first, n = it2->second;
          ll diff = x - xx;
          ll price = (N*(N+1))/2 - ((N-diff)*(N-diff+1))/2;
          price %= MOD;
          ll nn = min(num, n);
          res = (res + (nn % MOD) * price) % MOD;
          num -= nn;
          it2->second -= nn;
        }
      }
    }
    cout << "Case #" << cs << ": " << ((cost - res) % MOD + MOD) % MOD << endl;
  }
	return 0;
}
