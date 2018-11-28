#define dbg if(0)
#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<algorithm>
#include<bitset>
using namespace std;
typedef vector<int> VI;
typedef map<int,int> MII;
#define FOR(i,n) for(int i=0;i<(n);++i)
#define FOREACH(it, c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define ALL(c) (c).begin(),(c).end()

inline bool get(int m, int i) {
  return (m & (1<<i));
}
inline int set(int m, int i) {
  return (m | (1<<i));
}

MII add(const MII &a, const MII &b) {
  MII res = a;
  FOREACH(it, b) {
    res[it->first] += it->second;
  }
  return res;
}

inline int diff(int m1, int m2) {
  FOR(i,32) if (get(m1, i) != get(m2, i)) return i;
  return 32;
}

inline bool contains(MII &m, int k) {
  return m[k] > 0;
}

inline bool containsp(const MII &m, int k) {
  return m.find(k) != m.end();
}

struct dfs {
  int n;
  MII prev;
  map<int, MII> keys;
  VI opening;
  vector<MII> enclosed;
  dfs(int _n, const MII &starting_keys, const VI &_opening, const vector<MII> &_enclosed): 
    n(_n), prev(), keys(), opening(_opening), enclosed(_enclosed) {
    keys[0] = starting_keys;
    prev[0] = 0;
  }
  bool run(int end) {
    try {
      rund(end);
    } catch(int) {}
    return containsp(prev, end);
  }
  void rund(int end, int state=0) {
    MII &skeys = keys[state];
    dbg {
      bitset<3> binary(state);
      cout << "rund(" << binary << ") keys: ";
      FOREACH(it, skeys) {
        cout << it->first << ":" << it->second << " ";
      }
      cout << endl;
    }
    if (state == end) throw 7;
    FOR(i,n) {
      if (not get(state, i) and contains(skeys, opening[i])) {
        int new_state = set(state, i);
        if (not containsp(prev, new_state)) {
          prev[new_state] = state;
          keys[new_state] = add(skeys, enclosed[i]);
          keys[new_state][opening[i]]--;
          rund(end, new_state);
        }
      }
    }
  }
};

VI solve() {
  int k, n;
  cin >> k >> n;
  MII keys;
  FOR(i,k) {
    int key;
    cin >> key;
    keys[key]++;
  }
  VI opening;
  vector<MII> enclosed;
  FOR(i,n) {
    int oi, ki;
    cin >> oi >> ki;
    opening.push_back(oi);
    MII enc;
    FOR(j,ki) {
      int kk;
      cin >> kk;
      enc[kk]++;
    }
    enclosed.push_back(enc);
  }

  dfs d(n, keys, opening, enclosed);

  int end = (1<<n)-1;
  VI res;
  if (not d.run(end)) return res;
  int state = end;
  while (state != 0) {
    res.push_back(1+diff(d.prev[state], state));
    state = d.prev[state];
  }
  reverse(ALL(res));
  return res;
}

int main() {
  int t;
  cin >> t;
  FOR(i,t) {
    VI solution = solve();
    cout << "Case #" << i+1 << ":";
    if (solution.empty()) {
      cout << " IMPOSSIBLE";
    } else {
      FOREACH(it, solution) {
        cout << " " << *it;
      }
    }
    cout << endl;
  }
  return 0;
}
