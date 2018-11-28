#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <utility>
#include <queue>

#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define FOR(I,V) for (int I = 0; I < V; I++)
#define REP(I,A,B) for (int I = A; I <= B; I++)
#define FORD(I,V) for (int I = V-1; I >= 0; I--)
#define REPD(I,A,B) for (int I = A; I >= B; I--)
#define ALL(a) a.begin(), a.end()

#define MOD 1000002013

using namespace std;

typedef vector<int> VI;
typedef long long LL;
typedef unsigned long long ULL;

int n, m;
deque<pair<int, int> > tic;
vector<pair<int, int> > p;
int res1, res2;

void read()
{
  scanf("%d %d", &n, &m);
  p.clear();
  res1 = 0;
  FOR(i,m)
  {
    int aa, bb, pp;
    scanf("%d %d %d", &aa, &bb, &pp);
    p.pb(mp(aa, -pp));
    p.pb(mp(bb, pp));
    long long k = bb - aa;
    res1 += (((k * n - k * (k - 1) / 2) % MOD) * pp) % MOD;
    res1 %= MOD;
  }
  sort(ALL(p)); 
}

int solve()
{
  res2 = 0;
  FOR(i,2*m)
  {
    if (p[i].se < 0)
      tic.pb(mp(p[i].fi, -p[i].se));
    else
    {
      int ile = p[i].se;
      while (ile)
      {
        pair<int,int> out = tic.back();
        tic.pop_back();
        int ileout = min(out.se, ile);
        ile -= ileout;
        out.se -= ileout;
        if (out.se) tic.pb(out);
        long long k = p[i].fi - out.fi;
        res2 += (((k * n - k * (k - 1) / 2) % MOD) * ileout) % MOD;
        res2 %= MOD; 
      }
    }
  }
  //printf("%d %d aa\n", res1, res2);
  if (res2 > res1) res1 += MOD;
  return res1 - res2;
}

int main()
{
  int n;
  scanf("%d", &n);
  FOR(ii,n)
  {
    read();
    int res = solve();
    printf("Case #%d: %d\n", ii+1, res);
  }
  return 0;
}
