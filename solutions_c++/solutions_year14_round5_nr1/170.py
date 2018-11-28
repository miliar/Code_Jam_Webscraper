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

ll T, N, P, Q, R, S;
vector<ll> sums;

ll getsum(ll a, ll b) {
  a = min(a, N);
  b = max(b, (ll)1);
  if (a > b) return 0;
  return sums[b] - sums[a-1];
}

int main() {
  cin >> T;
  FOR(cs, 1, T+1) {
    cin >> N >> P >> Q >> R >> S;
    sums.clear();
    sums.push_back(0);
    FOR(i, 0, N) {
      ll v = ((i * P) + Q) % R + S;
      sums.push_back(sums[i] + v);
    }
    ll res = sums[N];
    int pos = 1;
    FOR(i, 1, N+1) {
      while (pos < i) pos++;
      while (pos < N && getsum(i, pos+1) <= getsum(pos+2, N)) pos++;
      ll v1 = max(max(getsum(1, i-1), getsum(i, pos)), getsum(pos+1, N));
      ll v2 = max(max(getsum(1, i-1), getsum(i, pos+1)), getsum(pos+2, N));
      res = min(res, v1);
      res = min(res, v2);
    }
    printf("Case #%d: %.10lf\n", cs, double(sums[N] - res) / sums[N]);
  }
	return 0;
}
