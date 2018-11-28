#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cassert>
using namespace std;
typedef long long ll;

#define REP(i,n) for(int i = 0; i < (int)(n); ++i)
#define FOR(i,k,n) for(int i = (k); i < (int)(n); ++i)
#define FOREQ(i,k,n) for(int i = (k); i <= (int)(n); ++i)
#define FORIT(i,c) for(__typeof((c).begin())i=(c).begin(); i!=(c).end(); ++i)
#define SZ(v) (int)((v).size())
#define MEMSET(v,h) memset((v),(h),sizeof(v))

int main() {
  int T; cin >> T;
  for(int t = 1; t <= T; ++t) {
    int n, m; cin >> n >> m;
    vector<vector<int>> fld(n, vector<int>(m));
    REP(i, n) REP(j, m) cin >> fld[i][j];

    vector<int> row(n), col(m);
    REP(i, n) {
      row[i] = 0;
      REP(j, m) row[i] = max(row[i], fld[i][j]);
    }
    REP(j, m) {
      col[j] = 0;
      REP(i, n) col[j] = max(col[j], fld[i][j]);
    }

    bool possible = true;
    REP(i, n) REP(j, m) {
      int const x = fld[i][j];
      if(x < row[i] && x < col[j]) possible = false;
    }

    cout << "Case #" << t << ": ";
    cout << (possible ? "YES" : "NO") << endl;
  }
}
