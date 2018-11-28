#define DEBUG 1

#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>
using namespace std;

#define LL long long
#define LD long double
#define PR pair<int,int>

#define Fox(i,n) for (i=0; i<n; i++)
#define Fox1(i,n) for (i=1; i<=n; i++)
#define FoxI(i,a,b) for (i=a; i<=b; i++)
#define FoxR(i,n) for (i=(n)-1; i>=0; i--)
#define FoxR1(i,n) for (i=n; i>0; i--)
#define FoxRI(i,a,b) for (i=b; i>=a; i--)
#define Foxen(i,s) for (i=s.begin(); i!=s.end(); i++)
#define Min(a,b) a=min(a,b)
#define Max(a,b) a=max(a,b)
#define Sz(s) int((s).size())
#define All(s) (s).begin(),(s).end()
#define Fill(s,v) memset(s,v,sizeof(s))
#define pb push_back
#define mp make_pair
#define x first
#define y second

template<typename T> T Abs(T x) { return(x<0 ? -x : x); }
template<typename T> T Sqr(T x) { return(x*x); }
string plural(string s) { return(Sz(s) && s[Sz(s)-1]=='x' ? s+"en" : s+"s"); }

const int INF = (int)1e9;
const double EPS = 1e-9;
const LD PI = acos(-1.0);

#define MOD 1000000007

#if DEBUG
#define GETCHAR getchar
#else
#define GETCHAR getchar_unlocked
#endif

bool Read(int &x)
{
	char c,r=0,n=0;
	x=0;
		for(;;)
		{
			c=GETCHAR();
				if ((c<0) && (!r))
					return(0);
				if ((c=='-') && (!r))
					n=1;
				else
				if ((c>='0') && (c<='9'))
					x=x*10+c-'0',r=1;
				else
				if (r)
					break;
		}
		if (n)
			x=-x;
	return(1);
}

struct Edge {
  int from, to, cap, flow, index;
  Edge(int from, int to, int cap, int flow, int index) :
    from(from), to(to), cap(cap), flow(flow), index(index) {}
};

struct Dinic {
  int N;
  vector<vector<Edge> > G;
  vector<Edge *> dad;
  vector<int> Q;
  
  Dinic(int N) : N(N), G(N), dad(N), Q(N) {}
  
  void AddEdge(int from, int to, int cap) {
    G[from].push_back(Edge(from, to, cap, 0, G[to].size()));
    if (from == to) G[from].back().index++;
    G[to].push_back(Edge(to, from, 0, 0, G[from].size() - 1));
  }

  long long BlockingFlow(int s, int t) {
    fill(dad.begin(), dad.end(), (Edge *) NULL);
    dad[s] = &G[0][0] - 1;
    
    int head = 0, tail = 0;
    Q[tail++] = s;
    while (head < tail) {
      int x = Q[head++];
      for (int i = 0; i < G[x].size(); i++) {
	Edge &e = G[x][i];
	if (!dad[e.to] && e.cap - e.flow > 0) {
	  dad[e.to] = &G[x][i];
	  Q[tail++] = e.to;
	}
      }
    }
    if (!dad[t]) return 0;

    long long totflow = 0;
    for (int i = 0; i < G[t].size(); i++) {
      Edge *start = &G[G[t][i].to][G[t][i].index];
      int amt = INF;
      for (Edge *e = start; amt && e != dad[s]; e = dad[e->from]) {
	if (!e) { amt = 0; break; }
	amt = min(amt, e->cap - e->flow);
      }
      if (amt == 0) continue;
      for (Edge *e = start; amt && e != dad[s]; e = dad[e->from]) {
	e->flow += amt;
	G[e->to][e->index].flow -= amt;
      }
      totflow += amt;
    }
    return totflow;
  }

  long long GetMaxFlow(int s, int t) {
    long long totflow = 0;
    while (long long flow = BlockingFlow(s, t))
      totflow += flow;
    return totflow;
  }
};

int H,W;
bool good;
bool G[2005][1005];

void rec(int y,int x,int d)
{
		if (y==H)
		{
			good=1;
			return;
		}
	G[y][x]=1;
		if ((d==0) || (d==1))
		{
			if ((y>0) && (!G[y-1][x])) //down
				rec(y-1,x,2);
			if (good)
				return;
			if ((x>0) && (!G[y][x-1])) //left
				rec(y,x-1,1);
			if (good)
				return;
			if ((y==H-1) || (!G[y+1][x])) //up
				rec(y+1,x,0);
			if (good)
				return;
			if ((x<W-1) && (!G[y][x+1])) //right
				rec(y,x+1,3);
		}
		else
		{
			if ((y==H-1) || (!G[y+1][x])) //up
				rec(y+1,x,0);
			if (good)
				return;
			if ((x<W-1) && (!G[y][x+1])) //right
				rec(y,x+1,3);
			if (good)
				return;
			if ((y>0) && (!G[y-1][x])) //down
				rec(y-1,x,2);
			if (good)
				return;
			if ((x>0) && (!G[y][x-1])) //left
				rec(y,x-1,1);
		}
}

int main()
{
		if (DEBUG)
			freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,t;
	int M,B;
	int i,j,k,a,b,tot;
	int y1[1000],y2[1000],x1[1000],x2[1000],comp[2005];
	Read(T);
		Fox1(t,T)
		{
			printf("Case #%d: ",t);
			Read(W),Read(M),Read(B);
			H=0;
				Fox(i,B)
				{
					Read(x1[i]),Read(y1[i]),Read(x2[i]),Read(y2[i]);//,y2[i]++;
					comp[H++]=y1[i];
					comp[H++]=y2[i];
				}
			sort(comp,comp+H);
			H=unique(comp,comp+H)-comp;
			Fill(G,0);
			H=M+1;
				Fox(i,B)
				{
					/*y1[i]=lower_bound(comp,comp+H,y1[i])-comp;
					y2[i]=lower_bound(comp,comp+H,y2[i])-comp-1;*/
						FoxI(a,y1[i],y2[i])
							FoxI(b,x1[i],x2[i])
								G[a][b]=1;
				}
			int V;
			Dinic gr(V=H*W*2+2);
				if (!H)
					continue;
				Fox(j,W)
				{
					gr.AddEdge(V-2,0*W+j,1);
					gr.AddEdge(H*W+(H-1)*W+j,V-1,1);
				}
				Fox(i,H)
					Fox(j,W)
						if (!G[i][j])
							gr.AddEdge(i*W+j,H*W+i*W+j,1);
			int my[4]={-1,1,0,0};
			int mx[4]={0,0,-1,1};
				Fox(i,H)
					Fox(j,W)
						Fox(k,4)
						{
							a=i+my[k];
							b=j+mx[k];
								if ((a>=0) && (a<H) && (b>=0) && (b<W))
									gr.AddEdge(H*W+i*W+j,a*W+b,1);
						}
			int ans=gr.GetMaxFlow(V-2,V-1);
			/*printf("\n");
				Fox(a,H)
				{
						Fox(b,W)
							printf("%c",G[a][b]?'#':'.');
					printf("\n");
				}
			printf("\n");*/
			tot=0;
				Fox(i,W)
					if (!G[0][i])
					{
						good=0;
						rec(0,i,0);
							if (good)
								tot++;
					}
			printf("%d\n",tot);
				if (tot!=ans)
				{
					printf("SHOULD BE %d\n",ans);
				}
		}
	return(0);
}