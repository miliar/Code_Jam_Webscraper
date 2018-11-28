#include <stdint.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <limits>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <boost/math/constants/constants.hpp>
using namespace std;

const double kPi = boost::math::constants::pi<double>();
const double k2Pi = 2.0 * kPi;

const int kIntMax = std::numeric_limits<int>::max();
const int kIntMin = std::numeric_limits<int>::min();
const uint16_t kUInt16Max = std::numeric_limits<uint16_t>::max();

const double kPhiRGR = 0.6180339887498949;  // reciprocal of the Golden Ratio
const double kSqrt2  = 1.4142135623730951;
const double kSqrt3  = 1.7320508075688772;

const double kDblInf = std::numeric_limits<double>::infinity();

#define CHECK(expression) {                                             \
  if (!(expression)) {                                                  \
    std::cerr << "CHECK failed at "                                     \
              << __FILE__ << ":" << __LINE__ << "!\n"                   \
              << "Expression: " << #expression << std::endl;            \
    std::abort();                                                       \
  }                                                                     \
}

#define ABORT(message) {                                                \
    std::cerr << "Aborted at "                                          \
              << __FILE__ << ":" << __LINE__ << "!\n"                   \
              << "Message: " << message << std::endl;                   \
    std::abort();                                                       \
}

#define all(v) (v).begin(),(v).end()
#define forint(i,c,d) for (int i=(c); i<=(d); ++i)
#define forall(i,V) for (int i=0; i<(V).size(); ++i)
#define foritr(p,V) for(__typeof((V).end()) p=(V).begin(); p!=(V).end(); ++p)
#define showall(V) { cerr<<#V<<": ";foritr(p, (V))cerr<<*(p)<<" ";cerr<<endl; }
#define showvar(x) { cerr<<#x<<" = "<<(x)<<endl; }

typedef long long int64;
typedef unsigned long long uint64;
template<class T> void CheckMin(T&a, const T&b) { if (b<a) a=b; }
template<class T> void CheckMax(T&a, const T&b) { if (a<b) a=b; }

template<typename T> inline
T Abs(const T &x) { return x < 0 ? -x : x; }

template<typename T> inline
T Min(const T &a, const T &b) { return a < b ? a : b; }

template<typename T> inline
T Max(const T &a, const T &b) { return b < a ? a : b; }

template<typename T> inline
T Sqr(const T &x) { return x * x; }

int Sign(const int x) { return x == 0 ? 0 : (x < 0 ? -1 : 1); }

template<typename T> inline
T Clamp(const T &x, const T &lower_bound, const T &upper_bound) {
  assert(!(upper_bound < lower_bound));
  return x < lower_bound ? lower_bound : (upper_bound < x ? upper_bound : x);
}

template<typename T> inline
std::string ToString(const T &v) {
  std::ostringstream out;
  out << v;
  CHECK(out);
  return out.str();
}

template<typename T> inline
T StringTo(const std::string &s) {
  std::istringstream in(s);
  T v;
  in >> v;
  CHECK(in);
  return v;
}

inline
int Round(const double x) { return static_cast<int>(std::floor(x + 0.5)); }

inline
bool IsExactInteger(const double x) { return x == std::floor(x); }

inline
bool IsBetween(const double x,
               const double lower_bound, const double upper_bound,
               const double eps = 0) {
  assert(lower_bound <= upper_bound);
  return -eps + lower_bound <= x && x <= upper_bound + eps;
}

inline
double DegToRad(const double deg) {
  static const double k = kPi / 180.0;
  return k * deg;
}

inline
double RadToDeg(const double rad) {
  static const double k = 180.0 / kPi;
  return k * rad;
}

inline
bool Eoln(std::istream &in) { return in.peek() == '\n' || in.peek() == EOF; }

inline
bool SeekEoln(std::istream &in) {
  int c(0);
  while ((c = in.peek()) != EOF &&
         (c == ' ' || c == '\t' || c == '\r')) in.get();
  return c == EOF || c == '\n';
}

inline
bool SeekEof(std::istream &in) {
  int c(0);
  while ((c = in.peek()) != EOF &&
         (c == ' ' || c == '\t' || c == '\r' || c == '\n')) in.get();
  return c == EOF ;
}

inline
void Readln(std::istream &in) {
  int c(0);
  do c = in.get(); while (c != '\n' && c != EOF);
}

template<typename T> void MakeUnique(T &V) {
  sort(V.begin(), V.end());
  V.erase(unique(V.begin(), V.end()), V.end());
}

////////////////////////////////////////////////////////////////////////

std::ifstream fin;
std::ofstream fout;

string SetFile(string s) {
  while (!s.empty() && s[0] <= ' ' ) s.erase(0, 1);
  while (!s.empty() && s[s.size() - 1] <= ' ' ) s.erase(s.size() - 1) ;
  const string::size_type p = s.find('.') ;
  if (p != string::npos) s = s.substr(0, p);
  //CHECK(freopen((s + ".in" ).c_str(), "r", stdin) != NULL); 
  //CHECK(freopen((s + ".out").c_str(), "w", stdout) != NULL);
  fin.open((s + ".in" ).c_str());  CHECK(fin);
  fout.open((s + ".out").c_str());  CHECK(fout);
  return s;
}

// push_back
