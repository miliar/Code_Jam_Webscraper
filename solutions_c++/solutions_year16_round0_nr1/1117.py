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

bool vis[10];

bool check() {
  FORZ(i,10) if (!vis[i]) return false;
  return true;
}

void solve() {
  llong n;
  scanf("%lld",&n);
  if (n==0) {
    printf("INSOMNIA\n");
    return;
  }
  memset(vis, 0, sizeof vis);
  llong i=1;
  do {
    llong tmp=n*i;
    while (tmp>0) {
      vis[tmp%10]=true;
      tmp/=10;
    }
    i++;
  } while (!check());
  printf("%lld\n",n*(i-1));
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
