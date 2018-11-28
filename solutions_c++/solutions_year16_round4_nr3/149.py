// Jakub Radoszewski

//#include<iostream>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
#include<numeric>
#include<cassert>
using namespace std;

#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define FORD(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,N) for(int I=0;I<(N);I++)
#define ALL(X) (X).begin(),(X).end()
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define INFTY 100000000
#define VAR(V,init) __typeof(init) V=(init)
#define FORE(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
#define SIZE(x) ((int)(x).size())

typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long ll;
typedef vector<string> VS;

ll nwd(ll a,ll b) { return !b?a:nwd(b,a%b); }
inline int CEIL(int a,int b) { return a%b ? a/b+1 : a/b; }
template <class T> inline T sqr(const T&a) { return a*a; }

int los(int m)
{
  return (int)((double)m*(rand()/(RAND_MAX+1.0)));
}

int r,c,ile,start;
char st[20][20];

int n;
VI t[100];
int dane[100];

void add_edge(int i,int j)
{
  t[i].PB(j); t[j].PB(i);
}

inline int numer(int i,int j)
{
  return i*c+j;
}

void graf()
{
  REP(i,n) t[i].clear();
  REP(i,r) REP(j,c-1)
  {
    int a=numer(i,j),b=numer(i,j+1);
    if (st[i][j]=='/' && st[i][j+1]=='/') add_edge(2*a,2*b+1);
    if (st[i][j]=='/' && st[i][j+1]=='\\') add_edge(2*a,2*b);
    if (st[i][j]=='\\' && st[i][j+1]=='/') add_edge(2*a+1,2*b+1);
    if (st[i][j]=='\\' && st[i][j+1]=='\\') add_edge(2*a+1,2*b);
  }
  REP(i,r-1) REP(j,c)
  {
    int a=numer(i,j),b=numer(i+1,j);
    if (st[i][j]=='/' && st[i+1][j]=='/') add_edge(2*a,2*b+1);
    if (st[i][j]=='/' && st[i+1][j]=='\\') add_edge(2*a,2*b+1);
    if (st[i][j]=='\\' && st[i+1][j]=='/') add_edge(2*a,2*b+1);
    if (st[i][j]=='\\' && st[i+1][j]=='\\') add_edge(2*a,2*b+1);
  }
  start=2*r*c;
  int akt=start;
  REP(j,c)
  {
    int b=numer(0,j);
    add_edge(akt,2*b+1);
    ++akt;
  }
  REP(i,r)
  {
    int b=numer(i,c-1);
    if (st[i][c-1]=='/') add_edge(akt,2*b); else add_edge(akt,2*b+1);
    ++akt;
  }
  FORD(j,c-1,0)
  {
    int b=numer(r-1,j);
    add_edge(akt,2*b);
    ++akt;
  }
  FORD(i,r-1,0)
  {
    int b=numer(i,0);
    if (st[i][0]=='/') add_edge(akt,2*b+1); else add_edge(akt,2*b);
    ++akt;
  }
  assert(akt==n);
}

bool col[100];

int dfs(int v)
{
  col[v]=1;
  int w=-1;
  REP(i,SIZE(t[v]))
  {
    int u=t[v][i];
    if (!col[u])
    {
      if (u>=start)
      {
        if (w==-1) w=u; else w=-2;
      }
      int x=dfs(u);
      if (x>=0)
      {
        if (w==-1) w=x; else w=-2;
      }
    }
  }
  return w;
}

inline bool sprawdz()
{
  REP(i,n) col[i]=0;
  REP(i,ile/2)
  {
    int a=dane[2*i],b=dane[2*i+1];
    if (dfs(start+a)!=start+b) return false;
  }
  return true;
}

void mymain()
{
  scanf("%d%d",&r,&c);
  ile=2*(r+c);
  REP(i,ile) { scanf("%d",dane+i); --dane[i]; }

  n=2*r*c+ile;
  REP(mask,(1<<(r*c)))
  {
    int ii=0;
    REP(i,r) REP(j,c)
    {
      if (mask&(1<<ii)) st[i][j]='\\'; else st[i][j]='/';
      ++ii;
    }
    graf();
    if (sprawdz())
    {
      REP(i,r)
      {
        REP(j,c) putchar(st[i][j]);
        puts("");
      }
      return;
    }
  }
  puts("IMPOSSIBLE");
}

int main()
{
  int ILE;
  scanf("%d",&ILE);
  FOR(iii,1,ILE)
  {
    printf("Case #%d:\n",iii);
    fprintf(stderr,"Case #%d:\n",iii);
    mymain();
  }
  return 0;
}
