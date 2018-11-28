#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
#include<set>
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
#define PLD pair<LD,LD>
using namespace std;
int n,m,a,b,c,d;
char ch;
LD V,X;//objętość, temperatura
vector<PLD> in;//temperatura tej wody,przepływ na jednostke czasu
LD A,B,C;
LD eps=1e-15;
LD zachlanuj(vector<PLD> w)
  {
  LD ob=0;
  LD ret=0;
  while(1)
    {
    LD temp=w.back().f;
    LD obj=min(w.back().s,V-ob);
    w.pop_back();
    
    ret=(ret*ob+temp*obj)/(ob+obj);
    ob+=obj;
    
    if(ob>=V-eps)break;
    }
  return ret;
  }
bool moge(LD x)
  {
  vector<PLD> pom=in;
  LD sumV=0;
  REP(i,pom.size())  
    {
    pom[i].s*=x;
    sumV+=pom[i].s;
    }
  if(sumV<V)
    {
    return 0;
    }
  sort(ALL(pom));
  LD mx=zachlanuj(pom);
  reverse(ALL(pom));
  LD mi=zachlanuj(pom);
  if(mi-eps<=X&&X-eps<=mx)return 1;
  return 0;
  }
void solve()
  {
  in.clear();
  cin>>n>>V>>X;
  FOR(i,1,n)
    {
    cin>>A>>B;
    in.PB(MP(B,A));    
    }
  LD poc=0;
  LD kon=1e10;
  if(moge(kon)==0)
    {
    puts("IMPOSSIBLE");
    return;
    }
  LD sr=-1;
  REP(i,20000)
    {
    sr=(poc+kon)/2;
    if(moge(sr))
      {
      kon=sr;
      }
    else
      {
      poc=sr;
      }
    }
  printf("%.9Lf\n",sr);
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
