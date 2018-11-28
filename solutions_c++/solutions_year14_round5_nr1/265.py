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

void solve(int T) {
  ll N, p, q, r, s;
  cin >> N >> p >> q >> r >> s;
  vector<ll> d(N, 0), sum(N, 0);
  FORI(i, N) {
    d[i] = ((i * p + q) % r + s);
  }

  sum[0] = d[0];
  FORIB(i, 1, N) {
    sum[i] = sum[i - 1] + d[i];
  }
  
  ll ax = sum[N - 1];

  ll best = numeric_limits<ll>::max();
  FORI(i, N) {
    ll x = sum[i];
    auto it = upper_bound(ALL(sum), (ax - x) / 2 + x); 
    auto j = it - sum.begin();
    if(j < N && j > i) {
      ll y1 = sum[j] - x;
      ll z1 = sum[N - 1] - x - y1;
      ll v1 = max(x, max(y1, z1)); 
      best = min(best, v1);

      ll y2 = sum[j - 1] - x;
      ll z2 = sum[N - 1] - x - y2;
      ll v2 = max(x, max(y2, z2));
      best = min(best, v2);
    } else {
      best = min(best, x);
    }
  }
  double res = (double)(sum[N - 1] - best)/(double)sum[N - 1];
  printf("Case #%d: %.10lf\n", T, res);
}

int main() {
  int T;
  scanf("%d", &T);
  FORI(t, T) {
    solve(t + 1);
  }
}
