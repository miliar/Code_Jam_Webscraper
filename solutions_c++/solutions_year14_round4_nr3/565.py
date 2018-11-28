#include <cstdio>
#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <functional>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef map<int,int> mii;
typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef vector<string> vs;

#define rep(i,n) for(int i=0;i<(n);i++)
#define forup(i,a,b) for(int i=(a);i<(b);i++)
#define fordn(i,a,b) for(int i=(a);i>(b);i--)
#define all(x) x.begin(),x.end()
#define permute(x) next_permutation(all(x))
#define gi(x) scanf("%d",&x)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second

const int max_v=100050;
const int inv=int(1e8);

int s,t;
int v;
struct adjlel
{
  int nb;
  int c;
  int f;
  int rix;
  adjlel(){}
  adjlel(int nb_, int c_, int f_, int rix_){ nb=nb_; c=c_; f=f_; rix=rix_; }
};
vector<adjlel> adjl[max_v];

bool visited[max_v];
int par[max_v]; int parixvt[max_v]; int vtixpar[max_v];
int aug[max_v];
queue<int> Q;
int augval;
 
bool augmentingpath()
{
  fill(visited, visited+v, false);
  while(!Q.empty())
  Q.pop();
  
  visited[s]=true;
  par[s]=s;
  Q.push(s);
  aug[s]=inv;
  
  int vt; adjlel vtnbr;
  while(!Q.empty())
  {
    vt=Q.front();
    Q.pop();
    
    for(int i=0; i<adjl[vt].size(); ++i)
    {
      vtnbr=adjl[vt][i];
      if((not visited[vtnbr.nb]) and ((vtnbr.c-vtnbr.f)>0))
      {
        visited[vtnbr.nb]=true;
        Q.push(vtnbr.nb);
        par[vtnbr.nb]=vt; parixvt[vtnbr.nb]=i; vtixpar[vtnbr.nb]=vtnbr.rix;
        aug[vtnbr.nb]=min(aug[vt],vtnbr.c-vtnbr.f);

        if(vtnbr.nb==t)
        {
          augval=aug[t];
        return true; 
        }
      }
    }
  }

  return false;
}
 
void augmentflow(int vt)
{
  if(par[vt]!=vt)
  {
    adjl[par[vt]][parixvt[vt]].f+=augval;
    adjl[vt][vtixpar[vt]].f-=augval;
    augmentflow(par[vt]);
  }
}

int maxflow;
void findmaxflow()
{
  maxflow=0;

  rep(k,v)
  rep(j,adjl[k].size())
    adjl[k][j].f=0;

  while(augmentingpath())
  {
    maxflow+=augval;
    augmentflow(t);
  }
}

// End of Codechunk

// To add an edge between nb and vt
void add_edge(int vt,int nb)
{
  //printf("%d %d\n",vt,nb);
  adjl[vt].pb(adjlel(nb,1,0,adjl[nb].size()));
  adjl[nb].pb(adjlel(vt,0,0,adjl[vt].size()-1));
}

const int max_n=510;
int T;
int w,h,b;
bool grid[max_n][max_n];
int X0,Y0,X1,Y1;

int inix(int x,int y) {
  return (y*w+x);
}

int outix(int x,int y) {
  return (w*h+y*w+x);
}

int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};

void init() {
  rep(i,max_n)
    rep(j,max_n)
      grid[i][j]=false;
  rep(i,max_v) {
    adjl[i].clear();
    visited[i]=par[i]=parixvt[i]=vtixpar[i]=aug[i]=0;
  }
}

int main() {
  gi(T);
  for(int z=1;z<=T;z++) {
    printf("Case #%d: ",z);
    init();
    gi(w); gi(h); gi(b);
    rep(i,b) {
      gi(X0); gi(Y0); gi(X1); gi(Y1);
      forup(x,X0,X1+1)
        forup(y,Y0,Y1+1)
          grid[x][y]=true;
    }
    rep(x,w)
      rep(y,h) {
        if(grid[x][y]) continue;
        rep(d,4) {
          int nx=x+dx[d],ny=y+dy[d];
          if(0<=nx and nx<w and 0<=ny and ny<h and (not grid[nx][ny]))
            add_edge(outix(x,y),inix(nx,ny));
        }
        add_edge(inix(x,y),outix(x,y));
      }
    v=2*w*h+2;
    s=2*w*h;
    t=s+1;
    rep(i,w) {
      if(not grid[i][0]) add_edge(s,inix(i,0));
      if(not grid[i][h-1]) add_edge(outix(i,h-1),t);
    }
    findmaxflow();
    printf("%d\n",maxflow);
  }
  return 0;
}
