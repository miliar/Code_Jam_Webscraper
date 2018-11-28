#include <cstdio>
#include <algorithm>

using namespace std;

#define MAX_M 2000
#define MODULO 1000002013
int n,m;
int o[MAX_M];
int e[MAX_M];
int p[MAX_M];

pair<int,int> op[MAX_M];
pair<int,int> ep[MAX_M];
long long normgain;

long long price(long long s) 
{
  if(s==0)
    return 0;
  s--;
  return (n*(s+1) - (s*(s+1)/2)) % MODULO;
}

void read_input()
{
  scanf("%d %d",&n,&m);
  normgain = 0;

  for(int i=0; i<m; i++) {
    scanf("%d %d %d",&o[i],&e[i],&p[i]);
    op[i].first = o[i];
    op[i].second = p[i];
    ep[i].first = e[i];
    ep[i].second = p[i];
    normgain += p[i] * price(e[i] - o[i]);
    normgain %= MODULO;
  }
  sort(op,op+m);
  sort(ep,ep+m);
}

void solve(int t)
{
  read_input();

  int oi = 0;
  int ei = 0;
  long long cp = 0;
  long long cg = 0;

  int oldp[MAX_M];
  int oldpcount;
  int oldps[MAX_M];

  oldpcount = 0;

  int old_s;
  while(oi!=m || ei!=m) {
    if((oi!=m) && 
       ((ei==m) ||
        (op[oi].first <= ep[ei].first))) {

      oldp[oldpcount] = op[oi].second;
      oldps[oldpcount] = op[oi].first;
      oldpcount++;
      oi++;
    } else {

      int numout = ep[ei].second;
      while((numout >0) && (oldp[oldpcount-1] <= numout)) {
        cg += ((long long)oldp[oldpcount-1]) * price(ep[ei].first - oldps[oldpcount-1]);
        cg %= MODULO;
        numout -= oldp[oldpcount-1];
        oldpcount--;
      }
      if(numout > 0) {
        cg += ((long long)numout) * price(ep[ei].first - oldps[oldpcount-1]);
        cg %= MODULO;
        oldp[oldpcount-1] -= numout;
      }

      ei++;
    }
  }
  printf("Case #%d: %lld\n",t+1,(normgain - cg + MODULO) % MODULO);
}

main()
{
  int tt;
  scanf("%d",&tt);
  for(int t=0; t<tt; t++)
    solve(t);
}
