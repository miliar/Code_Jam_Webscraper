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

const int MAXN = 5;

int N;
int arr[MAXN][MAXN];
int add[MAXN][MAXN];
int ord[MAXN];
bool used[MAXN];

bool dfs(int lv)
{
  if(lv >= N) return true;
  int v = ord[lv];
  bool any = false;
  for(int i=0; i<N; i++)
  {
    if(used[i] or !add[v][i]) continue;
    any = true;
    used[i] = true;
    if(!dfs(lv+1)) return false;
    used[i] = false;
  }
  if(!any)
  {
    //cout<<lv<<" GG"<<endl;
    return false;
  }
  return true;
}

bool check()
{
  //for(int i=0; i<N; i++) for(int j=0; j<N; j++) cout<<add[i][j]; cout<<endl;

  for(int i=0; i<N; i++)
    ord[i] = i;

  do
  {
    FZ(used);
    bool res = dfs(0);
    if(!res) return false;
  }while(next_permutation(ord, ord+N));
  return true;
}

int main() {
  IOS;

  int T;
  cin>>T;
  for(int t=1; t<=T; t++)
  {
    cin>>N;
    for(int i=0; i<N; i++)
    {
      string s;
      cin>>s;
      for(int j=0; j<N; j++)
      {
        arr[i][j] = (s[j] == '1');
      }
    }

    int ans = 12345678;
    for(int i=0; i<(1<<(N*N)); i++)
    {
      bool ok = true;
      int cst = 0;
      for(int j=0; j<N; j++)
      {
        for(int k=0; k<N; k++)
        {
          add[j][k] = !!(i&(1<<(j*N+k)));
          if(!add[j][k] and arr[j][k])
            ok = false;
          if(add[j][k] and !arr[j][k])
            cst++;
        }
      }
      if(!ok) continue;
      
      if(check())
        ans = min(ans, cst);
    }

    cout<<"Case #"<<t<<": "<<ans<<endl;
  }
  return 0;
}
