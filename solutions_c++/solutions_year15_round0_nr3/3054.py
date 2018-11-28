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
#define INIT(a, v) __typeof(v) a = (v)
#define FOREACH(a, v) for (INIT(a, (v).begin()); a!=(v).end(); ++a)
 
template<class T>
inline int size(const T&t){return t.size();}
 
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef long long LL;

#define INF 1000000000
#define PB push_back
#define MP make_pair
 
//////////////////////////////////////////

int mnoz(int a, int b) {
  int m = a/4;
  a %= 4;
  b = b-'i'+1;
  int w = b;
  if (a==1 && b==1) m = !m, w = 0;
  if (a==1 && b==2) w = 3;
  if (a==1 && b==3) m = !m, w = 2;
  if (a==2 && b==1) m = !m, w = 3;
  if (a==2 && b==2) m = !m, w = 0;
  if (a==2 && b==3) w = 1;
  if (a==3 && b==1) w = 2;
  if (a==3 && b==2) m = !m, w = 1;
  if (a==3 && b==3) m = !m, w = 0;
  return w+m*4;
}

int L, X;
char txt[20000];
bool moge[20000][3][8];

int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        scanf("%d%d%s", &L, &X, txt);
        REP(a, 3) REP(b, 8) moge[0][a][b] = 0;
        moge[0][0][0] = 1;
        REP(z, L*X) {
          REP(a, 3) REP(b, 8) moge[z+1][a][b] = 0;
          REP(a, 3) 
            REP(b, 8) 
              if (moge[z][a][b]) {
                int w = mnoz(b, txt[z%L]);
                moge[z+1][a][w] = 1;
                if ((a==0 && w==1) || (a==1 && w==2))
                  moge[z+1][a+1][0] = 1;
              }
        }
        printf("Case #%d: %s\n", (tt+1), moge[L*X][2][3] ? "YES" : "NO");
    }
}


