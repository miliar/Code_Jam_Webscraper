#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); ++i)

// ID*2^31,DD*2^31で実装されている
// 桁数は必要最低限の倍以上を推奨

// 整数部桁数
const int ID = 3;
// 小数部桁数
const int DD = 8;

const int BS = 31;

const bool PLUS = false;
const bool MINUS = true;

struct BD {
  bool sign;
  long long d[ID + DD];

  BD();
  ~BD();
  BD(int);
  BD(long long);
  BD(string);
  BD(double);

  BD normal();

  BD operator-() const;
  BD operator<<(int) const;
  BD operator>>(int) const;
  BD operator+(const BD&) const;
  BD operator-(const BD&) const;
  BD operator*(unsigned int) const;
  BD operator*(const BD&) const;
  BD operator/(const BD&) const;
  BD operator%(const BD&) const;

  BD operator<<=(int);
  BD operator>>=(int);
  BD operator+=(const BD&);
  BD operator-=(const BD&);
  BD operator*=(unsigned int);
  BD operator*=(const BD&);
  BD operator/=(const BD&);
  BD operator%=(const BD&);

  BD operator++();
  BD operator++(int);
  BD operator--();
  BD operator--(int);

  // EPSILONを考慮した比較
  bool operator==(const BD&) const;
  bool operator!=(const BD&) const;
  bool operator<(const BD&) const;
  bool operator>(const BD&) const;
  bool operator<=(const BD&) const;
  bool operator>=(const BD&) const;
  // EPSILONなしの厳密な比較
  // 0になるまで繰り返すなどの処理に用いる
  bool equals(const BD&) const;

  int toInt() const;
  long long toLongLong() const;
  string toString(int, string) const;
  double toDouble() const;
};

ostream &operator<<(ostream&, BD);
istream &operator>>(istream&, BD&);

// cmathから基本的な関数を抽出
BD sin(BD);
BD cos(BD);
BD tan(const BD&);
BD asin(BD);
BD acos(const BD&);
BD atan(BD);
BD atan2(const BD&, const BD&);
BD sinh(BD);
BD cosh(BD);
BD tanh(const BD&);
BD exp(const BD&);
BD log(const BD&);
BD log10(const BD&);
BD pow(const BD&, const BD&);
BD sqrt(const BD&);
BD abs(const BD&);
BD ceil(const BD&);
BD floor(BD);

// 何度もコンストラクタを呼ぶと無駄なので定数にしてしまう
// ライブラリ外では考慮する必要はほぼない
const BD BD0 = BD(0);
const BD BD1 = BD(1);
const BD BD2 = BD(2);
const BD BD3 = BD(3);
const BD REV10 = BD1 / BD(10);
const BD PI = (atan(BD1 / BD(5)) << 4) - (atan(BD1 / BD(239)) << 2);

// EPSILONの値はかなり怪しいので適宜調整が必要
const BD EPSILON = BD1 >> (BS - 4) * DD;

// complexでデフォルトコンストラクタは0を返すことが仮定されている
BD::BD() {*this = BD0;}
BD::~BD() {}

BD::BD(int n) {
  sign = PLUS;
  rep (i, ID + DD) d[i] = 0;
  d[DD] = n;
  normal();
}

BD::BD(long long n) {
  sign = PLUS;
  rep (i, ID + DD) d[i] = 0;
  d[DD] = n;
  normal();
}

// TODO どう見てもオーバーフローするので後で修正
BD::BD(string str) {
  *this = BD0;
  bool minus = false;
  if (str[0] == '-') {
    minus = true;
    str = str.substr(1);
  }
  int rp = 0;
  rep (i, str.size()) {
    if (str[i] == '.') rp = str.size() - i - 1;
    else *this = *this * 10 + (str[i] - '0');
  }
  while (rp--) *this *= REV10;
  if (minus) sign = MINUS;
}

BD::BD(double r) {
  *this = BD0;
  int n;
  BD bd = r >= 0 ? BD1 : -BD1;
  r = 2 * abs(frexp(abs(r), &n));
  bd <<= n - 1;
  rep (i, 64) {
    if (r >= 1) {
      *this += bd;
      r -= 1;
    }
    r *= 2;
    bd >>= 1;
  }
}

BD BD::normal() {
  rep (i, ID + DD - 1){
    d[i + 1] += d[i] >> BS;
    d[i] &= (1LL << BS) - 1;
  }
  if (d[ID + DD - 1] < 0) {
    sign = !sign;
    rep (i, ID + DD) d[i] = -d[i];
    normal();
  }
  if (d[ID + DD - 1] >= (1LL << BS)) throw "overflow";
  rep (i, ID + DD) if (d[i] != 0) return *this;
  sign = PLUS;
  return *this;
}

BD BD::operator-() const {
  BD bd(*this);
  bd.sign = !bd.sign;
  return bd;
}

BD BD::operator<<(int a) const {return BD(*this) <<= a;}
BD BD::operator>>(int a) const {return BD(*this) >>= a;}
BD BD::operator+(const BD &a) const {return BD(*this) += a;}
BD BD::operator-(const BD &a) const {return BD(*this) -= a;}
BD BD::operator*(unsigned int a) const {return BD(*this) *= a;}
BD BD::operator*(const BD &a) const {return BD(*this) *= a;}
BD BD::operator/(const BD &a) const {return BD(*this) /= a;}
BD BD::operator%(const BD &a) const {return BD(*this) %= a;}

BD BD::operator<<=(int a) {
  if (a < 0) return *this >>= -a;
  while (a >= BS) {
    if (d[ID + DD - 1]) throw "overflow";
    for (int i = ID + DD; --i > 0; ) d[i] = d[i - 1];
    d[0] = 0;
    a -= BS;
  }
  if (d[ID + DD - 1] >= (1LL << (BS - a))) throw "overflow";
  rep (i, ID + DD) d[i] <<= a;
  return normal();
}

BD BD::operator>>=(int a) {
  if (a < 0) return *this <<= -a;
  while (a >= BS) {
    rep (i, ID + DD - 1) d[i] = d[i + 1];
    d[ID + DD - 1] >>= BS;
    a -= BS;
  }
  rep (i, ID + DD - 1) {
    d[i] |= d[i + 1] << BS;
    d[i + 1] = 0;
  }
  rep (i, ID + DD) d[i] >>= a;
  return normal();
}

BD BD::operator+=(const BD &a) {
  if (sign == a.sign) rep (i, ID + DD) d[i] += a.d[i];
  else rep (i, ID + DD) d[i] -= a.d[i];
  return normal();
}

BD BD::operator-=(const BD &a) {return *this += -a;}

BD BD::operator*=(unsigned int a) {
  rep (i, ID + DD) d[i] *= a;
  return normal();
}

BD BD::operator*=(const BD &a) {
  BD res = BD0;
  rep (i, ID + DD) {
    if (i < DD) res = (res + *this * a.d[i]) >> BS;
    else res += *this * a.d[i] << (i - DD) * BS;
  }
  res.sign = (sign == a.sign ? PLUS : MINUS);
  return *this = res.normal();
}

BD BD::operator/=(const BD &a) {
  if (a == BD0) throw "divide by zero";
  BD rev = (double)1 / a.toDouble();
  rep (i, 7) rev = (rev << 1) - a * rev * rev;
  rev.sign = a.sign;
  return *this *= rev;
}

BD BD::operator%=(const BD &a) {
  if (a == BD0) throw "modulo by zero";
  return *this -= floor(*this / a) * a;
}

BD BD::operator++() {
  return *this += 1;
}

BD BD::operator++(int) {
  BD bd = *this;
  *this += 1;
  return bd;
}

BD BD::operator--() {
  return *this -= 1;
}

BD BD::operator--(int) {
  BD bd = *this;
  *this -= 1;
  return bd;
}

// TODO 比較周りの整合性がとれていない可能性があるので後で調べる
bool BD::operator==(const BD &a) const {return *this <= a && a <= *this;}
bool BD::operator!=(const BD &a) const {return !(*this == a);}

bool BD::operator<(const BD &a) const {
  if (*this == a) return false;
  BD aa = a - EPSILON;
  if (sign == MINUS) {
    if (aa.sign == MINUS) return -a < -*this;
    else return true;
  }
  if (aa.sign == MINUS) return false;
  for (int i = ID + DD; i-- > 0; ) if (d[i] != aa.d[i]) return d[i] < aa.d[i];
  return false;
}
bool BD::operator>(const BD &a) const {return a < *this;}

bool BD::operator<=(const BD &a) const {
  BD aa = a + EPSILON;
  if (sign == MINUS) {
    if (aa.sign == MINUS) return -aa <= -*this;
    else return true;
  }
  if (aa.sign == MINUS) return false;
  for (int i = ID + DD; i-- > 0; ) if (d[i] != aa.d[i]) return d[i] < aa.d[i];
  return true;
}
bool BD::operator>=(const BD &a) const {return a <= *this;}

bool BD::equals(const BD &a) const {
  if (sign != a.sign) return false;
  rep (i, ID + DD) if (d[i] != a.d[i]) return false;
  return true;
}

int BD::toInt() const {
  int res = 0;
  rep (i, ID) res += d[DD + i] << BS * i;
  if (sign == MINUS) return -res;
  return res;
}

long long BD::toLongLong() const {
  long long res = 0;
  rep (i, ID) res += d[DD + i] << BS * i;
  if (sign == MINUS) return -res;
  return res;
}

string BD::toString(int digit = 100, string mode = "near") const {
  string str;
  BD a = *this, bd = BD1;
  if (a.sign == MINUS) {
    str += "-";
    a.sign = PLUS;
  }
  if (mode == "near") {
    BD round = BD1 >> 1;
    rep (i, digit) round *= REV10;
    a += round + EPSILON;
  }
  if (mode == "ceil") {
    BD round = BD1;
    rep (i, digit) round *= REV10;
    a += round - EPSILON;
  }
  for (; bd <= a; bd *= 10) ++digit;
  if (bd > BD1) {
    bd *= REV10;
    --digit;
  }
  rep (i, digit + 1) {
    if (bd == BD0) {
      str += "0";
      continue;
    }
    if (bd == REV10) str += ".";
    int d = 0;
    while (bd < a) {
      a -= bd;
      ++d;
    }
    if (d > 9) {
      d -= 10;
      string::iterator itr = str.end();
      while (true) {
	if (itr == str.begin()) {
	  str = "1" + str;
	  break;
	}
	--itr;
	if (*itr == '.') continue;
	++*itr;
	if (*itr > '9') *itr = '0';
	else break;
      }
    }
    str += '0' + d;
    bd *= REV10;
  }
  return str;
}

double BD::toDouble() const {
  double res = 0;
  rep (i, ID + DD) res += d[i] * pow(2, (i - DD) * BS);
  if (sign == MINUS) return -res;
  return res;
}

ostream &operator<<(ostream &os, BD a) {
  os << a.toString();
  return os;
}
istream &operator>>(istream &is, BD &a) {
  string str;
  is >> str;
  a = BD(str);
  return is;
}

BD sin(BD x) {
  BD res = BD0, xx = - x * x;
  for (BD i = BD1; ; i += BD2) {
    x /= max(i * (i - 1), BD1);
    if (x.equals(BD0)) break;
    res += x;
    x *= xx;
  }
  return res;
}

BD cos(BD x) {
  BD res = BD0, xx = - x * x;
  x = BD1;
  for (BD i = BD0; ; i += BD2) {
    x /= max(i * (i - BD1), BD1);
    if (x.equals(BD0)) break;
    res += x;
    x *= xx;
  }
  return res;
}

BD tan(const BD &x) {return sin(x) / cos(x);}

BD asin(BD x) {
  if (abs(x) > BD1) throw "out of domain";
  if (x > BD1 / sqrt(BD2)) return (PI >> 1) - asin(sqrt(BD1 - x * x));
  if (x < -BD1 / sqrt(BD2)) return -(PI >> 1) + asin(sqrt(BD1 - x * x));
  BD res = BD0, xx = x * x >> 2;
  for (BD i = BD0; ; ++i) {
    x *= max(i * BD2 * (i * BD2 - BD1), BD1);
    x /= max(i * i, BD1);
    BD add = x / (i * BD2 + BD1);
    if (add.equals(BD0)) break;
    res += add;
    x *= xx;
  }
  return res;
}

BD acos(const BD &x) {return (PI >> 1) - asin(x);}

BD atan(BD x) {
  if (x.sign == MINUS) return -atan(-x);
  if (abs(x) > sqrt(BD2) + BD1) return (PI >> 1) - atan(BD1 / x);
  if (abs(x) > sqrt(BD2) - BD1) return (PI >> 2) + atan((x - BD1) / (x + BD1));
  BD res = BD0, xx = - x * x;
  for (BD i = BD1; ; i += BD2) {
    BD add = x / i;
    if (add.equals(BD0)) break;
    res += add;
    x *= xx;
  }
  return res;
}

BD atan2(const BD &y, const BD &x) {
  if (x == BD0) {
    if (y > BD0) return PI / BD2;
    if (y < BD0) return -PI / BD2;
    throw "origin can't define argument";
  }
  if (x.sign == PLUS) return atan(y / x);
  if (y.sign == PLUS) return atan(y / x) + PI;
  return atan(y / x) - PI;
}

BD sinh(BD x) {
  BD res = BD0, xx = x * x;
  for (BD i = BD1; ; i += BD2) {
    x /= max(i * (i - BD1), BD1);
    if (x.equals(BD0)) break;
    res += x;
    x *= xx;
  }
  return res;
}

BD cosh(BD x) {
  BD res = BD0, xx = x * x;
  x = BD1;
  for (BD i = BD0; ; i += BD2) {
    x /= max(i * (i - BD1), BD1);
    if (x.equals(BD0)) break;
    res += x;
    x *= xx;
  }
  return res;
}

BD tanh(const BD &x) {return sinh(x) / cosh(x);}

BD exp(const BD &x) {
  BD res = BD0, xx = BD1;
  for (int i = 0; ; ++i) {
    xx /= max(i, 1);
    if (xx.equals(BD0)) break;
    res += xx;
    xx *= x;
  }
  return res;
}

BD log(const BD &x) {
  BD y = log(x.toDouble());
  BD z = x / exp(y);
  BD a = (z - 1) / (z + 1);
  BD res = BD0, b = a, aa = a * a;
  for (int i = 1; ; i += 2) {
    if (b.equals(BD0)) break;
    res += b / i;
    b *= aa;
  }
  return y + res * BD2;
}

BD log10(const BD &x) {return log(x) / log(BD(10));}

BD pow(const BD &x, const BD &y) {
  if (x.sign == MINUS) {
    if (floor(y) == y) return floor(y).d[DD] % 2 ? -pow(-x, floor(y)) : pow(-x, floor(y));
    throw "power of negative number";
  }
  return exp(y * log(x));
}

BD sqrt(const BD &x) {
  BD r = 1 / sqrt(x.toDouble());
  rep (i, 7) r *= (BD3 - x * r * r) >> 1;
  return BD1 / r;
}

BD abs(const BD &x) {return x.sign == PLUS ? x : -x;}

BD ceil(const BD &x) {
  if (x.sign == MINUS) return -floor(-x);
  BD f = floor(x);
  return f == x ? f : x + 1;
}

BD floor(BD x) {
  if (x.sign == MINUS) return -ceil(-x);
  x += EPSILON;
  rep (i, DD) x.d[i] = 0;
  return x;
}

#define X real()
#define Y imag()

typedef BD Real;
typedef complex<Real> Point;
struct Line{Point a, b;};
typedef vector<Point> Polygon;

const Real EPS = BD("0.000000000000000000001");
//const Real PI = acos(-1);

// 比較関数
inline int sgn(Real a, Real b = 0) {return a < b - EPS ? -1 : a > b + EPS ? 1 : 0;}
inline bool near(Point a, Point b) {return !sgn(abs(a - b));}
namespace std {
  inline bool operator<(Point a, Point b) {return sgn(a.X, b.X) ? a.X < b.X : a.Y < b.Y;}
  inline bool operator<(Line a, Line b) {return !near(a.a, b.a) ? a.a < b.a : a.b < b.b;}
}

// 平方根
inline Real sr(Real a) {return sqrt(max(a, (Real)0));}

// 内積
inline Real dot(const Point& a, const Point& b) {return a.X * b.X + a.Y * b.Y;}
// 外積
inline Real det(const Point& a, const Point& b) {return a.X * b.Y - a.Y * b.X;}

// 線分のベクトル
inline Point vec(const Line& a) {return a.b - a.a;}

// 線分abに対する点cの位置
enum CCW{FRONT = 1, RIGHT = 2, BACK = 4, LEFT = 8, ON = 16};
inline int ccw(const Point& a, const Point& b, const Point& c) {
  if (near(a, c) || near(b, c)) return ON;
  int s = sgn(det(b - a, c - a));
  if (s) return s > 0 ? LEFT : RIGHT;
  return (a < b) == (b < c) ? FRONT : (c < a) == (a < b) ? BACK : ON;
}

// 有向角度
inline Real arg(const Point& base, const Point& a, const Point& b) {return arg((b - base) / (a - base));}
Line sortBase;
inline bool lessArg(const Point& a, const Point& b) {
  Real ang1 = arg(sortBase.a, sortBase.b, a);
  Real ang2 = arg(sortBase.a, sortBase.b, b);
  return sgn(ang1, ang2) ? ang1 < ang2 : norm(a) > norm(b);
}

// 射影
inline Point proj(const Point& a, const Point& b) {return a * dot(a, b) / norm(a);}
inline Point perp(const Line& l, const Point& p) {return l.a + proj(vec(l), p - l.a);}
inline Point refl(const Line& l, const Point& p) {return perp(l, p) * (Real)2 - p;}

// 交差判定
inline bool eqL(const Line& a, const Line& b) {return !sgn(det(vec(a), vec(b))) && !sgn(det(vec(a), b.a - a.a));}
inline bool iLL(const Line& a, const Line& b, bool strict = false) {
  if (sgn(det(vec(a), vec(b)))) return true;
  return !strict && !sgn(det(vec(a), b.a - a.a));
}
inline bool iLS(const Line& a, const Line& b, bool strict = false) {
  if (strict) return sgn(det(vec(a), b.a - a.a)) * sgn(det(vec(a), b.b - a.a)) < 0;
  return sgn(det(vec(a), b.a - a.a)) * sgn(det(vec(a), b.b - a.a)) <= 0;
}
inline bool iSS(const Line& a, const Line& b, bool strict = false) {
  int cwa = ccw(a.a, a.b, b.a) | ccw(a.a, a.b, b.b);
  int cwb = ccw(b.a, b.b, a.a) | ccw(b.a, b.b, a.b);
  if ((cwa & cwb) == (LEFT | RIGHT)) return true;
  return !strict && ((cwa | cwb) & ON);
}

// 交点
inline Point pLL(const Line& a, const Line& b) {return a.a + vec(a) * (det(vec(b), b.a - a.a) / det(vec(b), vec(a)));}

// 距離
inline Real dLP(const Line& l, const Point& p) {return abs(det(vec(l), p - l.a) / vec(l));}
inline Real dSP(const Line& s, const Point& p) {
  if (dot(vec(s), p - s.a) < 0) return abs(p - s.a);
  if (dot(vec(s), p - s.b) > 0) return abs(p - s.b);
  return dLP(s, p);
}
inline Real dLL(const Line& a, const Line& b) {return iLL(a, b) ? 0 : dLP(a, b.a);}
inline Real dLS(const Line& a, const Line& b) {return iLS(a, b) ? 0 : min(dLP(a, b.a), dLP(a, b.b));}
inline Real dSS(const Line& a, const Line& b) {return iSS(a, b) ? 0 : min(min(dSP(a, b.a), dSP(a, b.b)), min(dSP(b, a.a), dSP(b, a.b)));}

// 角の内外判定 角abの内部にあれば正、辺上は0、外部は負
inline int sAP(const Point& a, const Point& b, const Point& c) {return sgn(det(a, c)) - sgn(det(b, c)) - sgn(det(a, b));}

// 多角形の内外判定 内部:1、周上:0、外部:-1
inline int sGP(const Polygon& pol, const Point& p) {
  int side = -1;
  for (int i = 0; i < int(pol.size()); ++i) {
    Point p0 = pol[i] - p, p1 = pol[(i + 1) % pol.size()] - p;
    if (ccw(p0, p1, BD(0)) == ON) return 0;
    if (p0.Y > p1.Y) swap(p0, p1);
    if (sgn(p0.Y) <= 0 && 0 < sgn(p1.Y) && sgn(det(p0, p1)) > 0) side *= -1;
  }
  return side;
}

void solve() {
  int n;
  cin >> n;
  Real v, x;
  cin >> v >> x;
  vector<pair<Real, Real>> w(n);
  for (int i = 0; i < n; ++i) {
    cin >> w[i].second >> w[i].first;
  }
  sort(w.begin(), w.end());
  if (x < w[0].first || w.back().first < x) {
    cout << "IMPOSSIBLE" << endl;
    return;
  }
  vector<Point> p;
  Point pp = BD(0);
  for (int i = 0; i < n; ++i) {
    pp += Point(w[i].second, w[i].first * w[i].second);
    p.emplace_back(pp);
  }
  for (int i = 0; i < n; ++i) {
    pp -= Point(w[i].second, w[i].first * w[i].second);
    p.emplace_back(pp);
  }
  Real l = 0, u = 1e9;
  for (int _ = 0; _ < 100; ++_) {
    Real m = (l + u) / 2;
    Point pp(v / m, v * x / m);
    if (sGP(p, pp) == -1) l = m;
    else u = m;
  }
  cout << fixed << setprecision(100) << l << endl;
}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    cerr << i << endl;
    cout << "Case #" << i + 1 << ": ";
    solve();
  }
}
