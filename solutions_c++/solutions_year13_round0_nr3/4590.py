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

bool ispal(int num) {
  char temp[20];
  snprintf(temp, 20, "%d", num);
  int fst = 0;
  int lst = strlen(temp)-1;
  while (fst < lst) {
    if (temp[fst] != temp[lst]) return false;
    fst++;
    lst--;
  }
  return true;
}

void runcase() {
  int A, B;
  cin >> A >> B;
  int cnt = 0;
  FJ(A, B+1) {
    double a = sqrt(j);
    // not a perfect square
    if (a != floor(a)) continue;
    // is palindrome
    if (ispal(j) && ispal((int)a)) cnt++;
  }
  cout << cnt;
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

