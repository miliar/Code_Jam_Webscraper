#include <bits/stdc++.h>

#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define ALL(x) (x).begin(),(x).end()

using namespace std;

int main() {
  int T;
  cin >> T;
  REP(cas,T) {
    int N; cin >> N;
    vector<int> v(N);
    REP(i,N) cin >> v[i];
    int res = 10000;
    REP(i,1010) {
      int sum = i + 1;
      for (int j : v)
        sum += (j + i) / (i + 1) - 1;
      res = min(res, sum);
    }
    printf("Case #%d: %d\n", cas+1, res);
  }
  return 0;
}
