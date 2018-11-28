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
int n,m,a,b,c,d;
char ch;
char in[103][103];
int x[2][102];
void solve()
  {
  scanf("%d%d",&n,&m);
  FOR(i,1,100)x[0][i]=x[1][i]=0;
  FOR(i,1,n)
    {
    FOR(j,1,m)
      {
      scanf(" %c",&in[i][j]);
      if(in[i][j]!='.')
        {
        x[0][i]++;
        x[1][j]++;
        }
      }
    }
  bool no=0;
  FOR(i,1,n)
    {
    FOR(j,1,m)
      {
      if(in[i][j]!='.')
        {
        if(x[0][i]==1&&x[1][j]==1)no=1;
        }
      }
    }
  if(no)
    {
    puts("IMPOSSIBLE");
    return;
    }
  int res=0; 
  FOR(i,1,n)
    {
    if(x[0][i]==0)continue;
    int pom=1;
    while(in[i][pom]=='.')pom++;
    if(in[i][pom]=='<')res++;
    pom=m;
    while(in[i][pom]=='.')pom--;
    if(in[i][pom]=='>')res++;
    }
  FOR(i,1,m)
    {
    if(x[1][i]==0)continue;
    int pom=1;
    while(in[pom][i]=='.')pom++;
    if(in[pom][i]=='^')res++;
    pom=n;
    while(in[pom][i]=='.')pom--;
    if(in[pom][i]=='v')res++;
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
