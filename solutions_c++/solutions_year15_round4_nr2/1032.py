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

double v,c;
int n;
double vr[2],cr[2];

bool equal(double a, double b) {
  return fabs(a-b)<1e-6;
}

void solve() {
  cin>>n>>v>>c;
  FORZ(i,n) {
    cin>>vr[i]>>cr[i];
  }
  if (n==1) {
    if (!equal(c,cr[0])) cout << "IMPOSSIBLE\n";
    else printf("%.10f\n",v/vr[0]);
  } else {
    double res=-1;
    if (equal(c,cr[0])&&equal(c,cr[1])) res=v/(vr[0]+vr[1]);
    else if (equal(c,cr[0])&&!equal(c,cr[1])) res=v/vr[0];
    else if (!equal(c,cr[0])&&equal(c,cr[1])) res=v/vr[1];
    else if (!(cr[0]<c&&cr[1]<c)&&!(cr[0]>c&&cr[1]>c)) {
      res=max(v*(cr[1]-c)/((cr[1]-cr[0])*vr[0]),v*(c-cr[0])/((cr[1]-cr[0])*vr[1]));
    }
    if (res<0) cout << "IMPOSSIBLE\n";
    else printf("%.10f\n",res);
  }
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
