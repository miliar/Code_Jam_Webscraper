#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstring>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
#define SIZE(x) (int((x).size()))
#define rep(i,l,r) for (int i=(l); i<=(r); i++)
#define repd(i,r,l) for (int i=(r); i>=(l); i--)
#define rept(i,c) for (typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#ifndef ONLINE_JUDGE
#define debug(x) { cerr<<#x<<" = "<<(x)<<endl; }
#else
#define debug(x) {}
#endif
int n;
double tv, tt;
typedef pair<double, double> P;
P inp[110];
const double eps = 1e-10;
void lemon() {  
  scanf("%d%lf%lf",&n,&tv,&tt);
  double sv = 0;
  rep(i,1,n) {
    scanf("%lf%lf",&inp[i].second,&inp[i].first);
    sv += inp[i].second;
  }
  sort(inp+1, inp+n+1);
  double L=tv/sv,R=1e12,M;
  rep(itr,0,100) {
    M = (L+R)/2;
    double cv=0, ct=0, mt, Mt;
    rep(i,1,n) {
     // printf("%d %f %f\n", i, inp[i].first, inp[i].second);
      if (cv >= tv) break;
      if (cv + inp[i].second * M <= tv) {
        cv += inp[i].second * M;
        ct += inp[i].second * M * inp[i].first;
      } else {
        ct += (tv-cv) * inp[i].first;
        cv += tv - cv;
      }
    }
    //printf("%lf %lf\n", ct, cv);
    mt = ct/cv;
    ct=0;
    cv=0;
    repd(i,n,1) {
      if (cv >= tv) break;
      if (cv + inp[i].second * M <= tv) {
        cv += inp[i].second * M;
        ct += inp[i].second * M * inp[i].first;
      } else {
        ct += (tv-cv) * inp[i].first;
        cv += tv - cv;
      }
    }
    Mt = ct/cv;
    if (Mt >= tt-eps && mt <= tt+eps) R = M;
    else L = M;
  }
  if (L > 5e11) puts("IMPOSSIBLE");
  else printf("%.10f\n", L);
}
int main() {
  ios::sync_with_stdio(true);
  #ifndef ONLINE_JUDGE
  //  freopen("","r",stdin);
  #endif
  int cas;
  scanf("%d",&cas);
  rep(i,1,cas) {
  	printf("Case #%d: ",i);
  	lemon();
  }
  return 0;
}