#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <utility>
#include <functional>
#include <bitset>
#include <deque>
#include <tuple>

using namespace std;

typedef long long ll;
typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef pair<int, int> pii;

#define FOR(i, x, y) for(ll i=x; i<=y; i++)
#define FORD(i, x, y) for (ll i = x; i >= y; --i)
#define REP(i, n) for(ll i=0; i<n; i++)
#define REPD(i, n) for(ll i = n - 1; i >= 0; --i) 

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define UNIQ(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define SZ(c) (int)(c).size()
#define CONTAINS(s,obj) (s.find(obj)!=s.end())

#define CLEAR(x) memset(x,0,sizeof x)
#define COPY(from,to) memcpy(to, from, sizeof to)

#define sq(x) ((x)*(x))
#define pb push_back
#define mp make_pair
#define X first
#define Y second

const double eps = 1.0e-11;
const double pi = acos(-1.0);

const int N = 1010;
int curr[N], need[N];
int n;

int Count() {
  int tmp[N];
  map<int, int> h;
  REP(i, n) h[need[i]] = i;
  REP(i, n) tmp[i] = h[curr[i]];
  int count = 0;
  REP(i, n) REP(j, i) if (tmp[i] < tmp[j]) ++count;
  return count;
}

bool Check() {
  int l = 0;
  while(l + 1 < n && need[l] < need[l + 1]) ++l;
  while(l + 1 < n && need[l] > need[l + 1]) ++l;
  return (l + 1 == n);
}


// Need an endl after output.
void solve_small() {
  cin >> n;
  REP(i, n) cin >> curr[i], need[i] = curr[i];
  sort(need, need + n);
  int best = n * n;
  do {
    if (Check()) best = min(best, Count());
  } while(next_permutation(need, need + n));
  cout << best << endl;
}

void solve() {
  cin >> n;
  REP(i, n) cin >> curr[i];

  int res = 0;
  REP(i, n) {
    int left = 0;
    int right = 0;
    REP(j, i) left += curr[j] > curr[i];
    FOR(j, i + 1, n - 1) right += curr[j] > curr[i];
    res += min(left, right);
  }
  cout << res << endl;
}

int main() {
  freopen("B-large.in", "r", stdin);
  freopen("b.out2", "w", stdout);
  int tests;
  scanf("%d", &tests);
  REP(i, tests) {
    cerr << i << endl;
    printf("Case #%d: ", int(i + 1));
    solve();
  }
  return 0;
}