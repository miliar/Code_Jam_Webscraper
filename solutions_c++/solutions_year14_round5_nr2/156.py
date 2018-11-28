#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstring>

#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,p,k) for(int i=(p); i<=(k); ++i)

template<typename T> inline void checkmax(T &a, T b){ if(a<b) a = b; }

typedef long long LL;

int dyn[1000][3000];
enum { INF = 2000000000 };

int main()
{
  int t; std::cin >> t;
  FOR(_,1,t)
  {
    int p,q,n; scanf("%d%d%d",&p,&q,&n);
    std::vector<int> G(n),H(n);
    REP(i,n) scanf("%d%d",&H[i],&G[i]);
    std::vector<int> N(n),M(n);
    REP(i,n)
    {
      N[i] = (H[i]+q-1)/q;
      M[i] = ((H[i]-1)%q+p)/p;
      //printf("n=%d m=%d\n",N[i],M[i]);
      M[i] = N[i]-M[i]-1;
    }
    memset(dyn,-1,sizeof dyn);
    dyn[0][1] = 0;
    REP(i,n) REP(j,2500) if(dyn[i][j]>=0)
    {
      if(j+M[i]>=0) checkmax(dyn[i+1][j+M[i]],dyn[i][j]+G[i]);
      if(j+N[i]>=0) checkmax(dyn[i+1][j+N[i]],dyn[i][j]);
    }
    int res = -1;
    REP(i,3000) checkmax(res,dyn[n][i]);
    printf("Case #%d: %d\n",_,res);
  }
  return 0;
}
