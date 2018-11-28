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

int t;
int gx, gy;


struct st {
  int x, y, jumps;
  string res;
  st(int _x = 0, int _y = 0, int _jumps = 1, string _res = "") {
    x = _x; y = _y; jumps = _jumps;
    res = _res;
  }
} now;

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
  scanf ("%d", &t);
  for (int c = 0; c < t; c++) {
    scanf("%d%d", &gx, &gy);
    queue <st> Q;
    Q.push(st());
    set < pair<int, int> > v[505];
    while (!Q.empty()) {
      now = Q.front(); Q.pop();
      if (now.x == gx && now.y == gy) break;
      if (v[now.jumps].insert(make_pair(now.x, now.y)).second == false) continue;
      Q.push(st(now.x + now.jumps, now.y, now.jumps + 1, now.res + "E"));
      Q.push(st(now.x - now.jumps, now.y, now.jumps + 1, now.res + "W"));
      Q.push(st(now.x, now.y + now.jumps, now.jumps + 1, now.res + "N"));
      Q.push(st(now.x, now.y - now.jumps, now.jumps + 1, now.res + "S"));
    }
    printf("Case #%d: ", c + 1);
    cout << now.res << endl;
  }
	return 0;
}