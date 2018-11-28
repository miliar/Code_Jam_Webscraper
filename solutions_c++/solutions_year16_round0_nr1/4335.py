/**
 * Tags: set
 */
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <math.h>
#include <set>
#include <vector>
#include <string>
#include <iterator>
#include <algorithm>
#include <assert.h>
#include <map>

#include <sstream>

#include <stdexcept>

using namespace std;

typedef vector<string> vs;
typedef long long ll;
typedef long long int lli;
typedef vector<int> vi;
typedef vector<ll> vll;

int main(int argc, const char **argv) {
  int cases;
  string tmp;
  ll total, N, k;
  ll i;
  cin >> cases;
  set <int> s;

  for (int caseI = 1; caseI <= cases; caseI++) {
    cin >> N;
    if (N == 0) {
      cout << "Case #" << caseI << ": INSOMNIA" << endl;
      continue;
    }

    for (i=1; i<1000000; i++) {
      k = i * N;
      while (k>=1) {
        s.insert(k%10);
        k = k/10;
        if (s.size() == 10) { break; }
      }
      if (s.size() == 10) { break; }
    }

    if (s.size() == 10) {
     cout << "Case #" << caseI << ": " << i*N << endl;
    } else {
      cout << "Case #" << caseI << ": INSOMNIA" << endl;
    }
    s.clear();
  }

  return 0;
}
