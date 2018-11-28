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
typedef long double ld;

ll nwd(ll a,ll b) { return !b?a:nwd(b,a%b); }
inline int CEIL(int a,int b) { return a%b ? a/b+1 : a/b; }
template <class T> inline T sqr(const T&a) { return a*a; }

int los(int m)
{
  return (int)((double)m*(rand()/(RAND_MAX+1.0)));
}

struct pkt
{
  int x,y,z;
};

inline pkt operator-(pkt a,pkt b)
{
  pkt p;
  p.x=a.x-b.x;
  p.y=a.y-b.y;
  p.z=a.z-b.z;
  return p;
}

void wypisz(ld x)
{
  printf("%.5Lf",x);
}

inline ld operator*(pkt a,pkt b)
{
  return (ld)(a.x*b.x+a.y*b.y+a.z*b.z);
}

inline ld norm(pkt a)
{
  return (ld)(sqr(a.x)+sqr(a.y)+sqr(a.z));
}

int n,s;
pkt asteroidy[1010],predkosci[1010];

pair<ld,ld> intervals[1010][1010];

inline ld dist(pkt a,pkt b)
{
  return sqrtl((ld)(sqr(a.x-b.x)+sqr(a.y-b.y)+sqr(a.z-b.z)));
}

const ld EPS=1e-9;

inline pair<ld,ld> interval(pkt c,pkt av,pkt o,pkt l,ld r)
{
  l=l-av;

  if (l.x==0 && l.y==0 && l.z==0)
  {
    if (dist(c,o)<=r) return MP(0,1e7); else return MP(-1.,-1.);
  }
  
  ld podpierw=sqr(l*(o-c))-norm(l)*(dist(o,c)-sqrt(r));
  if (podpierw<=-EPS) return MP(-1.0,-1.0);
  ld lo=(-(l*(o-c))-sqrtl(podpierw))/norm(l);
  ld hi=(-(l*(o-c))+sqrtl(podpierw))/norm(l);
  if (hi<=-EPS) return MP(-1.0,-1.0);
  lo=max(lo,(ld)0.0);
  return MP(lo,hi);
}

int N;
int node[1010][1010];
//int celmin,celmax;

VI kraw[1010000];
bool vis[1010000];

bool czy;

void dfs(int v,int nv)
{
  if (czy) return;
  vis[nv]=true;
  if (v==1) { czy=true; return; }
  REP(i,SIZE(kraw[nv]))
  {
    int u=kraw[nv][i];
    assert(node[v][u]==nv);
    int nu=node[u][v];
    if (vis[nu]) continue;
    dfs(u,nu);
  }
}

bool dasie(ld d)
{
  REP(i,n) REP(j,n) if (i!=j)
  {
    intervals[i][j]=interval(asteroidy[i],predkosci[i],asteroidy[j],predkosci[j],d);
    //printf("%d %d ",i,j); wypisz(intervals[i][j].FI); putchar(' '); wypisz(intervals[i][j].SE); puts("");
  }

  N=0;

  REP(i,n)
  {
    vector<pair<ld,int> > pom;
    REP(j,n) if (j!=i)
    {
      pair<ld,ld> p=intervals[i][j];
      if (p.FI<0.0) continue;
      pom.PB(MP(p.FI,j+1));
      pom.PB(MP(p.SE,-(j+1)));
    }
    sort(ALL(pom));

    vector<pair<pair<ld,ld>,VI> > pom2,pom3;
    int a=0;
    ld pocz=-1.0;
    VI akt;
    REP(j,SIZE(pom))
    {
      if (a==0) pocz=pom[j].FI;
      if (pom[j].SE<0) --a; else ++a;
      if (pom[j].SE>0) akt.PB(pom[j].SE-1);
      if (a==0) pom2.PB(MP(MP(pocz,pom[j].FI),akt));
    }
    assert(!a);

    int ost=0;
    FOR(j,1,SIZE(pom2)-1)
      if (pom2[ost].FI.SE+s>=pom2[j].FI.FI)
      {
        pom2[ost].FI.SE=pom2[j].FI.SE;
        REP(k,SIZE(pom2[j].SE)) pom2[ost].SE.PB(pom2[j].SE[k]);
        pom2[j].SE.clear();
      } else
      {
        ost=j;
      }
    REP(j,SIZE(pom2)) if (!pom2[j].SE.empty()) pom3.PB(pom2[j]);

    if (i==0)
    {
      if (pom3.empty() || pom3[0].FI.FI>s) return false;
    }

    //if (i==1) celmin=N;
    REP(j,SIZE(pom3))
    {
      REP(k,SIZE(pom3[j].SE)) node[i][pom3[j].SE[k]]=N;
      kraw[N]=pom3[j].SE;
      ++N;
    }
    //if (i==1) celmax=N;
  }

  czy=false;
  REP(i,N) vis[i]=false;
  dfs(0,0);
  return czy;
}

void mymain()
{
  scanf("%d%d",&n,&s);
  REP(i,n)
  {
    scanf("%d%d%d%d%d%d",&asteroidy[i].x,&asteroidy[i].y,&asteroidy[i].z,&predkosci[i].x,&predkosci[i].y,&predkosci[i].z);
  }
  ld lo=0.0,hi=dist(asteroidy[0],asteroidy[1]);
  //wypisz(lo); wypisz(hi);
  REP(ii,30)
  {
    ld sr=(lo+hi)/2;
    //wypisz(sr); puts("");
    if (dasie(sr)) hi=sr; else lo=sr;
  }
  printf("%.8Lf\n",hi);
}

int main()
{
  int ILE;
  scanf("%d",&ILE);
  FOR(iii,1,ILE)
  {
    printf("Case #%d: ",iii);
    fprintf(stderr,"Case #%d:\n",iii);
    mymain();
  }
  return 0;
}
