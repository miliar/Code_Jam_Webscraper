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

int N;
int w[3][3];
int r[3];
int R[3];
int A[13];
int B[13];
string s[3][13];

char C[] = "PRS";

bool rec(int n) {
  if(n == N) {
    FOR(i,0,n) B[i] = A[i];
    while(n > 1) {
      n /= 2;
      FOR(i,0,n) {
        if(B[2*i] == B[2*i+1]) return false;
        B[i] = w[B[2*i]][B[2*i+1]];
      }
    }
    FOR(i,0,N) cout << C[A[i]];
    cout << endl;
    return true;
  } else {
    FOR(i,0,3) {
      if(r[i]) {
        r[i]--;
        A[n] = i;
        if(rec(n+1)) return true;
        r[i]++;
      }
    }
  }
  return false;
}

int main ()
{
  
  w[0][1] = 0;
  w[1][0] = 0;
  w[0][2] = 2;
  w[2][0] = 2;
  w[1][2] = 1;
  w[2][1] = 1;
  
  s[0][0] = "P";
  s[1][0] = "R";
  s[2][0] = "S";
  FOR(d,1,13) {
    if(s[0][d-1] < s[1][d-1]) s[0][d] = s[0][d-1] + s[1][d-1];
    else s[0][d] = s[1][d-1] + s[0][d-1];
    if(s[1][d-1] < s[2][d-1]) s[1][d] = s[1][d-1] + s[2][d-1];
    else s[1][d] = s[2][d-1] + s[1][d-1];
    if(s[0][d-1] < s[2][d-1]) s[2][d] = s[0][d-1] + s[2][d-1];
    else s[2][d] = s[2][d-1] + s[0][d-1];
  }
  DRI(T);
  FOR(t,0,T) {
    RI(N);
    RIII(r[1],r[0],r[2]);
    bool f = false;
    string re = s[0][N];
    FOR(p,0,3) {
      MM(R,0);
      FOR(i,0,s[p][N].size()) FOR(j,0,3) if(s[p][N][i] == C[j]) R[j]++;
      bool ok = true;
      FOR(i,0,3) if(R[i] != r[i]) ok = false;
      if(ok) {
        if(!f || s[p][N] < re) re = s[p][N];
        f = true;
      }
    }
    printf("Case #%d: ", t+1);
    if(f) cout << re << endl;
    else cout << "IMPOSSIBLE" << endl;
  }
  return 0;
}










