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

int A[37];
int N,J;

bool dv(int base, int d, int len) {
  int r = 0;
  FOR(i,0,len) {
    r *= base;
    r += A[i];
    r %= d;
  }
  return (r == 0);
}

void rec(int pos, int len) {
  if(pos == len) {
    if(!A[len-1]) return;
    vi v;
    FOR(b,2,11) {
      bool di = false;
      FOR(d,2,100) {
        if(dv(b,d,len)) {di = true; v.PB(d); break;}
      }
      if(!di) return;
    }
    FOR(i,0,len) cout << A[i];
    FOR(i,0,v.size()) cout << " " << v[i];
    cout << endl;
    if(!--J) throw -1;
  } else {
    FOR(i,0,2) {
      A[pos] = i;
      rec(pos+1,len);
    }
  }
}

int main ()
{
  A[0] = 1;
  DRI(T);
  FOR(t,0,T) {
    printf("Case #%d:\n", t+1);
    RII(N,J);
    try {
      rec(1,N);
    } catch(int e) {}
  }
  return 0;
}
