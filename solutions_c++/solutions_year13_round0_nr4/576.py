#include <map> 
#include <set> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cmath> 
#include <ctime> 
#include <float.h> 

using namespace std; 

#define REP(i, from, to) for (int i = (from); i < (to); ++i) 
#define FOR(i, n) REP(i, 0, (n)) 
#define ALL(x) x.begin(), x.end() 
#define SIZE(x) (int)x.size() 
#define PB push_back 
#define MP make_pair 

typedef long long i64; 
typedef vector<int> VI; 
typedef vector<VI> VVI; 
typedef vector<string> VS; 
typedef vector<VS> VVS; 
typedef pair<int, int> PII; 

struct State {
  int chestLockedMask;
  map<int, int> keys;
  VI path;
};

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int t;
  cin >> t;

  FOR (tt, t) {
    int k, n;
    cin >> k >> n;

    VI startKeys(k);
    FOR (i, k) cin >> startKeys[i];

    VI chestKey(n);
    VVI chest(n);
    FOR (i, n) {
      cin >> chestKey[i];

      int kk;
      cin >> kk;

      chest[i].resize(kk);
      FOR (j, kk) cin >> chest[i][j];
    }

    queue<State> q;
    
    State start;
    start.chestLockedMask = (1 << n) - 1;
    FOR (i, k)
      ++start.keys[startKeys[i]];

    set<pair<int, map<int, int> > > was;
    was.insert(make_pair(start.chestLockedMask, start.keys));

    q.push(start);
    VI res;

    while (!q.empty()) {
      State const& state = q.front();

      FOR (i, n) if (state.chestLockedMask & (1 << i)) {
        if (!state.keys.count(chestKey[i])) continue;

        State newState = state;
        newState.chestLockedMask &= ~(1 << i);
        newState.path.PB(i);
        if (!--newState.keys[chestKey[i]])
          newState.keys.erase(chestKey[i]);
        FOR (j, SIZE(chest[i]))
          ++newState.keys[chest[i][j]];

        if (newState.chestLockedMask == 0) {
          res = newState.path;
          break;
        }

        if (!was.count(make_pair(newState.chestLockedMask, newState.keys))) {
          was.insert(make_pair(newState.chestLockedMask, newState.keys));
          q.push(newState);
        }
      }

      if (!res.empty()) break;
      q.pop();
    }

    if (res.empty())
      cout << "Case #" << tt + 1 << ": " << "IMPOSSIBLE" << endl;
    else {
      cout << "Case #" << tt + 1 << ":" ;
      FOR (i, n) cout << " " << res[i] + 1;
      cout << endl;
    }
  }

  return 0;
}