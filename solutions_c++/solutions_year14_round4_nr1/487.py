#include <cassert>
#include <complex>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iostream>
#include <iterator>
#include <limits>
#include <numeric>
#include <sstream>
#include <utility>

#include <algorithm>
#include <bitset>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

#include <memory.h>
using namespace std;

#define Pi 3.141592653589793
#define all(c) (c).begin(), (c).end()
typedef long long ll;

int main() {
#ifdef LOCAL_HOST
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif

  int TT; cin >> TT;
  for (int tt = 1; tt <= TT; ++tt) {
    int n; cin >> n;
    int x; cin >> x;
    vector<int> vi(n);
    for (int i = 0; i < n; ++i) {
      cin >> vi[i];
    }

    multiset<int, greater<int> > si(all(vi));
    int res = 0;
    while (!si.empty()) {
      set<int, greater<int> >::iterator it = si.begin();
      int left = x - *it;
      si.erase(it);
      it = si.lower_bound(left);
      if (it != si.end()) {
        si.erase(it);
      }
      ++res;
    }

    printf("Case #%d: %d\n", tt, res);
  }

  return 0;
}
