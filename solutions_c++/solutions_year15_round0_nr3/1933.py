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

int A[4][4] {
  {0,1,2,3},
  {1,0,3,2},
  {2,3,0,1},
  {3,2,1,0}
};
int S[4][4] {
  {1,1,1,1},
  {1,-1,1,-1},
  {1,-1,-1,1},
  {1,1,-1,-1}
};
int B[8][8];
int mp[256];

void init() {
  mp['i'] = 1;
  mp['j'] = 2;
  mp['k'] = 3;
  REP(i,8) {
    REP(j,8) {
      int a = A[i%4][j%4];
      int s = S[i%4][j%4] * (i/4?-1:1) * (j/4?-1:1);
      if (s == -1) a += 4;
      B[i][j] = a;
    }
  }
}

int func1(const string &s, int target, ll X) {
  int c = 0;
  int cnt = 0;
  REP(k,min(X,8LL)) {
    REP(i,s.size()) {
      int a = mp[int(s[i])];
      c = B[c][a];
      if (c == target) return cnt;
      cnt++;
    }
  }
  return INF;
}

int func2(const string &s, int target, ll X) {
  int c = 0;
  int cnt = 0;
  REP(k,min(X,8LL)) {
    for (int i=s.size()-1; i>=0; --i) {
      int a = mp[int(s[i])];
      // cout << a << " " << c << " " << B[a][c] << endl;
      c = B[a][c];

      if (c == target) return cnt;
      cnt++;
    }
  }
  return INF;
}

bool check(const string &s, ll X) {
  int c = 0;
  REP(i,s.size()) c = B[c][mp[int(s[i])]];
  int r = 0;
  int t = c;
  while(X) {
    if (X&1) r = B[r][t];
    t = B[t][t];
    X >>= 1;
  }
  return (r == 4);
}

bool solve(const string &s, ll X) {
  if (!check(s,X)) return 0;
  ll p1 = func1(s,1,X);
  ll p2 = (ll)s.size()*X - 1 - func2(s,3,X);
  // cout << p1 << " " << p2 << endl;
  return p1 < p2;
}

int main() {
  init();
  int T;
  cin >> T;
  REP(cs,T) {
    int L;
    ll X;
    cin >> L >> X;
    string s;
    cin >> s;
    bool ans = solve(s, X);
    printf("Case #%d: %s\n", cs+1, ans ? "YES" : "NO");
  }
}
