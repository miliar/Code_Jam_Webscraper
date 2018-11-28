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

int sum[1007];
vector<int> diff[107];
int mn[107], mx[107];

int main ()
{
  DRI(T);
  FOR(t,0,T) {
    DRII(N,K);
    FOR(i,0,N-K+1) {
      RI(sum[i]);
    }
    FOR(i,0,K) diff[i].clear();
    FOR(i,0,N-K+1-1) {
      diff[i%K].PB(sum[i+1]-sum[i]);
    }
    int mxdiff = 0;
    FOR(i,0,K) {
      mn[i] = 0;
      mx[i] = 0;
      int curr = 0;
      FOR(j,0,diff[i].size()) {
        curr += diff[i][j];
        mn[i] = min(mn[i],curr);
        mx[i] = max(mx[i],curr);
      }
      mxdiff = max(mxdiff,mx[i]-mn[i]);
    }
    int sum0 = sum[0];
    while(sum0 < 0) sum0 += K;
    sum0 %= K;
    int dsum = 0;
    FOR(i,0,K) dsum += abs(mn[i]);
    dsum %= K;
    if(sum0 < dsum) sum0 += K;
    int fre = 0;
    FOR(i,0,K) fre += mxdiff-(mx[i]-mn[i]);
    if(dsum + fre < sum0) mxdiff++;
    printf("Case #%d: %d\n", t+1, mxdiff);
  }
  return 0;
}
