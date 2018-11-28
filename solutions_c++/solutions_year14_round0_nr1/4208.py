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

int t, a, c, cnt[114], tc, ti;

int main ()
{
  scanf("%d", &t);
  FOR(q, 0 ,t)
  {
    MM(cnt, 0);
    FOR(k, 0, 2)
    {
      scanf("%d", &a);
      --a;
      FOR(i, 0, 4) FOR(j, 0, 4)
      {
        scanf("%d", &c);
        if (i == a) ++cnt[c];
      }
    }
    tc = 0;
    FOR(i, 0, 114) if (cnt[i] == 2)
    {
      ++tc;
      ti = i;
    }
    printf("Case #%d: ", q + 1);
    if (!tc) printf("Volunteer cheated!\n");
    else if (tc == 1) printf("%d\n", ti);
    else printf("Bad magician!\n");
  }
  return 0;
}
