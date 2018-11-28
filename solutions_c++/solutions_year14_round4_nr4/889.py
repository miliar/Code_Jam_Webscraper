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

int n, m;
vector<string> v;

void printvec(VI x) {
  FORN(i, SZ(x)) {
    cout<<x[i]<<", ";
  }
  cout<<endl<<endl;
}

int mx = -1, nmx = 0;

int distinctp(vector<int> vs) {
  set<string> s;
  FORN(i, SZ(vs)) {
    string st = v[vs[i]];
    for(int j=1; j <= st.size(); j++) {
      s.insert(st.substr(0, j));
    }
  }
  return s.size()+1;
}

int getNodes(VI t) {
  int ret = 0;
  FORN(i, n) {
    VI tx;
    FORN(j, SZ(t)) {
      if (t[j] == i) {
        tx.PB(j);
      }
    }
    if (tx.size() > 0) {
      int x = distinctp(tx);
      ret += x;
    }
  }
  return ret;
}

void rec(VI t, int pos) {
  if (pos == m) {
    int nodes = getNodes(t);
    //printvec(t);
    //cout<<"nodes: " <<nodes<<endl;
    if (mx < nodes) {
      nmx = 1;
      mx = nodes;
    } else if (mx == nodes) {
      nmx++;
    }
    return;
  }
  FORN(i, n) {
    VI x = t;
    x.PB(i);
    rec(x, pos+1);
  }
}

PII solve() {
  VI tx;
  mx = 0, nmx = -1;
  rec(tx, 0);
  return MP(mx, nmx);
}

int main() {
  int tes;
  GI(tes);
  FORN(x, tes) {
    v.clear();
    GI(m); GI(n);
    FORN(i, m) {
      string s;
      cin >> s;
      v.PB(s);
    }
    PII p = solve();
    printf("Case #%d: %d %d\n", x+1, p.first, p.second);
  }
}
