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

#pragma comment(linker, ”/STACK:108777216“)

#define Pi 3.141592653589793
#define all(c) (c).begin(), (c).end()
typedef long long ll;

int ri() {
  int res; scanf("%d", &res); return res;
}

class timer {
public:
  timer() : t_(clock()) {}
  void start() { t_ = clock(); }
  float elapsed() { return float(clock() - t_) / CLOCKS_PER_SEC; }
private:
  clock_t t_;
};

int arr1[4][4];
int arr2[4][4];

int main() {
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);

  int T; cin >> T;
  for (int qq = 1; qq <= T; ++qq) {
    int r1, r2; cin >> r1;
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        cin >> arr1[i][j];
      }
    }
    cin >> r2;
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        cin >> arr2[i][j];
      }
    }
    vector<int> res(4);
    set<int> s1(arr1[r1-1], arr1[r1-1] + 4);
    set<int> s2(arr2[r2-1], arr2[r2-1] + 4);
    vector<int>::iterator it = set_intersection(all(s1), all(s2), res.begin());
    int d = distance(res.begin(), it);
    cout << "Case #" << qq << ": ";
    if (!d) {
      cout << "Volunteer cheated!" << endl;
    } else if (d > 1) {
      cout << "Bad magician!" << endl;
    } else {
      cout << res[0] << endl;
    }
  }

  return 0;
}
