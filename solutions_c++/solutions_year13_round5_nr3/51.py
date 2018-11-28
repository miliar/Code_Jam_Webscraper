// Authored by dolphinigle
// GCJ 2013 3

#include <vector>
#include <list>
#include <map>
#include <set>

#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <assert.h>

#define FORN(X,Y) for (int (X) = 0;(X) < (Y);++(X))
#define REP(X,Y,Z) for (int (X) = (Y);(X) < (Z);++(X))

#define RE(X,Y) for (int (X) = 0;(X) < (Y);++(X))
#define FOR(X,Y,Z) for (int (X) = (Y);(X) <= (Z);++(X))

#define SZ(Z) ((int)(Z).size())
#define ALL(W) (W).begin(), (W).end()
#define PB push_back

#define MP make_pair
#define A first
#define B second

#define INF 1023123123
#define EPS 1e-11

#define MX(Z,Y) Z = max((Z),(Y))
#define MN(X,Y) X = min((X),(Y))

#define FORIT(X,Y) for(typeof((Y).begin()) X = (Y).begin();X!=(Y).end();X++)

using namespace std;

typedef long long ll;
typedef double db;
typedef vector<int> vint;

int seq[3000];
int mfrom[3000];
int mto[3000];
ll mlb[3000];
ll mub[3000];
int setmin[3000];
int vis[3000];
ll mydist[3000];
int boleh[3000];

vint adj[3000];

ll Len(int x) {
  if (setmin[x]) {
    return mlb[x];
  } else {
    return mub[x];
  }
}

int n,m,p;

ll dijkdist[3000];
void Dijk() {
  FORN(i, n) dijkdist[i] = -1LL;
  dijkdist[0] = 0LL;
  set< pair<ll, int> > pq;
  pq.insert(MP(0LL, 0));
  while (!pq.empty()) {
    int a = pq.begin()->B;
    ll v = pq.begin()->A;
    pq.erase(pq.begin());
    if (dijkdist[a] != v) {
      continue;
    }
    FORIT(it, adj[a]) {
      int to = mto[*it];
      ll wei = Len(*it);
      if (dijkdist[to] == -1LL || dijkdist[to] > dijkdist[a] + wei) {
        dijkdist[to] = dijkdist[a] + wei;
        pq.insert(MP(dijkdist[to], to));
      }
    }
  }
  FORN(i, n) if (dijkdist[i] == -1LL) dijkdist[i] = INF;
}

int Test(int pathlen) {
  //cout << "testing " << pathlen << endl;
  FORN(i, 3000) setmin[i] = 0;
  FORN(i, 3000) vis[i] = 0;
  FORN(i, 3000) boleh[i] = 0;
  int cur = 0;
  vis[cur] = 1;
  mydist[cur] = 0LL;
  for (int i = 0; i < pathlen-1; ++i) {
    setmin[seq[i]] = 1;
    assert(mfrom[seq[i]] == cur);
    int prev = cur;
    cur = mto[seq[i]];
    if (vis[cur]) {
      //cout << "fail because of loop" << endl;
      return 0;
    }
    vis[cur] = 1;
    mydist[cur] = mydist[prev] + Len(seq[i]);
  }
  if (cur != 1 && vis[1]) {
    // ....
   // cout << "fail because of visited 1 before end" << endl;
    return 0;
  }
  boleh[cur] = 1;
  Dijk();
  FORN(i, n) if (vis[i]) {
    if (dijkdist[i] < mydist[i]) {
      //cout << i << ":" << dijkdist[i] << endl;
      //cout << "fail because shortest path failure" << endl;
      return 0;
    }
  }
  // ok i'm the sexiest now
  // ...i mean, shortest path
  // ...try to expand? please?
  //cout << cur << endl;
  while (true) {
    if (vis[1]) {
      return 1;
    }
    int found = 0;
    FORN(i, m) if (boleh[mfrom[i]] && !vis[mto[i]] && dijkdist[mto[i]] >= dijkdist[mfrom[i]] + mlb[i]) {
      // expand!
      int targ = mto[i];
      setmin[i] = 1;
      boleh[targ] = 1;
      vis[targ] = 1;
      Dijk();
      found = 1;
      break;
    }
    if (!found) {
      //cout << "fail because no node to expand" << endl;
      return 0;
    }
  }
}

int main() {
  int ntc;
  cin >> ntc;
  FORN(itc, ntc) {
    cout << "Case #" << (itc+1) << ": ";

    cin >> n >> m >> p;
    FORN(i, n) {
      adj[i].clear();
    }
    FORN(i, m) {
      int a, b, lo, hi;
      cin >> a >> b >> lo >> hi;
      --a;
      --b;
      adj[a].PB(i);
      mfrom[i] = a;
      mto[i] = b;
      mlb[i] = lo;
      mub[i] = hi;
    }
    FORN(i, p) {
      cin >> seq[i];
      --seq[i];
    }
    int best = 0;
    int lb = 1;
    int ub = p+1;
    while (lb <= ub) {
      int mid = (lb+ub)/2;
      if (Test(mid)) {
        best = mid;
        lb = mid+1;
      } else {
        ub = mid-1;
      }
    }
    //cout << best << endl;
    if (best == p+1) {
      cout << "Looks Good To Me" << endl;
    } else {
      cout << seq[best-1]+1 << endl;
    }
  }
}
