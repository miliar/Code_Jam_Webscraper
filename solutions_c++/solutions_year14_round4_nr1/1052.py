
// default code for competitive programming
// c2251393 ver 3.141 {{{

// Includes
#include <bits/stdc++.h>

// Defines
#define NAME(x) #x
#define SZ(c) (int)(c).size()
#define ALL(c) (c).begin(), (c).end()
#define FOR(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define REP(i, s, e) for(int i = (s); i <= (e); i++)
#define REPD(i, s, e) for(int i = (s); i >= (e); i--)
#define DEBUG 1
#define fst first
#define snd second
 
using namespace std;

// Typedefs
typedef double real;
typedef long long ll;
typedef pair<ll, int> pli;
typedef pair<int, int> pii;
typedef unsigned long long ull;

// Some common const.
const double EPS = -1e8;
const double Pi = acos(-1);
 
// Equal for double
bool inline equ(double a, double b)
{return fabs(a - b) < EPS;}

// }}}
// start ~~QAQ~~

const int MAXN = 10010;
const int MAXX = 710;

int n, x;
int in[MAXN];
bool vis[MAXN];

int main()
{
  int t;
  scanf("%d", &t);
  REP(__, 1, t)
  {
    printf("Case #%d: ", __);
    scanf("%d%d", &n, &x);
    REP(i, 1, n) scanf("%d", in+i);
    sort(in+1, in+1+n);
    fill(vis+1, vis+1+n, 0);
    int cnt = 0;
    REP(i, 1, n)
    {
      if(vis[i]) continue;
      cnt++;
      vis[i] = 1;
      int mx = -1, id = -1;
      REP(j, 1, n) if(!vis[j] && in[i] + in[j] <= x)
      {
        if(in[j] > mx)
        {
          mx = in[j];
          id = j;
        }
      }
      if(id > 0)
        vis[id] = 1;
    }
    printf("%d\n", cnt);
  }
}
