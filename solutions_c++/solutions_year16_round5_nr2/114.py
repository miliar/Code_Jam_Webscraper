#include <bits/stdc++.h>
#define MP make_pair
#define PB push_back
#define int long long
#define st first
#define nd second
#define rd third
#define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
#define RE(i, n) FOR(i, 1, n)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define REP(i, n) for(int i = 0;i <(n); ++i)
#define VAR(v, i) __typeof(i) v=(i)
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
using namespace std;
template<typename TH> void _dbg(const char* sdbg, TH h) { cerr<<sdbg<<"="<<h<<"\n"; }
template<typename TH, typename... TA> void _dbg(const char* sdbg, TH h, TA... t) {
  while(*sdbg != ',')cerr<<*sdbg++; cerr<<"="<<h<<","; _dbg(sdbg+1, t...);
}
#ifdef LOCAL
#define debug(...) _dbg(#__VA_ARGS__, __VA_ARGS__)
#define debugv(x) {{cerr <<#x <<" = "; FORE(itt, (x)) cerr <<*itt <<", "; cerr <<"\n"; }}
#else
#define debug(...) (__VA_ARGS__)
#define debugv(x)
#define cerr if(0)cout
#endif
#define make(type, x) type x; cin>>x;
#define make2(type, x, y) type x, y; cin>>x>>y;
#define make3(type, x, y, z) type x, y, z; cin>>x>>y>>z;
#define make4(type, x, y, z, t) type x, y, z, t; cin>>x>>y>>z>>t;
#define next ____next
#define prev ____prev
#define left ____left
#define hash ____hash
typedef long long ll;
typedef long double LD;
typedef pair<int, int> PII;
typedef pair<ll, ll> PLL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<ll> VLL;
typedef vector<pair<int, int> > VPII;
typedef vector<pair<ll, ll> > VPLL;

template<class C> void mini(C&a4, C b4){a4=min(a4, b4); }
template<class C> void maxi(C&a4, C b4){a4=max(a4, b4); }
template<class T1, class T2>
ostream& operator<< (ostream &out, pair<T1, T2> pair) { return out << "(" << pair.first << ", " << pair.second << ")";}
template<class A, class B, class C> struct Triple { A first; B second; C third;
  bool operator<(const Triple& t) const { if (st != t.st) return st < t.st; if (nd != t.nd) return nd < t.nd; return rd < t.rd; } };
template<class T> void ResizeVec(T&, vector<int>) {}
template<class T> void ResizeVec(vector<T>& vec, vector<int> sz) {
  vec.resize(sz[0]); sz.erase(sz.begin()); if (sz.empty()) { return; }
  for (T& v : vec) { ResizeVec(v, sz); }
}
typedef Triple<int, int, int> TIII;
template<class A, class B, class C>
ostream& operator<< (ostream &out, Triple<A, B, C> t) { return out << "(" << t.st << ", " << t.nd << ", " << t.rd << ")"; }
template<class T> ostream& operator<<(ostream& out, vector<T> vec) { out<<"("; for (auto& v: vec) out<<v<<", "; return out<<")"; }

struct Sol {
  void Test(int t) {
    cout<<"Case #"<<t<<": ";
    int n;
    cin>>n;
    VVI slo(n + 2);
    VI indeg(n + 2);
    RE (i, n) {
      int a;
      cin>>a;
      if (a) {
        slo[a].PB(i);
        indeg[i]++;
      }
    }
    vector<char> fsts(n + 2);
    RE (i, n) {
      cin>>fsts[i];
    }
    vector<string> cool;
    vector<int> hits;
    VI sz(n + 2);
    int M;
    cin>>M;
    RE (i, M) {
      string c;
      cin>>c;
      cool.PB(c);
      hits.PB(0);
    }
    function<void(int)> Dfs = [&](int v) {
      sz[v] = 1;
      for (auto son : slo[v]) {
        Dfs(son);
        sz[v] += sz[son];
      }
    };
    RE (i, n) {
      if (indeg[i] == 0) {
        Dfs(i);
      }
    }
    debugv(sz);
    int tries = 20000;
    REP (_, tries) {
      VI forb = indeg;
      string str;
      int rem = n;
      while (rem) {
        int r = rand () % rem;
        RE (i, n) {
          if (forb[i]) { continue; }
          r -= sz[i];
          if (r < 0) {
            forb[i] = 1;
            str += fsts[i];
            for (auto son : slo[i]) {
              forb[son] = 0;
            }
            //active[i] = 
            break;
          }
        }
        assert(r < 0);
        rem--;
      }
      debug(str);
      REP (c, M) {
        REP (beg, SZ(str)) {
          if (str.substr(beg, SZ(cool[c])) == cool[c]) {
            hits[c]++;
            break;
          }
        }
      }
    }
    REP (c, M) {
      cout<<(LD)hits[c] / tries<<" ";
    }
    cout<<endl;
      
  }
};

    
#undef int
int main() {
#define int long long

  ios_base::sync_with_stdio(0);
  cout << fixed << setprecision(6);
  cerr << fixed << setprecision(6);
  cin.tie(0);
  //double beg_clock = 1.0 * clock() / CLOCKS_PER_SEC;
  
  srand(clock());
  int T;
  cin>>T;
  RE (t, T) {
    Sol sol;
    sol.Test(t);
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  return 0;
}
