#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <vector>

using namespace std;

#define FOR(prom, a, b) for(int prom = (a); prom < (b); prom++)
#define FORD(prom, a, b) for(int prom = (a); prom > (b); prom--)
#define FORDE(prom, a, b) for(int prom = (a); prom >= (b); prom--)

#define DRI(a) int a; scanf("%d ", &a);
#define DRII(a, b) int a, b; scanf("%d %d ", &a, &b);
#define DRIII(a, b, c) int a, b, c; scanf("%d %d %d ", &a, &b, &c);
#define DRIIII(a, b, c, d) int a, b, c, d; scanf("%d %d %d %d ", &a, &b, &c, &d);
#define RI(a) scanf("%d ", &a);
#define RII(a, b) scanf("%d %d ", &a, &b);
#define RIII(a, b, c) scanf("%d %d %d ", &a, &b, &c);
#define RIIII(a, b, c, d) scanf("%d %d %d %d ", &a, &b, &c, &d);

#define PB push_back
#define MP make_pair

#define ff first
#define ss second
#define vi vector<int>
#define pii pair<int,int>

#define ll long long
#define ull unsigned long long

#define MM(co, cim) memset((co), (cim), sizeof((co)))

#define DEB(x) cerr << ">>> " << #x << " : " << x << endl;

int bits(int a) {
  int c = 0;
  while(a) {
    if(a&1) c++;
    a /= 2;
  }
  return c;
}
double P[207];
double d[20][20];

int main ()
{
  DRI(T);
  FOR(t,0,T) {
    double res = 0;
    DRII(N,K);
    FOR(i,0,N) cin >> P[i];
    FOR(m,0,(1<<N)) {
      if(bits(m) == K) {
        MM(d,0.0);
        d[0][0] = 1.0;
        int p = 0;
        FOR(i,0,N) {
          if(m & (1<<i)) {
            FOR(j,0,K) {
              d[p+1][j+1] += d[p][j] * P[i];
              d[p+1][j] += d[p][j] * (1.0-P[i]);
            }
            p++;
          }
        }
        res = max(res,d[K][K/2]);
      }
    }
    printf("Case #%d: %.10f\n", t+1, res);
  }
  return 0;
}










