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
int dr[] = {1, -1, 0, 0};
int dc[] = {0, 0, 1, -1};
struct Sol {
  bool Valid(int a, int b, int d) {
    return d >= a && d <= b;
  }
  vector<vector<char>> board;
  int r, c;
  bool Check(int ni, int nj, int dir) {
    do {
      ni += dr[dir];
      nj += dc[dir];
      if (Valid(1, r, ni) && Valid(1, c, nj)) {
        if (board[ni][nj] != '.') {
          return true;
        }
      } else {
        return false;
      }
    } while (1);
  }
        
  void Test() {
    cin>>r>>c;
    ResizeVec(board, {r + 2, c + 2});
    RE (i, r) {
      RE (j, c) {
        cin>>board[i][j];
      }
    }
    int acc = 0;
    RE (i, r) {
      RE (j, c) {
        int dir = -1;
        if (board[i][j] == '.') { continue; }
        if (board[i][j] == '<') { dir = 3; }
        if (board[i][j] == '>') { dir = 2; }
        if (board[i][j] == '^') { dir = 1; }
        if (board[i][j] == 'v') { dir = 0; }
        if (Check(i, j, dir)) { continue; }
        debug3(i, j, dir);
        acc++;
        int good = 0;
        REP (tr, 4) {
          good += Check(i, j, tr);
        }
        if (good == 0) {
          cout<<"IMPOSSIBLE\n";
          return;
        }
      }
    }
    cout<<acc<<"\n";
        
          
    
   
    
    
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
  
  make(int, T);
  RE (tt, T) {
    cout<<"Case #"<<tt<<": ";
    Sol sol;
    sol.Test();
  }
  return 0;
}
