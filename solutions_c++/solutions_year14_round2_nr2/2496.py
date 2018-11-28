//Santiago Vanegas Gil.
#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

#define D(x) cout << #x " is " << x << endl

using namespace std;

template <class T> string toStr(const T &x)
{ stringstream s; s << x; return s.str(); }

template <class T> int toInt(const T &x)
{ stringstream s; s << x; int r; s >> r; return r; }

int t, a, b, k;

int
solve() {
  int ans = 0;
  for (int i = 0; i < a; i++) {
    for (int j = 0; j < b; j++) {
      int bitw = i & j;
      if (bitw < k) ans++;
    }
  }
  return ans;
}

int
main() {
  cin >> t;
  for (int z = 1; z <= t; z++) {
     cin >> a >> b >> k;
     printf("Case #%d: %d\n", z, solve());
  }
  return 0;
}
