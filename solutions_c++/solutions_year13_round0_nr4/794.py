#include <iostream>
#include <iomanip>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <cstdlib>
#include <sstream>
#include <queue>
#include <cassert>
#include <bitset>
#include <climits>
#include <cfloat>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<ll> vll;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define FF first
#define SS second

#define FOR(v, s, e) for (int v = s; v < e; v++)
#define FE(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); ++i)
#define FI(c) for (ll i = 0; i < c; ++i)
#define FJ(s,c) for (ll j = s; j < c; ++j)
#define FK(s,c) for (ll k = s; k < c; ++k)
#define MP(X,Y) make_pair(X,Y)
// end boilerplate code...

int K, N;
vector<pair<int, multiset<int> > > chests;
set<int> did_open;

vector<int> done;

/* opened is DP state, each opened bitmask has a unique set of keys */
int search(int opened, multiset<int> keys) {
  if (opened == (1<<N)-1) return 1;
  
  pair<set<int>::iterator, bool> ret = did_open.insert(opened);
  if (ret.second == false) return 0;
  #ifdef DEBUG
    cout << "opened " << opened << endl;
  #endif

  /* for each chest */
  FI(N) {
    if (opened & (1<<i)) continue;
    multiset<int> keys2 = keys;
    multiset<int>::iterator it = keys2.find(chests[i].first);
    if (it == keys2.end()) continue;
    keys2.erase(it);
    FE(it2, chests[i].second) {
      keys2.insert(*it2);
    }
    if (search(opened | (1<<i), keys2) == 1) {
      done.push_back(i);
      return 1;
    }
  }
  return 0;
}

void runcase() {
  cin >> K >> N;
  chests.clear();
  done.clear();
  did_open.clear();

  multiset<int> start_keys;
  FI(K) {
    int sk;
    cin >> sk;
    start_keys.insert(sk);
  }

  FI(N) {
    int Ti, Ki;
    cin >> Ti >> Ki;
    multiset<int> keys;
    FJ(0, Ki) {
      int key;
      cin >> key;
      keys.insert(key);
    }
    chests.push_back(MP(Ti, keys));
  }

  if(search(0, start_keys)) {
    cout << (done[N-1]+1);
    FJ(1, N) {
      cout << " " << (done[N-1-j]+1);
    }
  } else {
    cout << "IMPOSSIBLE";
  }
}

int main() {
  cout << setprecision(9);
/* *** codejam style *** */
  int case_count;
  cin >> case_count;
  for (int i = 0; i < case_count; i++) {
    cout << "Case #" << (i+1) << ": ";
    runcase();
    cout << endl;
  }
/* *** because I'm awesome *** */
  return 0;
}

