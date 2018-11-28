// Authored by dolphinigle
// GCJ 2013 2

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

ll modu = 1000002013LL;
ll n, m;

ll Cost(ll beg, ll en) {
  ll dist = en - beg;
  ll delt = (dist * (dist-1LL)) / 2LL;
  delt %= modu;
  ll mul = n * dist;
  mul %= modu;
  mul -= delt;
  mul %= modu;
  mul += modu;
  mul %= modu;
  return mul;
}

int main() {
  int ntc;
  cin >> ntc;
  
  FORN(itc, ntc) {
    cout << "Case #" << (itc+1) << ": ";
    cin >> n >> m;
    map< ll, ll > enter;
    map< ll, ll > exit;
    ll totcost = 0LL;
    ll actual = 0LL;
    vector<ll> important;
    FORN(i, m) {
      ll a, b, c;
      cin >> a >> b >> c;
      enter[a] += c;
      exit[b] += c;
      important.PB(a);
      important.PB(b);
      actual += (Cost(a, b) * c) % modu;
      actual %= modu;
    }
    sort(ALL(important));
    important.erase(unique(ALL(important)), important.end());
    set< pair<ll, ll> > passengers;
    FORIT(it, important) {
      // put the entering ones
      passengers.insert(MP(-*it, enter[*it]));
      // extract the exiting ones
      ll exits = exit[*it];
      while (exits) {
        pair<ll, ll> itu = *(passengers.begin());
        passengers.erase(passengers.begin());
        ll doexit = min(exits, itu.B);
        itu.B -= doexit;
        if (itu.B) passengers.insert(itu);
        exits -= doexit;

        // calculate
        ll orig = -itu.A;
        ll en = *it;
        totcost += (Cost(orig, en) * doexit) % modu;
        totcost %= modu;
      }
    }
    actual -= totcost;
    actual %= modu;
    actual += modu;
    actual %= modu;
    cout << actual << endl;
  }
  return 0;
}
