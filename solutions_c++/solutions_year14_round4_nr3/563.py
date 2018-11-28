#include <iostream>
#include <vector>
#include <queue>
using namespace std;
const int kx[4] = {0, 0, 1, -1};
const int ky[4] = {1, -1, 0, 0};

const int maxint=1<<28,N=100010, M=N * 10;
inline int min(int i,int j)
{
  return (i>=j?j:i);
}
class edge
{
 public :
  int u,v,c,flow;
  edge(int cu,int cv,int cc) :u(cu),v(cv),c(cc),flow(0) {};
  int other(int p) { return p==u?v:u; }
  int cap(int p) { return p==u?c-flow:flow; }
  void add(int p,int f) {flow+=(p==u?f:-f);};
};
vector <edge> eg;
edge *net[M*2];
int nu[N+1],st,en,n,h[N],hn[N*2],ee[N],cur[N];
void innet()
{
  int l;
  memset(nu,0,sizeof(nu));
  memset(ee,0,sizeof(ee));
  memset(h,0,sizeof(h));
  memset(hn,0,sizeof(hn));
  for (l=eg.size()-1;l>=0;l--) nu[eg[l].u+1]++,nu[eg[l].v+1]++;
  for (l=2;l<=n;l++) nu[l]+=nu[l-1];
  for (l=eg.size()-1;l>=0;l--)
  {
    net[nu[eg[l].u]++]=&eg[l];
    net[nu[eg[l].v]++]=&eg[l];
  }
  for (l=n-1;l>0;l--) nu[l]=nu[l-1]; nu[0]=0;
  hn[n]=1; hn[0]=n-1;
  h[st]=n; ee[st]=maxint;
  for (l=0;l<n;l++) cur[l]=nu[l+1]-1;
}
void push(int u)
{
  edge *p=net[cur[u]];
  int ex=min(p->cap(u),ee[u]),v=p->other(u);
  p->add(u,ex); ee[u]-=ex; ee[v]+=ex;
}
void gap(int k)
{
  if (hn[k]||k>=n+1) return ;
  int i;
  for (i=0;i<n;i++)
    if (h[i]>k&&h[i]<=n&&i!=st) h[i]=n+1;
  for (i=k+1;i<=n;i++)
  {
    hn[n+1]+=hn[i]; hn[i]=0;
  }
}
void relable(int u)
{
  int i,mh=n*2,oh=h[u];
  for (i=nu[u+1]-1;i>=nu[u];i--)
    if (net[i]->cap(u)) mh=min(mh,h[net[i]->other(u)]+1);
  hn[mh]++; hn[oh]--;
  h[u]=mh; cur[u]=nu[u+1]-1;
  gap(oh);
}
int maxflow()
{
  queue <int> q;
  int u,p;
  q.push(st);
  while (!q.empty())
  {
    u=q.front(); q.pop();
    for (;cur[u]>=nu[u]&&ee[u]>0;cur[u]--)
    { 
      p=net[cur[u]]->other(u);
      if (u==st||h[u]==h[p]+1)
      {
        if (p!=en&&!ee[p]) q.push(p);
        push(u);
      }
    }
    if (ee[u]&&u!=st) 
    {
      relable(u);
      q.push(u);
    }
  }
  return ee[en];
}

bool mark[100][500];
void Add(int i, int j) {
  eg.push_back(edge(i, j, 1));
}
int main()
{
  int tc,l,i,j;
  scanf("%d",&tc);
  for (int cas = 1; cas <= tc; ++cas) {
    eg.clear();
    int nw, nh, nb;
    scanf("%d%d%d", &nw, &nh, &nb);
    memset(mark, 0, sizeof(mark));
    while (nb--) {
      int x0, y0, x1, y1;
      scanf("%d%d%d%d", &x0, &y0, &x1, &y1);
      for (int i = x0; i <= x1; ++i)
        for (int j = y0; j <= y1; ++j) {
          mark[i][j] = true;
        }
    }
    n = nw * nh * 2 + 2;
    for (int i = 0; i < nw; ++i) {
      if (!mark[i][0]) Add(0, i * nh * 2 + 1);
      if (!mark[i][nh - 1]) Add( (i * nh + nh - 1) * 2 + 2, n - 1);
    }
    int x ,y;
    for (int i = 0; i < nw; ++i)
      for (int j = 0; j < nh; ++j) {
        if (mark[i][j]) continue;
        Add((i * nh + j) * 2 + 1, (i * nh + j) * 2 + 2);
        for (int k = 0; k < 4; ++k) {
          x = i + kx[k];
          y = j + ky[k];
          if (x >= 0 && y >= 0 && x < nw && y < nh && !mark[x][y]) {
            Add( (i * nh + j) * 2 + 2, (x * nh + y) * 2 + 1);
          }
        }
      }
    // printf("%d\n", (int)eg.size());
    //输入边
    st=0; en=n-1;
    innet();
    int ans = maxflow();
    printf("Case #%d: %d\n", cas, ans);
  }
  return 0;
}
