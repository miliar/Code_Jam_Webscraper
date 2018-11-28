#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <limits>
#include <cstring>
#include <string>
using namespace std;

typedef pair<int,int> pairii;
typedef long long llong;

#define pb push_back
#define FOR(i,s,n) for (int (i) = (s); (i) < (n); (i)++)
#define FORZ(i,n) FOR((i),0,(n))

int r,c,n;
bool bld[20][20];

bool check(int x) {
  int c = 0;
  while (x>0) {
    c += x&1;
    x>>=1;
  }
  return c==n;
}

void solve() {
  cin>>r>>c>>n;
  int res=0x7fffffff;
  FORZ(i,1<<(r*c)) {
    if (check(i)) {
      FORZ(j,r)FORZ(k,c) bld[j][k]=false;
      FORZ(j,r)FORZ(k,c) {
        int tmp = j*c+k;
        if (i&(1<<tmp)) bld[j][k]=true;
      }
      int tmpr=0;
      FORZ(j,r)FORZ(k,c) {
        if (bld[j][k]) {
          if (j<r-1) tmpr+=bld[j+1][k];
          if (k<c-1) tmpr+=bld[j][k+1];
        }
      }
      res = min(res,tmpr);
    }
  }
  cout << res << "\n";
}

int main() {
#ifdef DEBUG
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif
  
  int t;
  scanf("%d", &t);
  FOR(i,1,t+1) {
    printf("Case #%d: ", i);
    solve();
  }
  
  return 0;
}
