#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>
   
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <complex>
#include <limits>
#include <functional>
#include <numeric>

using namespace std;

#define fr(a,b,c) for(int (a) = (b); (a) < (c); ++(a))
#define rp(a,b) fr(a,0,b)
#define cl(a,b) memset((a), (b), sizeof(a))
#define sc(a) scanf("%d", &a)
#define sc2(a,b) scanf("%d%d", &a, &b)
#define sc3(a,b,c) scanf("%d%d%d", &a, &b, &c)
#define scs(s) scanf("%s", s)
#define pri(x) printf("%d\n", x)
#define fre(a,b) for(int a = adj[b]; ~a; a = ant[a])

#define iter(a) __typeof((a).begin())
#define fore(a,b) for(iter(b) a = (b).begin(); a != (b).end(); ++a)

#define st first
#define nd second
#define mp make_pair
#define pb push_back

#define db(x) cerr << #x << " == " << x << endl
#define _ << ", " <<

#define add(a,b) to[z] = b, ant[z] = adj[a], adj[a] = z++

const int oo = 0x3f3f3f3f;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<int> vi;

double pd[202][102];
int mark[202][102], passo;
int N, K;
double P[202], R[202];
double go(int k, int y) {
  if (y > K/2) return 0.0;
  if (k == 0) return (y == K/2) * 1.0;
  double &ret = pd[k][y];
  if (mark[k][y] == passo) return ret;
  mark[k][y] = passo;
  return ret = P[k-1] * go(k-1, y+1) + (1.0 - P[k-1]) * go(k-1, y);
}

int main() {
  cl(mark,0);
  passo = 0;
  int t; sc(t);
  int cas = 1;
  while (t--) {
    sc2(N,K);
    vector<double> v1, v2;
    rp(i,N) scanf("%lf", &R[i]);
    sort(R, R+N);

    double ans = 0;
    rp(i,N-K+1) {
      int ps = 0;
      rp(j,K) P[ps++] = R[i+j];
      passo++;
      ans = max(ans, go(K,0));
    }
    int qnt = 0;
    fr(k,1,K) {
      int a = k;
      int b = K-k;
      int ps = 0;
      rp(e,a) P[ps++] = R[e];
      rp(e,b) P[ps++] = R[N-1-e];
      passo++;
      qnt++;
      ans = max(ans, go(K,0));
    }
    printf("Case #%d: %.10lf\n", cas++, ans);
  }
  return 0;
}






