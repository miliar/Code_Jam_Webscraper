#include<bits/stdc++.h>
#define PII pair<int,int>
#define f first
#define s second
#define VI vector<int>
#define LL long long
#define MP make_pair
#define LD long double
#define PB push_back
#define ALL(V) V.begin(),V.end()
#define abs(x) max((x),-(x))
#define PDD pair<LD,LD> 
#define VPII vector< PII > 
#define siz(V) ((int)V.size())
#define FOR(x, b, e)  for(int x=b;x<=(e);x++)
#define FORD(x, b, e) for(int x=b;x>=(e);x--)
#define REP(x, n)     for(int x=0;x<(n);x++)
#define mini(a,b) a=min(a,b)
#define maxi(a,b) a=max(a,b)
#define VVI vector<VI>
#define VLD vector<LD>
using namespace std;
int n,m,a,b,c,d,k;
LD in[202];
LD dp[202][202];
LD calc(VLD V)
  {
  
  
  int n = V.size();
  FOR(i, 0, n)
    FOR(j, 0, n)
      dp[i][j]=0;
  dp[0][0] = 1;
  REP(i, V.size())
    {
    FOR(j, 0, n+1)
      {
      dp[i+1][j]=(j>0?(dp[i][j-1]*(V[i])) : 0) + dp[i][j] * (1-V[i]);      
      }
    }
//  REP(i, V.size()){printf("%.2Lf ",V[i]);}puts("");
    
  return dp[n][n/2];
  }
void solve()
  {
  scanf("%d%d",&n,&k);
  FOR(i,1,n)
    {
    scanf("%Lf",&in[i]);
    }
  sort(in+1, in+n+1);
  LD res = 0;
  int x = n - k;
  FOR(i, 1, n)
    {
    VLD V;
    int poc1 = 1;
    int kon1 = i-1;
    int poc2 = i+x;
    int kon2 = n;
    if(kon1 > n)break;
    FOR(j,poc1,kon1)V.PB(in[j]);
    FOR(j,poc2,kon2)V.PB(in[j]);
//    cerr<<V.size()<<endl;
    if(V.size() < k)continue;
    maxi(res, calc(V));
    
    }
  printf("%.8Lf\n", res);
  }
main()
{
int z;
scanf("%d",&z);
FOR(iii,1,z)
  {
  printf("Case #%d: ",iii);
  solve();
  }
}
