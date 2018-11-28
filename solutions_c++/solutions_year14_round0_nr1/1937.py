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

int d[2][4][4];

void get(int x[][4]) {
  FORN(i, 4)
    FORN(j, 4) {
      GI(x[i][j]);
    }
}

void proc() {
  int n, m;
  GI(n);
  get(d[0]);
  GI(m);
  get(d[1]);
  set<int> one;
  FORN(i, 4) one.insert(d[0][n-1][i]);
  int sz = 0;
  int val = -1;
  FORN(i, 4) {
    int v = d[1][m-1][i];
    if (one.find(v) != one.end()) {
      val = v;
      sz++;
    }
  }
  if (sz == 1) {
    printf("%d\n", val);
  } else if (sz > 1) {
    printf("Bad magician!\n");
  } else {
    printf("Volunteer cheated!\n");
  }
}

int main() {
  int tes;
  GI(tes);
  FORN(t, tes) {
    printf("Case #%d: ", t+1);
    proc();
  }
}
