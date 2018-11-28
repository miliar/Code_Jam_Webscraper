#include <algorithm>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
#include <cstring>

#define SIZE(s) ((int)((s).size()))
#define FOREACH(it,vec) for(typeof((vec).begin())it=(vec).begin();it!=(vec).end();++it)
#define REP(i,n) for(int i=0;i<(int)(n);++i)

using namespace std;

vector<int> P;
int p, T, D;

int main(void) {
  cin >> T;
  REP(t, T) {
    cout << "Case #" << t+1 << ": ";
    cin >> D;
    P.resize(D);
    REP(d, D) cin >> P[d];
    sort(P.begin(), P.end());
    int best = 1000;
    for(int kopka=1; kopka <= 1000; ++kopka) {
      int cur = kopka;
      for(int j = SIZE(P)-1; j>= 0; --j) {
        if (P[j] <= kopka) break;
        cur += (P[j] + kopka - 1) / kopka - 1;
      }
      best = min(best, cur);
    }
    cout << best << endl;
  }
  return 0;
}
