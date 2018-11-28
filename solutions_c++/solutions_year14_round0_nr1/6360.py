#include <string>
#include <cstring>
#include <vector>
#include <cmath> 
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
 
using namespace std;
 
#define REP(a,n) for(int a=0; a<(n); ++a)
#define FOR(a,b,c) for(int a=(b); a<=(c); ++a)
#define FORD(a,b,c) for(int a=(b); a>=(c); --a)
#define INIT(i,v) __typeof(v) i = (v)
#define FOREACH(i,v) for(INIT(i, (v).begin()); i!=(v).end(); ++i)
#define MP make_pair
#define PB push_back
 
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long LL;
 
template<class T>
inline int size(const T&t){return t.size();}

#define INF 1000000000
 
//////////////////////////////////////////

int main() {
  int TT;
  scanf("%d", &TT);
  REP(tt, TT) {
    int y1, y2;
    scanf("%d", &y1);
    --y1;
    set<int> r1;
    REP(y, 4) REP(x, 4) {
      int a;
      scanf("%d", &a);
      if (y==y1)
        r1.insert(a);
    }
    vi wyn;
    scanf("%d", &y2);
    --y2;
    REP(y, 4) REP(x, 4) {
      int a;
      scanf("%d", &a);
      if (y==y2 && r1.find(a)!=r1.end())
        wyn.PB(a);
    }
    printf("Case #%d: ", tt+1);
    if (size(wyn)==1)
      printf("%d\n", wyn[0]);
    else
      printf(size(wyn) ? "Bad magician!\n" : "Volunteer cheated!\n");
  }
}


