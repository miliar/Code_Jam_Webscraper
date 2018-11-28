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
#include <iomanip>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
 
using namespace std; 

struct Tribe {
  int d, n, w, e, s, d_d, d_p, d_s;
  Tribe(int _d = 0, int _n = 0, int _w = 0, int _e = 0, int _s = 0, int _d_d = 0, int _d_p = 0, int _d_s = 0) {
    d = _d; n = _n; w = _w; e = _e; s = _s; d_d = _d_d; d_p = _d_p; d_s = _d_s;
  }
} now;

bool operator < (Tribe a, Tribe b) {
  return a.d < b.d;
}

int t;
int n, res, day;

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
  scanf ("%d", &t);
  for (int c = 0; c < t; c++) {
    scanf("%d", &n);
    res = day = 0;
    map <int, int> wall, attacks;
    map <int, int>::iterator it;
    multiset <Tribe> Q;
    for (int i = 0; i < n; i++) {
      scanf("%d%d%d%d%d%d%d%d", &now.d, &now.n, &now.w, &now.e, &now.s, &now.d_d, &now.d_p, &now.d_s);
      now.w *= 2;
      now.e *= 2;
      now.d_p *= 2;
      Q.insert(now);
    }
    while (!Q.empty()) {
      now = *Q.begin(); Q.erase(Q.begin());
      if (now.d > day) {
        // Upgrade wall
        for (it = attacks.begin(); it != attacks.end(); it++) wall[it->first] = it->second;
        attacks.clear();
      }
      day = now.d;
      // Attack!
      bool success = false;
      for (int i = now.w; i <= now.e; i++) {
        if (wall[i] < now.s) {
          success = true;
          attacks[i] = max(attacks[i], now.s);
        }
      }
      if (success == true) res++;
      // Advance tribe
      now.d += now.d_d;
      now.w += now.d_p;
      now.e += now.d_p;
      now.s += now.d_s;
      now.n--;
      if (now.n > 0) Q.insert(now);
    }
    printf("Case #%d: %d\n", c + 1, res);
  }
	return 0;
}