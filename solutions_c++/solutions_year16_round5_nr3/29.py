#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES
#include <array>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <climits>
#include <ctime>
#include <numeric>
#include <vector>
#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <complex>
#include <deque>
#include <functional>
#include <list>
#include <map>
#include <string>
#include <sstream>
#include <set>
#include <thread>
#include <unordered_set>
#include <unordered_map>
#include <stack>
#include <queue>
#include <forward_list>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int uint;
typedef unsigned char uchar;
typedef double ld;
typedef pair<int, int> pii;
typedef pair<short, short> pss;
typedef pair<LL, LL> pll;
typedef pair<ULL, ULL> puu;
typedef pair<ld, ld> pdd;
template<class T> inline T sqr(T x) { return x * x; }
template<class T> inline string tostr(const T & x) { stringstream ss; ss << x; return ss.str(); }
inline LL parse(const string & s) { stringstream ss(s); LL x; ss >> x; return x; }
#define left asdleft
#define right asdright
#define link asdlink
#define unlink asdunlink
#define next asdnext
#define prev asdprev
#define y0 asdy0
#define y1 asdy1
#define mp make_pair
#define MT make_tuple
#define pb push_back
#define sz(x) ((int)(x).size())
#define all(x) (x).begin(), (x).end()
#define clr(ar,val) memset(ar, val, sizeof(ar))
#define istr stringstream
#define forn(i,n) for(int i=0;i<(n);++i)
#define forv(i,v) forn(i,sz(v))
#define X first
#define Y second
const ld EPS = 1e-12;
const int INF = 1000*1000*1000;
const LL LINF = INF * 1ll * INF;
const ld DINF = 1e200;
const ld PI = 3.1415926535897932384626433832795l;
int gcd(int a,int b){return a?gcd(b%a,a):b;}
LL gcd(LL a,LL b){return a?gcd(b%a,a):b;}
LL gcdex(LL a,LL b,LL &x,LL &y){if(!a){x=0,y=1;return b;}LL k=b/a;LL g=gcdex(b-k*a,a,y,x);x-=k*y;return g;}
LL inv(LL a,LL m){LL x,y,g;g=gcdex(a,m,x,y);return (x%(m/g)+m/g)%m/g;}
LL crt(LL a1,LL m1,LL a2,LL m2){LL a=(a2-a1%m2+m2)%m2;LL x,y,g;g=gcdex(m1,m2,x,y);if(a%g)return -1;LL m=m1/g*m2;x*=a/g;x=(x%m2+m2)%m2;LL r=(a1+x*m1)%m;assert(r%m1==a1 && r%m2==a2);return r;}
LL powmod(LL a,LL p,LL m){LL r=1;while(p){if(p&1)r=r*a%m;p>>=1;a=a*a%m;}return r;}
bool isprime(LL a){if(a<=1)return false;for (LL i=2;i*i<=a;++i){if(a%i==0)return false;}return true;}
LL sqrtup(LL a){if(!a)return 0;LL x=max(0ll,(LL)sqrt((ld)a));while(x*x>=a)--x;while((x+1)*(x+1)<a)++x;return x+1;}
LL isqrt(LL a){LL x=max(0ll,(LL)sqrt((ld)a));while(x*x>a)--x;while((x+1)*(x+1)<=a)++x;return x;}
LL sgn(LL x){return x<0?-1:x>0?1:0;}
template<class T> ostream& operator<<(ostream &s, const vector<T> &v);
template<class A,class B> ostream& operator<<(ostream &s, const pair<A,B> &p);
template<class K,class V> ostream& operator<<(ostream &s, const map<K,V> &m);
template<class T,size_t N> ostream& operator<<(ostream &s, const array<T,N> &a);
template<class T> ostream& operator<<(ostream &s, const vector<T> &v){s<<'[';forv(i,v){if(i)s<<',';s<<v[i];}s<<']';return s;}
template<class A,class B> ostream& operator<<(ostream &s, const pair<A,B> &p){s<<"("<<p.X<<","<<p.Y<<")";return s;}
template<class K,class V> ostream& operator<<(ostream &s, const map<K,V> &m){s<<"{";bool f=false;for(const auto &it:m){if(f)s<<",";f=true;s<<it.X<<": "<<it.Y;}s<<"}";return s;}
template<class T> ostream& operator<<(ostream &s, const set<T> &m){s<<"{";bool f=false;for(const auto &it:m){if(f)s<<",";f=true;s<<it;}s<<"}";return s;}
template<class T> ostream& operator<<(ostream &s, const multiset<T> &m){s<<"{";bool f=false;for(const auto &it:m){if(f)s<<",";f=true;s<<it;}s<<"}";return s;}
template<class T,size_t N> ostream& operator<<(ostream &s, const array<T,N> &a){s<<'[';forv(i,a){if(i)s<<',';s<<a[i];}s<<']';return s;}
template<size_t n,class... T> struct put1 { static ostream& put(ostream &s, const tuple<T...> &t){s<<get<sizeof...(T)-n>(t);if(n>1)s<<',';return put1<n-1,T...>::put(s,t);} };
template<class... T> struct put1<0,T...> { static ostream& put(ostream &s, const tuple<T...> &t){return s;} };
template<class... T> ostream& operator<<(ostream &s, const tuple<T...> &t){s<<"(";put1<sizeof...(T),T...>::put(s,t);s<<")";return s;}
ostream& put2(ostream &s, const tuple<> &t){return s;}
template<class U> ostream& put2(ostream &s, const tuple<U> &t){return s<<get<0>(t);}
template<class U,class V,class... T> ostream& put2(ostream &s, const tuple<U,V,T...> &t){return s<<t;}
#ifdef __ASD__
#define dbg(...) do { cerr << #__VA_ARGS__ << " = "; put2(cerr, make_tuple(__VA_ARGS__)); cerr << endl; }while(false)
#else
#define dbg(...) do{}while(false)
#endif

struct vec{
  ld x,y,z;
  vec(){}
  vec(ld x,ld y,ld z):x(x),y(y),z(z){}
  vec operator+(const vec &b)const{
    return vec(x+b.x,y+b.y,z+b.z);
  }
  vec operator-(const vec &b)const{
    return vec(x-b.x,y-b.y,z-b.z);
  }
  vec operator*(ld b)const{
    return vec(x*b,y*b,z*b);
  }
  ld dot(const vec &b)const{
    return x*b.x+y*b.y+z*b.z;
  }
  ld lensq()const{
    return dot(*this);
  }
  ld len()const{
    return sqrt(lensq());
  }
  void read(){
    cin>>x>>y>>z;
  }
};
ostream&operator<<(ostream&o,vec v){
  return o<<'('<<v.x<<','<<v.y<<','<<v.z<<')';
}

struct sol{
  ld S0;
  vector<vec> P,V;
  ld ans;

  void input(){
    int n;
    cin>>n>>S0;
    P.resize(n);
    V.resize(n);
    forn(i,n){
      P[i].read();
      V[i].read();
    }
  }

  pdd win(vec p,vec v,ld R){
    if(v.lensq()<1e-5){
      return p.lensq()<R*R ? pdd(-1e200,1e200) : pdd(1e200, -1e200);
    }
    ld t0=-(p.dot(v))/v.lensq();
    ld d0q=(p+v*t0).lensq();
    ld dd=R*R-d0q;
    //dbg(p,v,R,t0,d0q,dd);
    if(dd<0)
      return pdd(1e200,-1e200);
    ld tt=sqrt(dd/v.lensq());
    //dbg(tt);
    if(t0+tt<=0)
      return mp(1e200,-1e200);
    return mp(max(0.,t0-tt),t0+tt);
  }

  bool check(ld R){
    vector<vector<pdd>> J(sz(P),vector<pdd>(sz(P)));
    forv(i,P){
      J[i][i]=mp(1e200,-1e200);
      forn(j,i){
        J[i][j]=J[j][i]=win(P[i]-P[j],V[i]-V[j],R);
      }
    }
    vector<vector<pdd>> S(sz(P));
    forv(v,P){
      vector<pair<ld,int>> evs;
      forv(i,P){
        pdd t=J[v][i];
        if(t.Y<=t.X)
          continue;
        evs.pb(mp(t.X,+1));
        evs.pb(mp(t.Y+S0,-1));
      }
      if(!v){
        evs.pb(mp(0,+1));
        evs.pb(mp(S0,-1));
      }
      sort(all(evs));
      int d=0;
      ld st=0;
      for(auto e:evs){
        if(!d){
          assert(e.Y==1);
          st=e.X;
        }
        d+=e.Y;
        if(!d){
          assert(e.Y==-1);
          S[v].pb(mp(st,e.X));
        }
      }
      assert(!d);
    }
    //dbg(S);

    vector<vector<ld>> D(sz(P));
    vector<vector<char>> W(sz(P));
    forv(v,P){
      D[v].resize(sz(S[v]),1e200);
      W[v].resize(sz(S[v]));
    }
    priority_queue<pair<ld,pii>> qu;
    D[0][0]=0;
    qu.push(mp(-0,mp(0,0)));
    while(!qu.empty()){
      int v=qu.top().Y.X;
      int q=qu.top().Y.Y;
      qu.pop();
      if(W[v][q])
        continue;
      W[v][q]=true;
      forv(i,P){
        //dbg(v,q,i,D[v]);
        pdd w=J[v][i];
        if(w.Y<w.X || w.Y<D[v][q] || w.X>S[v][q].Y)
          continue;
        ld d=max(D[v][q],w.X);
        if(S[i].empty()){
          dbg("weird 1");
          continue;
        }
        auto it=upper_bound(all(S[i]),mp(d+1e-12,1e200));
        if(it==S[i].begin()){
          dbg("weird 2");
          ++it;
        }
        int j=it-S[i].begin()-1;
        //dbg(j);
        if(d<D[i][j]){
          if(i==1)
            return true;
          D[i][j]=d;
          qu.push(mp(-d,mp(i,j)));
        }
      }
    }
    return false;
  }

  void solve(){
    //ans=(check(2.0001) ? 2 : 1e9);return;
    
    ld a=0,b=1e4;
    forn(qqq,60){
      ld r=(a+b)*.5;
      if(check(r))
        b=r;
      else
        a=r;
    }
    ans=(a+b)*.5;
  }

  void output(){
    cout<<ans<<endl;
  }
};

int main(int argc, char **argv){
  ios_base::sync_with_stdio(false);cin.tie(0);cout.precision(20);

  if(argc>1){
    cout<<20<<endl;
    forn(qqq,20){
      cout<<1000<<' '<<rand()%100+1<<endl;
      forn(i,1000){
        forn(j,6)
          cout<<rand()%1001-500<<' ';
        cout<<'\n';
      }
    }
    return 0;
  }
  
  const int T=8;
  int tc;
  cin>>tc;
  if(T==1){
    forn(q,tc){
      dbg(q);
      cout<<"Case #"<<q+1<<": ";
      sol s;
      s.input();
      s.solve();
      s.output();
    }
  }else{
    vector<sol> ss(tc);
    mutex m;
    vector<thread> ts(min(T,tc));
    int qq=0;
    for(auto&t:ts){
      t=thread([&]{
	  while(true){
	    int q;
	    {
	      unique_lock<mutex> lo(m);
	      if(qq>=tc)
		break;
	      q=qq++;
	      ss[q].input();
	    }
	    ss[q].solve();
	  }
	});
    }
    for(auto&t:ts){
      t.join();
    }
    assert(qq==tc);
    forv(i,ss){
      cout<<"Case #"<<i+1<<": ";
      ss[i].output();
    }
  }

  return 0;
}
