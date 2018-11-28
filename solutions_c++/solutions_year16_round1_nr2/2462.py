#include <bits/stdc++.h>
#ifndef M_PI
#define M_PI 3.141592653589793238462643q
#endif

#define ff(i,s,e) for(int i=(s);i<(int)(e);i++)
#define fr(i,s,e) for(int i=(e);i-->(int)(s);)
#define FF(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define Fr(i,s,e) for(int i=(e);i>=(int)(s);i--)

#define gcd(a,b) __gcd(a,b)
#define all(a) a.begin(),a.end()
#define ln putchar('\n')
#define sp putchar(' ')
using namespace std;

typedef int64_t ll;
typedef __float128 ld;
typedef __int128 lll;

typedef pair<int,int> pii;
typedef map<int,int> mii;
typedef map<ll,ll> mll;
typedef pair<ll,ll> pll;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<pii> vpii;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef vector<vd> vvd;

template<class T>inline int pr(const T&v);
template<class T, class...Args> inline int pr(const T&a,const Args (&... args));

inline int scan(int&i){return scanf("%d",&i);}
inline int scan(ll&i){return scanf("%" PRId64,&i);}
inline int scan(double&i){return scanf("%lf",&i);}
inline int scan(char&i){int c;while((c=getchar())!=EOF&&c<=' ');i=c;return c!=EOF;}
inline int scan(string&i){i.clear();int c;while((c=getchar())!=EOF&&c<=' ');while(c>' ')i+=c,c=getchar();return i.size();}
inline int scanln(string&i){i.clear();int c;while((c=getchar())!=EOF&&c<' ');while(c>=' ')i+=c,c=getchar();return i.size();}
template<class T> inline int scan(T&a){a.sc();}
template<class T, class U> inline int scan(pair<T,U>&a){scan(a.first);return scan(a.second);}

inline int pr(const int& i){printf("%d",i);}
inline int pr(const unsigned int& i){printf("%u",i);}
inline int pr(const bool i){printf("%d",i);}
inline int pr(const ll&i){printf("%" PRId64,i);}
inline int pr(const unsigned long&i){printf("%" PRId64,(ll)i);}
inline int pr(const double&i){printf("%.12f",i);}
inline int pr(const float&i){printf("%.4f",i);}
inline int pr(const char&i){putchar(i);}
inline int pr(const char*i){printf("%s",i);}
inline int pr(const string&i){for(char c:i)pr(c);}

template<class T>inline int scan(vector<T>&v){for(T&i:v)scan(i);}
template<class T,class U>inline int pr(const pair<T,U>&p){pr(p.first,p.second);}
template<class T>inline int pr(const vector<T>&v){if(v.empty())return 0;pr(v[0]);ff(i,1,v.size())pr(' '),pr(v[i]);}
template<class T>inline int prlns(const vector<T>&v){ff(i,0,v.size())pr(v[i]),pr('\n');}
template<class T, class...Args> inline int scan(T&a,Args (&... args)){return scan(a),scan(args...);}
template<class T, class...Args> inline int pr(const T&a,const Args (&... args)){pr(a),pr(' '),pr(args...);}
template<class T> inline int prln(const T&a){pr(a),ln;}
template<class T, class...Args> inline int prln(const T&a,const Args (&... args)){pr(a),sp,prln(args...);}
template<class...Args> inline int rpr(const Args (&... args)){
#ifndef ONLINE_JUDGE
  pr(args...),ln;fflush(stdout);
#endif
}
inline int gi(){int x;scan(x);return x;}
inline int gis(){int x;scan(x);return x-1;}

template<class T>inline int pr(const T&v){v.print();}

template<class T, class U> inline void smax(T&a,const U&b){if(a<b)a=b;}
template<class T, class U> inline void smin(T&a,const U&b){if(b<a)a=b;}

template<class T> T& operator +=(vector<T>&v,const T&a){v.push_back(a);return v.back();}

const int inf = (1<<30) + (1 << 29);
const ll LargeMod = 4611686018427388039;
const ll MOD = 1E9+7;
const ll linf = 1E17;
typedef unsigned int uint;
const ll lprime = 37ll;

int fpow(ll base, ll n) {
  ll cur = 1;
  while (n) {
    if (n & 1)cur = cur * base % 100;
    base = base * base % 100;
    n >>= 1;
  }
  return cur;
}
struct po {
  double x, y;
  int sc() {
    return scan(x, y);
  }
  double len() {
    return sqrt(x * x + y * y);
  }
  po operator *(double o) {
    return {x*o, y*o};
  }
  po operator + (po o) {
    return {x+o.x,y+o.y};
  }
  int print() const {
    pr(x,y),ln;
  }
};

struct problem {
  int n;
  vector<vvi> a;
  int solve() {
    vi u(n, 0);
    ff(i,0,n) {
      bool ok = 1;
      if (a[i].size() == 2)
        ff(j,0,i)
          if(a[i][1][j] != a[j][0][i])
            ok = 0;
      ff(j,0,i)
        if(a[j].size()==2 && a[i][0][j] != a[j][1][i])
          ok = 0;
      if (i)
        ff(j,0,n)
        if(a[i][0][j] <= a[i-1][0][j])
          ok=0;
      if (!ok) {
        while (u[i] || a[i].size() == 1) {
          if (a[i].size() == 2) {
            swap(a[i][0], a[i][1]);
            u[i] = !u[i];
          }
          i--;
        }
        u[i] = !u[i];
        swap(a[i][0], a[i][1]);
        i--;
      }
    }
    int ro = 0;
    ff(i,0,n) {
      if (a[i].size() == 1)ro = i;
    }
    ff(i,0,n) {
      sp, pr(a[i][0][ro]);
    }
    ln;

  }
  
  int init() {
    
  }
  
  int get_input() {
    scan(n);
    vvi v;
    v.resize(n*2 - 1, vi(n));
    scan(v);
    a.resize(n);
    ff(i,0,n) {
      int mi = 1000000;
      for (vi &u:v) {
        smin(mi, u[i]);
      }
      ff(j,0,v.size()) {
        if (v[j][i] == mi) {
          a[i].push_back(v[j]);
          v.erase(v.begin()+j);
          j--;
        }
      }
    }
  }
};

int main(){
  int T;
  scan(T);
  ff(i,0,T) {
    printf("Case #%d:", i+1);
    unique_ptr<problem> xx(new problem());
    xx->get_input();
    xx->init();
    xx->solve();
  }
  return 0;
}
