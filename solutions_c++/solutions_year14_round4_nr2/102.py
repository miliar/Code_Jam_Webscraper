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
    int n, res = 0;
    cin >> n;
    vector<int> v(n);
    REP(i,n) cin >> v[i];
    REP(i,n) {
      int mi = 0;
      REP(j,v.size()) if (v[j] < v[mi]) mi = j;
      res += min(mi, (int)v.size() - mi - 1);
      v.erase(v.begin() + mi);
    }
    printf("Case #%d: %d\n", cas+1, res);
  }
  return 0;
}
