#include <iostream>
#include <fstream>
#include <sstream>

#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
#include <vector>
#include <algorithm>
#include <bitset>

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

#define forn(i, n) for(int i = 0; i< int(n); i++)
#define ford(i, n) for(int i = int(n) - 1; i >= 0; i--)
#define foreach(it, a) for(__typeof((a).begin()) it = a.begin(); it != a.end(); it++)

template<typename X> X abs(X a) { if (a < 0) return -a; return a; }
template<typename X> X sqr(X a) { return a * a; }
template<typename X> bool hasbit(X mask, int pos) { return (mask >> pos) & 1; }

#define sz(a) int((a).size())
#define all(a) (a).begin(),(a).end()
#define mp make_pair
#define pb push_back
#define ft first
#define sc second

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = 1000000000;
const ld EPS = 1e-9;
const ld PI = ld(3.1415926535897932384626433832795);

using namespace std;

int is_e[2000];
int is_f[2000];
string s[200];
int n;
inline bool read(){
  if (scanf("%d\n", &n) != 1)
    return false;
  forn(i, n) {
    getline(cin, s[i]);
  }
  return true;
}

inline void solve() {
  vector < vector < int > > ids(n, vector < int > (0, 0));
  map<string, int> to_id;
  int cntid = 0;
  memset(is_f, 0, sizeof is_f);
  memset(is_e, 0, sizeof is_e);
  forn(i, n) {
    stringstream ss;
    ss << s[i];
    string word;
    while (ss >> word) {
      if (!to_id.count(word)) {
        to_id[word] = cntid;
        cntid++;
      }
      ids[i].pb(to_id[word]);
      if (i == 0) is_f[to_id[word]] = 1;
      if (i == 1) is_e[to_id[word]] = 1;
    }
  }
  int ans = INF;
  forn(mask, (1 << (n - 2))) {
    forn(i, n - 2) {
      int eng = (hasbit(mask, i) > 0);
      forn(j, sz(ids[i + 2])) {
        is_e[ids[i + 2][j]] += (eng == 1);
        is_f[ids[i + 2][j]] += (eng == 0);
      }
    }
    int tans = 0;
    forn(i, cntid) {
      if (is_e[i] > 0 && is_f[i] > 0) {
        tans++;
      }
    }
    forn(i, n - 2) {
      int eng = (hasbit(mask, i) > 0);
      forn(j, sz(ids[i + 2])) {
        is_e[ids[i + 2][j]] -= (eng == 1);
        is_f[ids[i + 2][j]] -= (eng == 0);
      }
    }
    ans = min(ans, tans);
  }
  cout << ans << endl;
}

int main() {
#ifdef gridnevvvit
  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);
#endif
  int testcount;
  scanf("%d\n", &testcount);
  forn(test, testcount) {
    assert(read());
    cout << "Case #" << test + 1 << ": ";
    solve();
    cerr << "solved testcase " << test + 1 << endl;
  }
}
