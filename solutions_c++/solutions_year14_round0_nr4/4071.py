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

typedef long long int ll;
typedef pair<int, int> pii;

#define PB push_back
#define MP make_pair

#define FOR(prom, a, b) for(int prom = (a); prom < (b); prom++)
#define FORD(prom, a, b) for(int prom = (a); prom > (b); prom--)
#define FORDE(prom, a, b) for(int prom = (a); prom >= (b); prom--)
#define SV(vec) {int s_v_;scanf("%d", &(s_v_));vec.PB(s_v_);}
#define MM(co, cim) memset((co), (cim), sizeof((co)))
#define DEB(x) cerr << ">>> " << #x << " : " << x << endl;

int t, n, n1, n2, k1, k2, rd, rn;
double a[1014], b[1014];

int main ()
{
  scanf("%d", &t);
  FOR(z, 0, t)
  {
    rd = rn = 0;
    scanf("%d", &n);
    FOR(i, 0, n) scanf("%lf", a + i);
    FOR(i, 0, n) scanf("%lf", b + i);
    sort(a, a + n);
    sort(b, b + n);
    n1 = 0;
    n2 = k2 = n - 1;
    while (k2 >= 0)
    {
      if (a[n2] > b[k2])
      {
        --n2;
        ++rd;
      }
      else ++n1;
      --k2;
    }
    n1 = k1 = 0;
    while (k1 < n)
    {
      while (k1 < n && b[k1] < a[n1])
      {
        ++rn;
        ++k1;
      }
      if (k1 < n)
      {
        ++n1;
        ++k1;    
      }
    }
    printf("Case #%d: %d %d\n", z + 1, rd, rn);
  }
  return 0;
}
