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

struct P {
  int x0,y0,x1,y1;
  void in() {
    cin>>x0>>y0>>x1>>y1;
    x1++;y1++;
  }
  int dis(const P &p) {
    int res = min({max(abs(x0-p.x1),abs(y0-p.y1)),max(abs(x1-p.x0),abs(y1-p.y0)),
          max(abs(x0-p.x1),abs(y1-p.y0)),max(abs(x1-p.x0),abs(y0-p.y1))});
    if (max(x0,p.x0)<min(x1,p.x1)) {
      chmin(res, min(abs(y0-p.y1),abs(y1-p.y0)));
    }
    if (max(y0,p.y0)<min(y1,p.y1)) {
      chmin(res, min(abs(x0-p.x1),abs(x1-p.x0)));
    }
    return res;
  }
} p[1000];

int dist[1000];

int solve() {
  int w,h,n;
  input(w,h,n);
  REP(i,n) p[i].in();
  priority_queue<pii> Q;
  REP(i,n) {
    dist[i] = p[i].x0;
    Q.push(pii(-p[i].x0,i));
  }
  if (n == 0) return w;
  // REP(i,n) {
  //   for (int j=i+1; j<n; ++j) {
  //     cout << tpl(i,j,p[i].dis(p[j])) << endl;
  //   }
  // }
  int res = INF;
  while(!Q.empty()) {
    pii c = Q.top(); Q.pop();
    int d = -c.first;
    int id = c.second;
    if (dist[id] < d) continue;
    chmin(res, dist[id]+w-p[id].x1);
    REP(i,n) {
      int dd = d + p[id].dis(p[i]);
      if (dist[i] > dd) {
        dist[i] = dd;
        Q.push(pii(-dd,i));
      }
    }
  }
  return res;
}

int main() {
  int T;
  cin >> T;
  REP(cs,T) {
    printf("Case #%d: %d\n", cs+1, solve());
  }
}
