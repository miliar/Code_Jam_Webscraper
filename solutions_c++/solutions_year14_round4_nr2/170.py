#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
#define valid(y,x,h,w) (0<=y&&y<h&&0<=x&&x<w)
#define tpl(...) make_tuple(__VA_ARGS__)
const int INF = 1<<29;
const double EPS = 1e-8;
const double PI = acos(-1);
typedef long long ll;
typedef pair<int,int> pii;
template<class T> bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T> bool chmin(T &a, const T &b) { if (a>b) { a=b; return 1; } return 0; }
template<class T>ostream&operator<<(ostream &o,const vector<T>&t){o<<'[';FOR(i,t){if(i!=t.begin())o<<',';o<<*i;}return o<<']';}
template<class S,class T>ostream&operator<<(ostream &o,const pair<S,T>&t){return o<<'('<<t.first<<','<<t.second<<')';}
template<int N,class Tp>void out(ostream&,const Tp&){}
template<int N,class Tp,class,class ...Ts>void out(ostream &o,const Tp&t){if(N)o<<',';o<<get<N>(t);out<N+1,Tp,Ts...>(o,t);}
template<class ...Ts>ostream&operator<<(ostream&o,const tuple<Ts...>&t){o<<'(';out<0,tuple<Ts...>,Ts...>(o,t);return o<<')';}
template<class T>void output(T *a,int n){REP(i,n){if(i)cout<<',';cout<<a[i];}cout<<endl;}
template<class T>void output(T *a,int n,int m){REP(i,n)output(a[i],m);}
template<class T>void output(T t){if(t<0)t=-t,putchar('-');static int c[20];int k=0;
while(t)c[k++]=t%10,t/=10;if(!k)c[k++]=0;while(k)putchar(c[--k]^48);}
template<class S,class ...T>void output(S a,T...t){output(a);putchar(' ');output(t...);}
template<class T>bool input(T &t){t=0;int n=0,c;while(~(c=getchar())&&!isdigit(c)&&c!='-');if(!~c)return 0;
if(c=='-')n=1;else t=c^48;while(isdigit(c=getchar()))t=10*t+c-'0';t=n?-t:t;return 1;}
template<class S,class ...T>bool input(S&a,T&...t){input(a);return input(t...);}

const int MAX_N = 10000;

struct SegSum {
  int bit[MAX_N+1];               // nの最大+1必要
  int n;
  int K;
  void init(int _n) {
    n = _n;
    memset(bit, 0, sizeof(bit));
    for (K=1;(K<<1)<=n;K<<=1);
  }
  int sum(int i) {              // [1,i]の和
    int s = 0;
    while(i) {
      s += bit[i];
      i -= i & -i;
    }
    return s;
  }
  int sum(int a, int b) {      // [a,b]の和
    return sum(b)-sum(a-1);
  }
  void add(int i, int x) {      // i(>=1)にx足す
    while(i <= n) {
      bit[i] += x;
      i += i & -i;
    }
  }
  void add(int a, int b, int x) {
    // [a,b]をx個加える
    // sum(int i)がi番目の値となる
    add(a, x);
    add(b+1, -x);
  }
  int lowerBound(int w) {
    // min x s.t. sum(x)>=w
    if (w<=0) return 0;
    int x = 0;
    for (int k=K; k; k>>=1) {
      if (x+k<=n && bit[x+k]<w) {
        w -= bit[x+k];
        x += k;
      }
    }
    return x+1;
  }
};

int a[10000];
int mp[10000];
pii b[10000];

int solve() {
  int n;
  input(n);
  int mx = 0;
  int mid = 0;
  REP(i,n) {
    input(a[i]);
    if (chmax(mx,a[i])) mid = i;
  }
  output(a,n);
  vector<int> v;
  REP(i,n) if (a[i]!=mx)v.push_back(a[i]);
  REP(i,n-1) {
    b[i] = pii(v[i],i);
  }
  sort(b,b+n-1);
  // output(b,n-1);
  REP(i,n-1) mp[b[i].second] = i+1;
  int res = INF;
  static SegSum ss;
  REP(m,n) {
    for (int c=0; c<
    for (int c1=0;c1<=n-1-m; ++c1) {
      for (int c2=0; c2<=m; ++c2) {
        // cout << tpl(m,c1,c2) << endl;
        int tmp = abs(mid-m) + c1*c2;
        ss.init(n+1);
        REP(i,m) {
          int t = mp[i];
          if (i>=m-c1) t = mp[m+i-(m-c1)];
          tmp += ss.sum(t,n);
          ss.add(t,1);
        }
        ss.init(n+1);
        for (int i=m; i<n-1; ++i) {
          int t = mp[i];
          if (i-m<c2) t = mp[m-c2+i-m];
          tmp += ss.sum(1,t);
          ss.add(t,1);
        }
        // cout <<m  << " " << tmp << endl;
        chmin(res, tmp);
      }
    }
  }
  return res;
}

int main() {
  int T;
  cin >> T;
  REP(cs,T) {
    int ans = solve();
    printf("Case #%d: %d\n", cs+1, ans);
  }
}
