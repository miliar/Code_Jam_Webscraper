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
bool possible(int r,int p, int s)
  {
  if(abs(r - p) >= 2 || abs(r - s) >= 2 || abs(p - s) >= 2)
    {
    return 0;
    }  
  return 1;
  }
VI operator+(VI a, VI b)
  {
  if(a > b)swap(a, b);
  REP(i, b.size())a.PB(b[i]);
  return a;
  }
  
void print(VI V)
  {
  REP(i, V.size())printf("%c",V[i]);puts("");
  }
bool ok(int r,int p,int s, VI V)
  {
  REP(i, V.size())
    {
    if(V[i]=='R')r--;
    if(V[i]=='P')p--;
    if(V[i]=='S')s--;
    }
  if(p != 0 || r != 0 || s != 0)return 0;
  return 1;
  }
VI generate(int x,int who)
  {
  if(x == 0)
    {
    return {who};
    }
  
  if(who == 'P')return generate(x-1, 'P') + generate(x-1, 'R');
  if(who == 'R')return generate(x-1, 'R') + generate(x-1, 'S');
  if(who == 'S')return generate(x-1, 'P') + generate(x-1, 'S');
  }
void solve2(int n, int r, int p, int s)
  {
  if(abs(r - p) >= 2 || abs(r - s) >= 2 || abs(p - s) >= 2)
    {
    puts("IMPOSSIBLE");
    return;
    }
  VI V1 = generate(n, 'P');
  VI V2 = generate(n, 'R');
  VI V3 = generate(n, 'S');
  VVI V;
  if(ok(r, p, s, V1))V.PB(V1);
  if(ok(r, p, s, V2))V.PB(V2);
  if(ok(r, p, s, V3))V.PB(V3);
  if(V.size() != 1)
    {
    cerr<<"UWAGA"<<" "<<V.size()<<endl;
    REP(i, V.size())print(V[i]);
    exit(0);
    }
  sort(ALL(V));
  print(V[0]);
  }
void solve()
  {
  int r,p,s;
  scanf("%d%d%d%d",&n,&r,&p,&s);
  solve2(n, r, p, s);
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
