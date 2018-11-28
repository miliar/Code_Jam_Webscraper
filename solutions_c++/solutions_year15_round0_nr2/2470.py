#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;
#define DEBUG(x) cerr << '>' << #x << ':' << (x) << endl;
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,a) for(int i=0; i<(a);++i)
inline bool EQ(double a, double b) {return fabs(a-b) < 1e-9;}

typedef long long ll;
int T, D;
int A[2000];

int splitMoves(int from, int to) {
  return max(0, (from - 1) / to);
}

int main() {
  scanf("%d", &T);
  REP(t,T) {
    scanf("%d", &D);
    REP(i,D) scanf("%d", A+i);
    
    int m = 0;
    REP(i,D) m = max(m, A[i]);
    
    int best = m;
    FOR(normal, 1, m) {
      int special = 0;
      REP(i, D) {
        special += splitMoves(A[i], normal);
      }
      best = min(best, special + normal);
    }
    
    printf("Case #%d: %d\n", t+1, best);
  }
  return 0;
}
