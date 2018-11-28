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

const int MAXN = 106;

int R, C, V;
int arr[MAXN];
bool dir[MAXN][MAXN];
bool air[MAXN][MAXN];
vector<int> edge[MAXN];
int label[MAXN];
int vis[MAXN];

void dfs(int v, int c)
{
  if(vis[v] != -1) return;
  vis[v] = c;
  for(auto u: edge[v])
    dfs(u, c);
}

bool check()
{
  V = (R+1) * C + R * (C+1);
  for(int i=0; i<V; i++)
    edge[i].clear();

  for(int i=0; i<R; i++)
  {
    for(int j=0; j<C; j++)
    {
      int a = (R+1)*C + i * (C+1) + j;
      int c = a + 1;
      int b = i * C + j;
      int d = b + C;

      if(dir[i][j])
      {
        edge[a].PB(d);
        edge[d].PB(a);
        edge[b].PB(c);
        edge[c].PB(b);
      }
      else
      {
        edge[a].PB(b);
        edge[b].PB(a);
        edge[c].PB(d);
        edge[d].PB(c);
      }
    }
  }

  for(int i=0; i<C; i++)
  {
    label[i] = i;
    label[R+C+(C-1-i)] = R * C + i; 
  }
  for(int i=0; i<R; i++)
  {
    label[C+i] = (R+1)*C + i * (C+1) + C;
    label[R+C+C+(R-1-i)] = (R+1)*C + i * (C+1);
  }

  for(int i=0; i<V; i++)
    vis[i] = -1;

  for(int i=0; i<V; i++)
    if(vis[i] == -1)
      dfs(i, i);

  //for(int i=0; i<V; i++) cout<<vis[i]<<" ";cout<<endl;
  //for(int i=0; i<2*(R+C); i++) cout<<label[arr[i]]<<" ";cout<<endl;
  //for(int i=0; i<2*(R+C); i++) cout<<vis[label[i]]<<" ";cout<<endl;

  for(int i=0; i<R+C; i++)
  {
    int a = label[arr[2*i]], b = label[arr[2*i+1]];
    //cout<<a<<" / "<<b<<endl;
    if(vis[a] != vis[b]) return false;
  }
  //cout<<"OK"<<endl;
  //for(int i=0; i<R; i++){for(int j=0; j<C; j++) cout<<dir[i][j];cout<<endl;}
  return true;
}

int main() {
  IOS;

  int T;
  cin>>T;
  for(int t=1; t<=T; t++)
  {
    cin>>R>>C;
    for(int i=0; i<2*(R+C); i++)
    {
      cin>>arr[i];
      arr[i]--;
    }

    bool ans = false;

    for(int i=0; i<(1<<(R*C)); i++)
    {
      for(int j=0; j<R; j++)
      {
        for(int k=0; k<C; k++)
        {
          dir[j][k] = !!(i&(1<<(j*C+k)));
        }
      }

      if(check())
      {
        //cout<<"OK"<<endl;
        //for(int j=0; j<R; j++){for(int k=0; k<C; k++) cout<<dir[j][k];cout<<endl;}
        ans = true;
        for(int j=0; j<R; j++)
          for(int k=0; k<C; k++)
            air[j][k] = dir[j][k];
      }
    }

    cout<<"Case #"<<t<<":"<<endl;
    if(ans)
    {
      for(int i=0; i<R; i++)
      {
        for(int k=0; k<C; k++)
          cout<<(air[i][k] ? '\\' : '/');
        cout<<endl;
      }
    }
    else
      cout<<"IMPOSSIBLE"<<endl;
  }
  return 0;
}
