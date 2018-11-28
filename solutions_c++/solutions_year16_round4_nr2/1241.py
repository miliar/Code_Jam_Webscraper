#include <vector>
#include <list>
#include <map>
#include <unordered_set>
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

const int MAXN=205;
int n,m;
double pr[MAXN];
unordered_set<int> cc[MAXN];
int tmp[MAXN];

void init() {
  FORZ(i,MAXN) cc[i].clear();
}

void store(int x) {
  int tx=x;
  int cnt=0;
  while (x>0) {
    if (x%2==1) cnt++;
    x/=2;
  }
  cc[cnt].insert(tx);
}

double prob(int x, bool rev) {
  double res=1;
  int idx=0;
  while (x>0) {
    if (x%2==1) {
      if (rev) res*=(1.0-pr[idx]);
      else res*=pr[idx];
    }
    x/=2;
    idx++;
  }
  return res;
}

void solve() {
  init();
  cin>>n>>m;
  FORZ(i,n) cin>>pr[i];
  FORZ(i,1<<n) {
    store(i);
  }
  double res=0;
  for (int x : cc[m]) {
    double p=0;
    for (int a : cc[m/2]) {
      int b=x-a;
      if (cc[m/2].find(b)!=cc[m/2].end()) {
        p+=prob(a,true)*prob(b,false);
        p+=prob(a,false)*prob(b,true);
      }
    }
    p/=2.0;
    res=max(p,res);
  }
  printf("%.10f\n",res);
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
