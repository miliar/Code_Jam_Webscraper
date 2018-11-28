#include <cmath>
#include <functional>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <unordered_map>
#include <queue>
#include <set>
using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define REP(i,n) FOR(i,0,n)

double c, f, x;

int main() {
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);

  int T;
  cin >> T;
  REP(tests,T) {
    cout << "Case #" << tests + 1 << ": ";
    cin >> c >> f >> x;
    double ans = 1e10;
    double cur = 0;
    double produce = 2;
    for (int i = 0; i < 100000; ++i) {
      ans = min(ans, cur + x / produce);
      cur += c / produce;
      produce += f;
    }

    cout.precision(10);
    cout << fixed << ans << endl;
  }
  return 0;
}