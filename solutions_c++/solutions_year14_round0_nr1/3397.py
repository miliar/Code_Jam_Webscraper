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
  int r1, r2;
  int l1[16], l2[16];
  cin >> r1; r1--;
  FI(16) cin >> l1[i];
  cin >> r2; r2--;
  FI(16) cin >> l2[i];

  set<int> poss1;
  set<int> poss2;
  FJ(r1*4, r1*4+4) poss1.insert(l1[j]);
  FJ(r2*4, r2*4+4) {
    if (poss1.find(l2[j]) != poss1.end()) {
      poss2.insert(l2[j]);
    }
  }
  if (poss2.size() == 1) {
    cout << *poss2.begin() << endl;
  } else if(poss2.size() == 0) {
    cout << "Volunteer cheated!" << endl;
  } else {
    cout << "Bad magician!" << endl;
  }

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

