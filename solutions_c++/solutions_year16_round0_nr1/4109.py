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
using namespace std;
int n,a,b;
int t[10];
int cnt = 0;
void add2(int x)
  {
  if(t[x]==0){t[x]++;cnt++;}
  }
void add(int x)
  {
  while(x)
    {
    add2(x%10);
    x/=10;
    }
  }
void solve2(int x)
  {
  REP(i,10)t[i]=0;
  cnt = 0;
  FOR(i,1,1000)
    {
    add(x*i);
    if(cnt == 10)
      {
      printf("%d\n",x*i);
      return;
      }
    }
  puts("WUAAA");
  cerr<<"WUAA"<<endl;
  exit(-1);
  }
void solve()
  {
  int n;
  scanf("%d",&n);
  if(n==0)puts("INSOMNIA");
  else solve2(n);
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
