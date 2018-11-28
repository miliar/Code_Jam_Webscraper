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

string s[8];
int m,n;
int mp[8];
int mx,num;
void rec(int cur) {
  if (cur == m) {
    vector<set<string> > S(n);
    REP(i,m) {
      REP(j,s[i].size()+1) {
        S[mp[i]].insert(s[i].substr(0,j));
      }
    }
    int cnt = 0;
    REP(i,n) {
      cnt += S[i].size();
    }
    if (chmax(mx, cnt)) {
      num = 1;
    } else if (mx == cnt) {
      num++;
    }
    return;
  }
  REP(i,n) {
    mp[cur] = i;
    rec(cur+1);
  }
}

void solve() {
  input(m,n);
  REP(i,m) cin >> s[i];
  mx=0;
  num=0;
  rec(0);
}

int main() {
  int T;
  cin >> T;
  REP(cs,T) {
    solve();
    printf("Case #%d: %d %d\n", cs+1, mx, num);
  }
}
