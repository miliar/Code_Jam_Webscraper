#include <algorithm>
#include <bitset>
#include <cmath> 
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <utility>
#include <vector>
#define PB push_back
#define MP make_pair
#define LB lower_bound
#define UB upper_bound
#define FT first
#define SD second
#define VI vector<int> 
#define MII map<int,int>
#define SI set<int>
#define rep(i, n) for (int i = 0; i < n; i++)
typedef long long LL;
typedef long double LD;
const int INF = 0x7FFFFFFF;
const LL LINF = 0x7FFFFFFFFFFFFFFFll;
const int u = 5010, w = 200010, c = 100;

const int Ni = 5111;
 const int MAX = 1<<26;

using namespace std;

 struct Edge{
     int u,v,c;
     int next;
 }edge[200*Ni];
 int edn;//边数
 int p[Ni];//父亲
 int d[Ni];
 int sp,tp;//原点，汇点
int front[Ni];
int n, m, total, 
A, B;
char s[1010][12];
vector<pair<int, int> > like;
map<string, int> h;
bool a[Ni], b[Ni];

 void addedge(int u,int v,int c)
 {
     edge[edn].u=u; edge[edn].v=v; edge[edn].c=c;
     edge[edn].next=p[u]; p[u]=edn++;
     edge[edn].u=v; edge[edn].v=u; edge[edn].c=0;
     edge[edn].next=p[v]; p[v]=edn++;
 }
 int bfs()
 {
     queue <int> q;
     memset(d,-1,sizeof(d));
     d[sp]=0;
     q.push(sp);
     while(!q.empty())
     {
         int cur=q.front();
         q.pop();
         for(int i=p[cur];i!=-1;i=edge[i].next)
         {
             int u=edge[i].v;
             if(d[u]==-1 && edge[i].c>0)
             {
                 d[u]=d[cur]+1;
                 q.push(u);
             }
         }
     }
     return d[tp] != -1;
 }
 int dfs(int a,int b)
 {
     int r=0;
     if(a==tp)return b;
     for(int i=p[a];i!=-1 && r<b;i=edge[i].next)
     {
         int u=edge[i].v;
         if(edge[i].c>0 && d[u]==d[a]+1)
         {
             int x=min(edge[i].c,b-r);
             x=dfs(u,x);
             r+=x;
             edge[i].c-=x;
             edge[i^1].c+=x;
         }
     }
     if(!r)d[a]=-2;
     return r;
 }

 int dinic(int sp,int tp)
 {
     int totalal=0,t;
     while(bfs())
     {
         while(t=dfs(sp,MAX))
         totalal+=t;
     }
     return totalal;
 }


int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int casenum;
	scanf("%d", &casenum);
	for (int z = 1;z <= casenum;z++)
	{

         edn=0;//初始化
         memset(p,-1,sizeof(p));
         sp=1;tp=n;
		scanf("%d", &n);
		like.clear(); 
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		h.clear(); 
		m = 0;
		for (int i = 1;i <= n;i++){
			int cnt = 0;
			do {
				scanf("%s", s[++cnt]);
				if (!h[s[cnt]]) 
					h[s[cnt]] = ++m;
				if (i == 1) a[h[s[cnt]]] = 1;
				if (i == 2) b[h[s[cnt]]] = 1;
			} while (getchar() == ' ');
			if (i > 2){
				for (int i = 1;i < cnt;i++)
					for (int j = i + 1;j <= cnt;j++)
						like.PB(MP(h[s[i]], h[s[j]]));
			}
		}
		memset(front, 0, sizeof(front));
		sp = 0;
		tp = 2 * m + 1;
		total = 1;
		for (int i = 0;i < like.size();i++){
			int x = like[i].FT, y = like[i].SD;
			addedge(m + x, y, INF), addedge(m + y, x, INF);
		}
		for (int i = 1;i <= m;i++){
			addedge(sp, i, b[i] ? INF : c);
			addedge(i, m + i, c + 1);
			addedge(m + i, tp, a[i] ? INF : c);
		}
		
		int mf = dinic(sp, tp);
		printf("Case #%d: %d\n", z, mf - c*m);
	}
	return 0;
}