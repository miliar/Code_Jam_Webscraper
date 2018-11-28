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

// Need an endl after output.
void solve() {
  int n, x;
  cin >> n >> x;
  multiset<int, greater<int> > ss;
  vector<int> s(n); REP(i, n) cin >> s[i], ss.insert(s[i]);
  SORT(s);
  int r = 0;
  REPD(i, n) {
    int curr = s[i];
    if (!CONTAINS(ss, curr)) continue;
    ss.erase(ss.find(curr));
    auto it = ss.lower_bound(x - curr);
    ++r;
    if (it != ss.end()) ss.erase(it);
  }
  cout << r << endl;
}

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("a.out1", "w", stdout);
  int tests;
  scanf("%d", &tests);
  REP(i, tests) {
    printf("Case #%d: ", int(i + 1));
    solve();
  }
  return 0;
}