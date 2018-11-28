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
using namespace std;
int n,m,a,b,c,d;
const int MXN = 5;
int in[MXN][MXN];
int cpin[MXN][MXN];
bool used[MXN];
bool rec(VI V)
  {
  if(V.size() == 0)return 1;
  int x = V.back();
  V.pop_back();
  int pasuje = 0;
  bool ok = 1;
  FOR(i,1,n)
    {
    if(used[i])continue;
    if(in[x][i] == 0)continue;
    pasuje++;
    
    used[i] = 1;
    ok &= rec(V);
    used[i] = 0;
    }
  if(pasuje == 0)return 0;
  return ok;
  }
bool isok()
  {
  VI V;
  REP(i, n)
    {
    V.PB(i+1);
    }
  do
    {
    if(rec(V)==0)return 0;    
    }
  while(next_permutation(ALL(V)));
  return 1;
  }
void solve()
  {
  scanf("%d",&n);
  FOR(i,1,n)
    FOR(j,1,n)
      {
      char ch;
      scanf(" %c",&ch);
      cpin[i][j] = in[i][j] = ch-'0';
      }
  int res = 1e9; 
 
  REP(u, 1<<(n*n))
    {
    bool kk = 1;
    FOR(i,1,n)
     FOR(j,1,n)
      in[i][j]=cpin[i][j];
    
    int x = 0;
    FOR(i,1,n)
      {
      FOR(j,1,n)
        {
        if((1<<x) & u)
          {
          if(in[i][j])kk = 0;
          in[i][j] = 1;
          }
        x++;
        }
      }
    if(kk == 0)continue;
    if(isok())mini(res, __builtin_popcount(u));
    }
  printf("%d\n",res);  
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
