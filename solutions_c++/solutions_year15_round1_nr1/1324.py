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

const int MAXN = 10005;
int ar[MAXN],n;

void solve() {
  cin>>n;
  FORZ(i,n) scanf("%d",ar+i);
  int res=0,mx=0;
  FOR(i,1,n) {
    if (ar[i-1]>ar[i]) res+=ar[i-1]-ar[i];
    mx = max(mx,ar[i-1]-ar[i]);
  }
  cout << res << " ";
  res=0;
  FOR(i,1,n) {
    if (ar[i-1]>mx) res+=mx;
    else res+=ar[i-1];
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
