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
int n;
vector<int> v;

int numSwaps(VI v1) {
  int ret = 0;
  FORN(i, n) {
    int pos = 0;
    FORN(j, n) {
      if (v1[j] == v[i]) {
        pos = j;
        break;
      }
    }
    for (int j = pos; j > i; j--) {
      int tx = v1[j];
      v1[j] = v1[j-1];
      v1[j-1] = tx;
      ret++;
    }
  }
  return ret;
}

bool isValid(VI v1) {
  int mx = 0;
  FORN(i, SZ(v1)) {
    if (v1[mx] < v1[i]) mx = i;
  }
  for (int i = 0; i < mx; i++) {
    if (v1[i] > v1[i+1]) return false;
  }
  for (int i = mx+1; i < n; i++) {
    if (v1[i] > v1[i-1]) return false;
  }
  return true;
}

void printvec(VI x) {
  FORN(i, SZ(x)) {
    cout<<x[i]<<", ";
  }
  cout<<endl<<endl;
}

int solve() {
  int ret = 1e9;
  VI t = v;
  sort(ALL(t));
  do {
    if (isValid(t)) {
      //cout<<"isvalid"<<endl;
      int x = numSwaps(t);
      if (ret > x) {
        ret = x;
        //printvec(t);
      }
    }
  } while(next_permutation(ALL(t)));
  return ret;
}

int main() {
  int tes;
  GI(tes);
  FORN(x, tes) {
    v.clear();
    GI(n);
    FORN(i, n) {
      int t;
      GI(t);
      v.PB(t);
    }
    int ans = solve();
    printf("Case #%d: %d\n", x+1, ans);
  }
}
