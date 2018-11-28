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

typedef long double LD;

const LD kEps = 1e-9;

struct Point3 {
  LD x, y, z;
  Point3(LD a, LD b, LD c) : x(a), y(b), z(c) {}
  Point3() : Point3(0, 0, 0) {}
  Point3(const Point3& a) : x(a.x), y(a.y), z(a.z) {}
  void operator=(const Point3& a) { x = a.x; y = a.y; z = a.z; }
  Point3 operator+(const Point3& a) const { Point3 p(x + a.x, y + a.y, z + a.z); return p; }
  Point3 operator-(const Point3& a) const { Point3 p(x - a.x, y - a.y, z - a.z); return p; }
  Point3 operator*(LD a) const { Point3 p(x * a, y * a, z * a); return p; }
  Point3 operator/(LD a) const { assert(a > kEps); Point3 p(x / a, y / a, z / a); return p; }
  Point3& operator+=(const Point3& a) { x += a.x; y += a.y; z += a.z; return *this; }
  Point3& operator-=(const Point3& a) { x -= a.x; y -= a.y; z -= a.z; return *this; }
  Point3& operator*=(LD a) { x *= a; y *= a; z *= a; return *this;}
  Point3& operator/=(LD a) { assert(a > kEps); x /= a; y /= a; z /= a; return *this; }
  
  LD DotProd(const Point3& a) const {
    return x * a.x + y * a.y + z * a.z;
  }
  LD Norm() const {
    return sqrt(x * x + y * y + z * z);
  }
  void NormalizeSelf() {
    *this /= Norm();
  }
  Point3 Normalize() {
    Point3 res(*this);
    res.NormalizeSelf();
    return res;
  }
  LD Dis(const Point3& a) const {
    return (*this - a).Norm();
  }
  
  friend ostream& operator<<(ostream& out, Point3 m);
};

ostream& operator<<(ostream& out, Point3 p) {
  out << "(" << p.x << ", " << p.y << ", " << p.z << ")";
  return out;
}

struct Line3 {
  Point3 p[2];
  Point3& operator[](int a) { return p[a]; }
  friend ostream& operator<<(ostream& out, Line3 m);
};

Point3 ProjPtToLine3(Point3 p, Line3 l) { // ok
  Point3 diff = l[1] - l[0];
  diff.NormalizeSelf();
  return l[0] + diff * (p - l[0]).DotProd(diff);
}
LD Sq(LD x) {
  return x * x;
}
const LD kInf = 1e9;
struct Quad {
  LD a, b, c;
  Quad operator-(Quad p) {
    return {a - p.a, b - p.b, c - p.c};
  }
  vector<LD> Zeros() {
    if (abs(a) < kEps) {
      if (abs(b) < kEps) {
        return {};
      }
      return {-c / b};
    }
    LD delta = b * b - 4 * a * c;
    if (delta < kEps) {
      return {};
    }
    delta = sqrt(delta);
    return {(-b - delta) / (2 * a), (-b + delta) / (2 * a)};
  }
  LD Eval(LD x) {
    return a * x * x + b * x + c;
  }
  pair<LD, LD> NegativeInter() {
    vector<LD> zeros = Zeros();
    assert(SZ(zeros) != 1);
    if (SZ(zeros) == 0) {
      if (Eval(0) < kEps) {
        return {0, kInf};
      } else {
        return {-1, -1};
      }
    }
    pair<LD, LD> ret = {max((LD)0., zeros[0]), max((LD)0, zeros[1])}; 
    if (ret.nd < kEps) { return {}; }
    return ret;
  }
};

struct Sol {
  vector<Point3> asts;
  vector<Point3> vels;
  void Test(int tt) {
    cout<<"Case #"<<tt<<": ";
    int n, s;
    cin>>n>>s;
    asts.resize(n + 2);
    vels.resize(n + 2);
    RE (i, n) {
      int x, y, z, vx, vy, vz;
      cin>>x>>y>>z>>vx>>vy>>vz;
      asts[i] = {(LD)x, (LD)y, (LD)z};
      vels[i] = {(LD)vx, (LD)vy, (LD)vz};
    }
    LD kl = 0, kp = 1e4, faj = kp;
    
    //vector<pair<Quad, PII>> lens;
    vector<vector<Quad>> lens(n + 2, vector<Quad>(n + 2));
    RE (a, n) {
      RE (b, n) {
        if (a == b) { continue; }
        Point3 rel_vel = vels[a] - vels[b];
        Point3 diff = asts[a] - asts[b];
        Line3 tor = {diff, diff + rel_vel};
        LD v = rel_vel.Norm();
        if (abs(v) < kEps) { lens[a][b] = {0, 0, diff.Norm() * diff.Norm()}; continue; }
        Point3 proj = ProjPtToLine3(Point3{0, 0, 0}, tor);
        Point3 norm_vel = rel_vel.Normalize();
        LD offset = -(proj - diff).DotProd(norm_vel);
        LD A = proj.Norm();
        lens[a][b] = {v * v, 2 * v * offset, offset * offset + A * A};
        //debug(a, b, lens.back().a, lens.back().b, lens.back().c);
      }   
    }
   
    REP (iter, 100) {
      LD aktc = (kl + kp) / 2;
      bool found = false;
      vector<LD> events{0};
      RE (a, n) {
        RE (b, n) {
          if (a == b) { continue; }
          Quad q = lens[a][b];
          q.c -= Sq(aktc);
          pair<LD, LD> good = q.NegativeInter();
          if (a < b) { debug(good.st, good.nd); }
          if (good.st > kEps) {
            events.PB(good.st);
          }
          if (good.nd > kEps) {
            events.PB(good.nd);
            events.PB(good.nd + s + 2 * kEps);
          }
        }
      }
      sort(ALL(events));
      debug(aktc, events);
      vector<LD> active(n + 2, -kInf);
      active[1] = -2 * kEps;
      LD bef = -2 * kEps;
      vector<LD> last_jump(n + 2, -kInf);
      last_jump[1] = 0;
      for (LD t : events) {
        //VVI slo(n + 2);
        function<int(int, VI&)> Dfs = [&](int v, VI& cc) {
          int sz = 1;
          active[v] = t;
          cc.PB(v);
          RE (nei, n) {
            if (lens[v][nei].Eval(t) < Sq(aktc + kEps)) {
              if (active[nei] < t - kEps) {
                sz += Dfs(nei, cc);
              }
            }
          }
          return sz;
        };
        RE (a, n) {
          //if (active[a] < bef - kEps) { continue; }
          if (active[a] > t - kEps) { continue; }
          //LD mid = (active[a] + t) / 2;
//           bool ccan_jump = false;
//           RE (b, n) {
//             if (a == b) { continue; }
//             if (lens[a][b].Eval(mid) < Sq(aktc + kEps) && active[b] > bef - kEps) {
//               ccan_jump = true;
//               break;
//             }
//           }
          if (last_jump[a] > t - s - kEps) {
            VI cc;
            Dfs(a, cc);
            if (SZ(cc) > 1) {
              for (auto dupa : cc) {
                last_jump[dupa] = t;
              }
            }
          }
        }
        //can_jump = new_can_jump;
        cerr<<t<<" active: "<<active[1]<<" "<<active[2]<<" "<<active[3]<<endl;
        if (active[2] > -5) {
          faj = aktc;
          kp = aktc;
          found = true;
          break;
        }
        bef = t;
      }
      if (!found) {
        kl = aktc;
      }
    }
    cout<<faj<<endl;
    
  }
};

    
#undef int
int main() {
#define int long long

  ios_base::sync_with_stdio(0);
  cout << fixed << setprecision(4);
  cerr << fixed << setprecision(4);
  cin.tie(0);
  //double beg_clock = 1.0 * clock() / CLOCKS_PER_SEC;
  
  int T;
  cin>>T;
  RE (t, T) {
    Sol sol;
    sol.Test(t);
  }
    
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  return 0;
}
