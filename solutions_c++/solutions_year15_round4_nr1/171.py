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

string casestr;

vector<int> g[10000];
vector<int> rg[10000];
string s[100];
int id[100][100];
int nr[100];
int nc[100];
pii p[100000];

void solve() {
  int h,w;
  input(h,w);
  int n = 0;
  REP(i,100)nr[i]=nc[i]=0;
  REP(i,h) {
    cin>>s[i];
    REP(j,w) {
      if (s[i][j] != '.') {
        p[n] = pii(i,j);
        id[i][j] = n++;
        nr[i]++;
        nc[j]++;
      }
    }
  }
  REP(i,n) {
    g[i].clear();
  }
  REP(i,h) {
    REP(j,w) {
      if (s[i][j] != '.') {
        int ii=i,jj=j;
        int d = string("^>v<").find(s[i][j]);
        ii += dy[d];
        jj += dx[d];
        while(valid(ii,jj,h,w)) {
          if (s[ii][jj] != '.') {
            g[id[i][j]].push_back(id[ii][jj]);
            break;
          }
          ii += dy[d];
          jj += dx[d];
        }
      }
    }
  }
  int ans = 0;
  REP(i,n) {
    if (g[i].size() == 0) {
      int y = p[i].first;
      int x = p[i].second;
      if (nr[y]>=2||nc[x]>=2) {
        ans++;
      } else {
        ans = -1;
        break;
      }
    }
  }
  if (ans >= 0) {
    cout << casestr << " " << ans << endl;
  } else {
    cout << casestr << " " << "IMPOSSIBLE" << endl;
  }
}

int main() {
  int T;
  cin >> T;
  REP(cs,T) {
    casestr = "Case #" + to_string(cs+1) + ":";
    solve();
  }
}
