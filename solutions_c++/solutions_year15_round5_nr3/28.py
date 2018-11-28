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

#define ll long long
#define ull unsigned long long

#define MM(co, cim) memset((co), (cim), sizeof((co)))

#define DEB(x) cerr << ">>> " << #x << " : " << x << endl;

#define EPS 1e-9

double P[27], S[27], dir[27];
double dyn[(1<<25)+7];

int main ()
{
  DRI(T);
  FOR(t,0,T) {
    double Y;
    cin >> Y;
    DRI(N);
    FOR(i,0,N) {
      cin >> P[i];
      if(P[i] < 0) {
        dir[i] = -1;
        P[i] = -P[i];
      }
      else dir[i] = 1;
    }
    FOR(i,0,N) {
      cin >> S[i];
    }
    FOR(m,0,(1<<N)) dyn[m] = -1;
    dyn[0] = 0;
    FOR(m,0,(1<<N)) {
      if(dyn[m] == -1) continue;
      double time = dyn[m];
      FOR(i,0,N) {
        if(m & (1<<i)) continue;
        int orMsk = (1<<i);
        double timeCatch = time + (P[i] + time*S[i]) / (Y-S[i]);
        FOR(j,0,N) {
          if(m & (1<<j)) continue;
          if(i == j) continue;
          if(dir[j] != dir[i]) continue;
          double timeCatch2 = time + (P[j] + time*S[j]) / (Y-S[j]);
          if(timeCatch2 - EPS < timeCatch) orMsk |= (1<<j);
        }
        int newState = m | orMsk;
        if(newState == (1<<N)-1) {
          if(dyn[newState] == -1) dyn[newState] = timeCatch;
          else if(dyn[newState] > timeCatch) dyn[newState] = timeCatch;
        } else {
          timeCatch = time + 2.0 * (P[i] + time*S[i]) / (Y-S[i]);
          if(dyn[newState] == -1) dyn[newState] = timeCatch;
          else if(dyn[newState] > timeCatch) dyn[newState] = timeCatch;
        }
      }
    }
    printf("Case #%d: %.6lf\n", t+1, dyn[(1<<N)-1]);
  }
  return 0;
}
