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

const int MAXN=1005;
int n;
string tpc[MAXN][2];

void solve() {
  cin>>n;
  FORZ(i,n) cin>>tpc[i][0]>>tpc[i][1];
  int res=0;
  FORZ(i,1<<n) {
    int cnt=0;
    bool valid=true;
    FORZ(j,n) {
      if (i&(1<<j)) {
        cnt++;
        bool found1=false,found2=false;
        FORZ(k,n) {
          if ((i&(1<<k))==0) {
            if (tpc[j][0].compare(tpc[k][0])==0) found1=true;
            if (tpc[j][1].compare(tpc[k][1])==0) found2=true;
          }
          if (found1&&found2) break;
        }
        if (found1&&found2) continue;
        valid=false;
        break;
      }
    }
    if (valid) res=max(res,cnt);
  }
  cout<<res<<"\n";
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
