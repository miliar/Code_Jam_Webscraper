#include<bits/stdc++.h>
#include<unistd.h>
using namespace std;
#define FZ(n) memset((n),0,sizeof(n))
#define FMO(n) memset((n),-1,sizeof(n))
#define F first
#define S second
#define PB push_back
#define ALL(x) begin(x),end(x)
#define SZ(x) ((int)(x).size())
#define IOS ios_base::sync_with_stdio(0); cin.tie(0)
template<typename A, typename B>
ostream& operator <<(ostream &s, const pair<A,B> &p) {
  return s<<"("<<p.first<<","<<p.second<<")";
}
template<typename T>
ostream& operator <<(ostream &s, const vector<T> &c) {
  s<<"[ ";
  for (auto it : c) s << it << " ";
  s<<"]";
  return s;
}
// Let's Fight!

typedef pair<int, int> pii;
typedef pair<int, pii> pip;

const int MAXN = 1010;

int N;
int S;
int x[MAXN], y[MAXN], z[MAXN], vx[MAXN], vy[MAXN], vz[MAXN];
int root[MAXN];

void djInit()
{
  for(int i=0; i<N; i++)
    root[i] = i;
}

int djFind(int v)
{
  if(root[v] == v) return v;
  return root[v] = djFind(root[v]);
}

void djUnion(int u, int v)
{
  int pu = djFind(u), pv = djFind(v);
  if(pu != pv)
  {
    root[pu] = pv;
  }
}

double calc()
{
  vector<pip> edge;

  for(int i=0; i<N; i++)
  {
    for(int j=i+1; j<N; j++)
    {
      int dx = x[i] - x[j], dy = y[i] - y[j], dz = z[i] - z[j];
      int dis = dx * dx + dy * dy + dz * dz;
      edge.PB({dis, {i, j}});
    }
  }
  sort(ALL(edge));

  djInit();
  for(auto e: edge)
  {
    djUnion(e.S.F, e.S.S);
    if(djFind(0) == djFind(1))
      return sqrt(e.F);
  }
  return 0;
}

int main() {
  IOS;

  int T;
  cin>>T;
  for(int t=1; t<=T; t++)
  {
    cin>>N>>S;
    for(int i=0; i<N; i++)
    {
      cin>>x[i]>>y[i]>>z[i]>>vx[i]>>vy[i]>>vz[i];
    }

    double ans = calc();
    cout<<"Case #"<<t<<": "<<fixed<<setprecision(10)<<ans<<endl;
  }

  return 0;
}
