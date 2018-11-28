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
#define typeof __typeof__
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

void runcase() {
  int N;
  set<double> naomi;
  set<double> ken;
  set<double> ken2;
  cin >> N;
  FI(N) { double t; cin >> t; naomi.insert(t); }
  FI(N) { double t; cin >> t; ken.insert(t); ken2.insert(t); }

  // war strategy is for Naomi to play the smallest she has
  // then Ken plays the smallest he has to beat that, otherwise his smallest
  int nwarpt = 0;
  FE(it, naomi) {
    set<double>::iterator kit = ken.lower_bound(*it);
    if (kit != ken.end()) {
      ken.erase(kit);
    } else {
      nwarpt++;
      ken.erase(ken.begin());
    }
  }

  // deceitful war, hmm
  // naomi can play her smallest to force ken to discard his largest
  int ndwarpt = 0;
  while (naomi.size() > 0) {
    // naomi decides whether she can win
    // if so, win by playing the smallest block she can use
    set<double>::iterator kit2 = ken2.end(); --kit2;
    set<double>::iterator it2 = naomi.end(); --it2;
    if (*it2 > *kit2) {
      //naomi.erase(naomi.lower_bound(*kit2));
      naomi.erase(naomi.lower_bound(*ken2.begin()));
      ken2.erase(ken2.begin());
      ndwarpt++;
    } else {
      // if she decides she can't win
      // play her smallest and lie to force ken to bleed his largest
      ken2.erase(kit2);
      naomi.erase(naomi.begin());
    }
  }

  cout << ndwarpt << " " << nwarpt << endl;
}

int main() {
  cout << setprecision(9);
/* *** codejam style *** */
  int case_count;
  cin >> case_count;
  for (int i = 0; i < case_count; i++) {
    cout << "Case #" << i+1 << ": ";
    runcase();
  }
/* *** because I'm awesome *** */
  return 0;
}

