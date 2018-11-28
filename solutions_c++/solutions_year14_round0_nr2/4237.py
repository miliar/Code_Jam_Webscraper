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

int t;
double c, f, x, prod, res, cand, bprod;

int main ()
{
  scanf("%d", &t);
  FOR(q, 0, t)
  {
    scanf("%lf%lf%lf", &c, &f, &x);
    prod = 2.0;
    bprod = 0.0;
    res = x / prod;
    cand = x / (prod + f) + c / prod;
    while (cand < res)
    {
      res = cand;
      bprod += c / prod;
      prod += f;
      cand = x / (prod + f) + c / prod + bprod;
    }
    printf("Case #%d: %.7f\n", q + 1, res);
  }
  return 0;
}
