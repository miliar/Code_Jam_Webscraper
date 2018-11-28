#include <algorithm>
#include <array>
#include <bitset>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <forward_list>
#include <functional>
#include <initializer_list>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <regex>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <valarray>
#include <vector>
using namespace std;

#define FORI(i,n) for(int i=0; i<(int)(n); ++i)
#define FORIB(i,b,n) for(int i=(int)(b); i<(int)(n); ++i)
#define FORIR(i,n) for(int i=(int)((n)-1); i>=0; --i)
#define FORIBR(i,b,n) for(int i=(int)((n)-1); i>=(int)(b); --i)
#define MP(a,b) make_pair(a,b)
#define MT(a...) make_tuple(a)
#define ALL(L) (L).begin(),(L).end()
#define ALLR(L) (L).rbegin(),(L).rend()
#define SZ(L) (L).size()
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define SORTED_PAIR(a,b) MIN(a,b),MAX(a,b)
#define INF (1<<29)
#define EPS (1e-9)

typedef unsigned int uint;
typedef unsigned long long ull;
typedef signed long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef pair<int,int> pii;
typedef vector<pii> vii;

pii cost(int H, int P, int Q) {
  pii r;
  r.first = (H + Q - 1) / Q;
  if(H % Q == 0) {
    r.second = r.first - 1 - ((Q + P - 1) / P);
  } else {
    r.second = r.first - 1 - (((H % Q) + P - 1) / P);
  }
  return r;
}

ll calc(int i, int s, vii& H, int P, int Q, map<pii, ll>& cache) {
  if(i >= (int)H.size()) return 0;
  if(cache.count(MP(i, s))) return cache[MP(i, s)];
  pii ct = cost(H[i].first, P, Q);
  ll v1 = calc(i + 1, s + ct.first, H, P, Q, cache);
  if(s + ct.second >= 0) {
    ll v2 = H[i].second + calc(i + 1, s + ct.second, H, P, Q, cache);
    return max(v1, v2);
  }
  return v1;
}

void solve(int T) {
  int P, Q, N;
  cin >> P >> Q >> N;
  vii H(N);
  FORI(i, N) cin >> H[i].first >> H[i].second;
  map<pii, ll> cache;
  ll res = calc(0, 1, H, P, Q, cache);
  printf("Case #%d: %lld\n", T, res);
}

int main() {
  int T;
  scanf("%d", &T);
  FORI(t, T) {
    solve(t + 1);
  }
}
