#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define ALL(x) (x).begin(),(x).end()

using namespace std;

int main() {
  int t;
  cin >> t;
  REP(cas,t) {
    int n, x;
    cin >> n >> x;
    vector<int> v(n);
    REP(i,n) cin >> v[i];
    sort(v.begin(), v.end());
    int li = 0, la = n - 1, cnt = 0;
    while (la >= li) {
      if (v[la] + v[li] <= x) {
        la--; li++;
      }
      else {
        la--;
      }
      cnt++;
    }
    printf("Case #%d: %d\n", cas+1, cnt);
  }
  return 0;
}
