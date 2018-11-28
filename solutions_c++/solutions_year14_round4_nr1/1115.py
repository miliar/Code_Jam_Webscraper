#include<iostream>
#include<string.h>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<list>
#include<stack>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cassert>
#define CLRM(x) memset(x,-1,sizeof(x))
#define CLR(x) memset(x,0,sizeof(x))
#define ALL(x) x.begin(),x.end()
#define GI(x) scanf("%d", &x);
#define FORN(i, n) for(int i = 0; i < n; i++)
#define FOR(i, start, end) for(int i = start; i < end; i++)
#define PB push_back
#define MP make_pair
#define VI vector<int> 
#define VVI vector<vector<int> >
#define PII pair<int,int>
#define SZ(x) (int)x.size()
#define LL long long
#define MIN(a,b) (a)<(b)?(a):(b)
#define MAX(a,b) (a)>(b)?(a):(b)
#define LMAX 1000000000000000000LL
#define IMAX 1000000000
using namespace std;

int sz;
int n;
vector<int> v;

int solve() {
  sort(ALL(v));
  int ret = 0;
  while(v.size() > 0) {
    ret++;
    int t = v[0];
    v.erase(v.begin());
    int lo = 0, hi = v.size();
    while (hi-lo > 3) {
      int mid = (lo+hi)/2;
      if (v[mid] + t <= sz) {
        lo = mid;
      } else {
        hi = mid;
      }
    }
    int found = 0;
    int i = -1;
    for(i = lo; i < hi; i++) {
      if (t + v[i] > sz) break;
      found = 1;
    }
    if (found) {
      v.erase(v.begin()+i-1);
    }
  }
  return ret;
}

int main() {
  int tes;
  GI(tes);
  FORN(x, tes) {
    v.clear();
    GI(n);
    GI(sz);
    FORN(i, n) {
      int t;
      GI(t);
      v.PB(t);
    }
    int ans = solve();
    printf("Case #%d: %d\n", x+1, ans);
  }
}
