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

const int MAXN = 105;
const int Q = 10000;

int N, M;
char alp[MAXN];
int par[MAXN];
vector<int> ch[MAXN];
string cool[MAXN];
int wei[MAXN];

void dfs(int v)
{
  wei[v] = 1;
  for(auto c: ch[v])
  {
    dfs(c);
    wei[v] += wei[c];
  }
}

string sample()
{
  vector<int> cur;
  for(int i=1; i<=N; i++)
    if(par[i] == 0)
      cur.PB(i);

  string s;
  for(int i=0; i<N; i++)
  {
    int tot = N - i;
    int sz = SZ(cur);
    int r = rand() % tot;

    int res = -1;
    for(int j=0; j<sz; j++)
    {
      int x = cur[j];
      if(r < wei[x])
      {
        res = x;
        swap(cur[j], cur.back());
        cur.pop_back();
        break;
      }
      r -= wei[x];
    }

    s.PB(alp[res]);
    for(auto c: ch[res])
      cur.PB(c);
  }

  return s;
}

vector<double> calc()
{
  for(int i=1; i<=N; i++)
    if(par[i] != 0)
      ch[par[i]].PB(i);

  for(int i=1; i<=N; i++)
    if(par[i] == 0)
      dfs(i);

  vector<double> ret;
  ret.resize(M);

  for(int i=0; i<Q; i++)
  {
    string s = sample();
    for(int j=0; j<M; j++)
    {
      if(s.find(cool[j]) != string::npos)
        ret[j] += 1;
    }
  }

  for(int i=0; i<M; i++)
    ret[i] /= Q;

  return ret;
}

int main() {
  IOS;

  int T;
  cin>>T;
  for(int t=1; t<=T; t++)
  {
    cin>>N;
    for(int i=1; i<=N; i++)
      cin>>par[i];
    for(int i=1; i<=N; i++)
    {
      wei[i] = 0;
      ch[i].clear();
    }
    string s;
    cin>>s;
    for(int i=1; i<=N; i++)
      alp[i] = s[i-1];
    cin>>M;
    for(int i=0; i<M; i++)
      cin>>cool[i];

    vector<double> vans = calc();
    cout<<"Case #"<<t<<":";
    cout<<fixed<<setprecision(3);
    for(auto x: vans)
      cout<<" "<<x;
    cout<<endl;
  }
  return 0;
}
