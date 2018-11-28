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
#ifdef LOCAL
#define debug(x) {cerr <<#x<<" = " <<x<<"\n"; }
#define debug2(x, y) {cerr <<#x<<" = " <<x<<", "<<#y <<" = " <<y <<"\n";}
#define debug3(x, y, z) {cerr <<#x<<" = " <<x<<", "<<#y <<" = " <<y <<", "<<#z<<" = "<<z<<"\n";}
#define debug4(x, y, z, t) {cerr <<#x<<" = " <<x<<", "<<#y <<" = " <<y <<", "<<#z<<" = "<<z<<", "<<#t <<" = " <<t<<"\n";}
#define debugv(x) {{cerr <<#x <<" = "; FORE(itt, (x)) cerr <<*itt <<", "; cerr <<"\n"; }}
#else
#define debug(x)
#define debug2(x, y)
#define debug3(x, y, z)
#define debug4(x,y,z,t)
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
using namespace std;
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
#undef int
const long long P = 28;
struct Sol {
  unordered_map<long long, int> mapka;
  vector<vector<int>> vec;
  int Cool(int a) {
    int b = 0;
    if (a & 5) {
      b++;
    }
    if (a & 10) {
      b++;
    }
    return (b == 2);
  }
  ll Hash(string s) {
    int acc = 0;
    int pot = 1;
    for (auto c : s) {
      acc += pot * ((int)(c) - (int)('a') + 1);
      pot *= P;
    }
    return acc;
  }
  int Rec(int bit, int n) {
    if (bit >= n) {
      return 0;
    }
    int r[3];
    FOR (wh, 1, 2) {
      int acc = 0;
      unordered_map<long long, int> old;
      for (auto str : vec[bit]) {
        int& x = mapka[str];
        old[str] = x;
        acc -= Cool(x);
        mapka[str] |= wh;
        acc += Cool(x);
      }
      r[wh] = acc + Rec(bit + 1, n);
      for (auto str : vec[bit]) {
        mapka[str] = old[str];
      }
    }
    return min(r[1], r[2]);
  }
  void Test() {
    make(int, n);
    string s;
    getline(cin, s);
    RE (i, n) {
      getline(cin, s);
      s += ' ';
      string tmp;
      vec.PB({});
      set<int> here;
      for (auto c : s) {
        if (c == ' ') {
          int h = Hash(tmp);
          tmp = "";
          if (here.count(h)) { continue; }
          here.insert(h);
          vec.back().PB(h);
        } else {
          tmp += c;
        }
      }
    }
    for (auto str : vec[0]) {
      mapka[str] |= 1;
    }
    for (auto str : vec[1]) {
      mapka[str] |= 2;
    }
    int st = 0;
    for (auto p : mapka) {
      if (p.nd == 3) {
        st++;
      }
    }
    cout<<st + Rec(2, n)<<endl;
  }
    
    
   
   
};

#undef int
int main() {
#define int long long

  ios_base::sync_with_stdio(0);
  cout << fixed << setprecision(10);
  cerr << fixed << setprecision(10);
  cin.tie(0);
  double beg_clock = 1.0 * clock() / CLOCKS_PER_SEC;
//   pot[0] = 1;
//   RE (i, 20) {
//     pot[i] = pot[i - 1] * P;
//   }
  make(int, T);
  RE (tt, T) {
    cout<<"Case #"<<tt<<": ";
    Sol sol;
    sol.Test();
  }
  return 0;
}
