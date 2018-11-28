#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define REPR(i,n) for (int i=(int)(n)-1;i>=0;--i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
#define valid(y,x,h,w) (0<=y&&y<h&&0<=x&&x<w)
#define tpl(...) make_tuple(__VA_ARGS__)
const int INF = 0x3f3f3f3f;
const double EPS = 1e-8;
const double PI = acos(-1);
const int dy[] = {-1,0,1,0};
const int dx[] = {0,1,0,-1};
typedef long long ll;
typedef pair<int,int> pii;
template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T>bool chmin(T &a, const T &b) { if (b<a) { a=b; return 1; } return 0; }
template<typename Ch,typename Tr,typename C,typename=decltype(begin(C()))>basic_ostream<Ch,Tr>& operator<<(basic_ostream<Ch,Tr>&os,
const C& c){os<<'[';for(auto i=begin(c);i!=end(c);++i)os<<(i==begin(c)?"":" ")<<*i;return os<<']';}
template<class S,class T>ostream&operator<<(ostream &o,const pair<S,T>&t){return o<<'('<<t.first<<','<<t.second<<')';}
template<int N,class Tp>void output(ostream&,const Tp&){}
template<int N,class Tp,class,class ...Ts>void output(ostream &o,const Tp&t){if(N)o<<',';o<<get<N>(t);output<N+1,Tp,Ts...>(o,t);}
template<class ...Ts>ostream&operator<<(ostream&o,const tuple<Ts...>&t){o<<'(';output<0,tuple<Ts...>,Ts...>(o,t);return o<<')';}
template<class T>void output(T t,char z=10){if(t<0)t=-t,putchar(45);int c[20];
int k=0;while(t)c[k++]=t%10,t/=10;for(k||(c[k++]=0);k;)putchar(c[--k]^48);putchar(z);}
template<class T>void outputs(T t){output(t);}
template<class S,class ...T>void outputs(S a,T...t){output(a,32);outputs(t...);}
template<class T>void output(T *a,int n){REP(i,n)cout<<a[i]<<(i!=n-1?',':'\n');}
template<class T>void output(T *a,int n,int m){REP(i,n)output(a[i],m);}
template<class T>bool input(T &t){int n=1,c;for(t=0;!isdigit(c=getchar())&&~c&&c-45;);
if(!~c)return 0;for(c-45&&(n=0,t=c^48);isdigit(c=getchar());)t=10*t+c-48;t=n?-t:t;return 1;}
template<class S,class ...T>bool input(S&a,T&...t){input(a);return input(t...);}
template<class T>bool inputs(T *a, int n) { REP(i,n) if(!input(a[i])) return 0; return 1;}

// 集合にデータを入れたい時
template <class T>
struct UnionFind {
  vector<int> data;
  vector<T> val;
  UnionFind(int size) : data(size, -1), val(size) { }
  bool unionSet(int x, int y, T v) {
    x = root(x); y = root(y);
    if (x != y) {
      if (data[y] < data[x]) swap(x, y);
      data[x] += data[y]; data[y] = x;
      val[x] = v;
    }
    return x != y;
  }
  bool findSet(int x, int y) {
    return root(x) == root(y);
  }
  int root(int x) {
    return data[x] < 0 ? x : data[x] = root(data[x]);
  }
  int size(int x) {
    return -data[root(x)];
  }
  T &value(int x) {
    return val[root(x)];
  }
};

string casestr;
const int N = 1000000;
int s[1000001];
int m[1000001];
bool dead[N];
bool used[N];
// int deadcnt[N];

vector<int> lst[N+1];
vector<int> g[N];

int dfs(int v) {
  if (!used[v] || dead[v]) return 0;
  dead[v] = 1;
  int res = 1;
  for (int u : g[v]) {
    res += dfs(u);
  }
  return res;
}

void solve() {
  int n,d;
  cin >> n >> d;
  int s0,as,cs,rs;
  input(s0,as,cs,rs);
  int m0,am,cm,rm;
  input(m0,am,cm,rm);
  s[0] = s0;
  m[0] = m0;
  REP(i,n-1) {
    s[i+1] = ((ll)s[i]*as+cs) % rs;
    m[i+1] = ((ll)m[i]*am+cm) % rm;
  }
  m[0] = -1;
  for (int i=1; i<n; ++i) m[i] %= i;
  REP(i,N+1)lst[i].clear();
  REP(i,n) g[i].clear();
  REP(i,n) {
    lst[s[i]].push_back(i);
    if (i)
      g[m[i]].push_back(i);
  }

  //
  REP(i,n) {
    used[i]=0;
    dead[i]=0;
    // deadcnt[i]=0;
  }
  UnionFind<int> uf(n);
  int ans = 0;
  for (int i=max(0,s[0]-d); i<=min(1000000,s[0]+d); ++i) {
    // add i
    for (int v : lst[i]) {
      if (m[v] != -1) {
        // cout << tpl("add", v) << endl;
        if (!dead[m[v]]) {
          // int t = deadcnt[uf.root(v)];
          uf.unionSet(v,m[v],uf.value(v)+uf.value(m[v]));
          // deadcnt[uf.root(v)] += t;
          used[v] = 1;
        }
      }
    }
    // remove i-d-1
    if (i>=s[0]+1 && i-d-1>=0) {
      for (int v : lst[i-d-1]) {
        int cnt = dfs(v);
        // cout << tpl("remove", v, cnt) << endl;
        uf.value(v) += cnt;
        // deadcnt[uf.root(v)] += cnt;
      }
    }
    // cout << tpl(uf.size(0), deadcnt[uf.root(0)]) << endl;
    int tmp = uf.size(0) - uf.value(0);
    chmax(ans, tmp);
  }
  cout << casestr << " " << ans << endl;
}

int main() {
  int T;
  cin >> T;
  REP(cs,T) {
    casestr = "Case #" + to_string(cs+1) + ":";
    solve();
  }
}
