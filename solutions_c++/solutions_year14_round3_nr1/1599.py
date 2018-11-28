#include <iostream>
#include <algorithm>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <math.h>
#include <time.h>
#include <set>
#include <utility>
#include <map>
#include <stdio.h>
#include <assert.h>
#include <limits.h>

using namespace std;
typedef vector<unsigned long long int> VU;
VU two(1, 1);

int main () {
    freopen("A-large.in","r",stdin);
    freopen("outputAlarge.txt", "w", stdout);
  while (two.size() <= 40)
    two.push_back(2 * (*(two.rbegin())));
  unsigned long long int T; cin >> T;
  for (unsigned long long int t(1); t <= T; ++t) {
    unsigned long long int P, Q; {char c; cin >> P >> c >> Q;}
    unsigned long long int twos(0);
    while (Q % 2 <= 0) {Q /= 2; ++twos;}
    if (P % Q > 0)
      cout << "Case #" << t << ": impossible" << endl;
    else {
      P /= Q; Q = two[twos];
      unsigned long long int i1; for (i1 = 0; 2 * two[i1] <= P; ++i1);

      cout << "Case #" << t << ": " << (twos - i1) << endl;
    }
  }

  return 0;
}
