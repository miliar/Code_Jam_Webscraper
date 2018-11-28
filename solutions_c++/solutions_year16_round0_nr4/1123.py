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
typedef unsigned long long llong;

#define pb push_back
#define FOR(i,s,n) for (llong (i) = (s); (i) < (n); (i)++)
#define FORZ(i,n) FOR((i),0,(n))

llong k,c,s;

void solve() {
  cin>>k>>c>>s;
  if (c>k) c=k;
  llong n=k-c+1;
  if (n>s) {
    cout<<"IMPOSSIBLE\n";
    return;
  }
  llong x=1;
  FOR(i,1,c+1) x*=k;
  llong idx=0;
  llong p=1;
  FOR(i,1,c) {
    x/=k;
    idx+=p*(x/k);
    p++;
  }
  FORZ(i,n) cout<<idx+i+1<<" ";
  cout<<"\n";
}

int main() {
#ifdef DEBUG
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif
  
  int t;
  scanf("%d", &t);
  FOR(i,1,t+1) {
    printf("Case #%lld: ", i);
    solve();
  }
  
  return 0;
}
