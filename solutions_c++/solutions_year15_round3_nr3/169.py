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

const int MAXD=105;
llong c,d,v,dn[MAXD];

void solve() {
  cin>>c>>d>>v;
  FORZ(i,d) cin>>dn[i];
  llong curr=1,res=0,sum=0;
  FORZ(i,d) {
    while (curr<dn[i]&&curr<=v) {
      res++;
      sum+=curr;
      curr=sum*c+1;
    }
    sum+=dn[i];
    curr=sum*c+1;
  }
  while (curr<=v) {
    res++;
    sum+=curr;
    curr=sum*c+1;
  }
  cout << res << endl;
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
