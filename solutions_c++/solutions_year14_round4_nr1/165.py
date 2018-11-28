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

int a[10000];
bool used[10000];
int solve() {
  int n,x;
  input(n,x);
  multiset<pii> S;
  REP(i,n) {
    input(a[i]);
    S.insert(pii(a[i],i));
  }
  memset(used,0,sizeof(used));
  int res = 0;
  for(int i=n-1; i>=0; --i) {
    if (used[i]) continue;
    S.erase(S.find(pii(a[i],i)));
    res++;
    if (S.size()) {
      auto it = S.upper_bound(pii(x-a[i],INF));
      if (it != S.begin()) {
        it--;
        used[it->second] = 1;
        S.erase(it);
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
