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
using namespace std;

#define all(v) (v).begin(),(v).end()
#define forint(i,c,d) for (int i=(c); i<=(d); ++i)
#define forall(i,V) for (int i=0; i<(V).size(); ++i)
#define foritr(p,V) for(__typeof((V).end()) p=(V).begin(); p!=(V).end(); ++p)
#define showall(V) { cerr<<#V<<": ";foritr(p, (V))cerr<<*(p)<<" ";cerr<<endl; }
#define showvar(x) { cerr<<#x<<" = "<<(x)<<endl; }

typedef long long int64;
template<class T> void CheckMin(T&a, const T&b) { if (b<a) a=b; }
template<class T> void CheckMax(T&a, const T&b) { if (a<b) a=b; }


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

// push_back

bool IsPalin(const int64 x) {
  const string s = ToString(x);
  int h = 0, e = s.size() - 1;
  while (h < e && s[h] == s[e]) ++h, --e;
  return h >= e;
}

std::vector<int64> all;

void Init() {
  all.clear();
  forint (i, 1, 10000000) {
    if (IsPalin(i) && IsPalin(static_cast<int64>(i)*i)) all.push_back(static_cast<int64>(i)*i);
  }
}

void Readin() {  // process one case
  int64 a, b;
  fin >> a >> b;
  fout << (upper_bound(all.begin(), all.end(), b) -
           upper_bound(all.begin(), all.end(), a - 1)) << endl;
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


int main() {
  const string main_filename = SetFile(/*@*/" C-large-1         ");

  int num_test;  fin >> num_test;
  assert(Eoln(fin));  Readln(fin);
  
  Init();
  
  showvar(num_test);
  forint (number, 1, num_test) { 
    fout << "Case #" << number << ": ";
    cerr << "Running on Case #" << number << endl;


    Readin();
    //Work();
    //fout << ans << endl;
  }

  if (!SeekEof(fin)) ABORT("Wrong! Not at EOF!");
  fclose(stdin);
  fclose(stdout);

  cerr << "\n\n---------- OUTPUT of " + main_filename + ": ----------" << endl;
  system(("cat " + main_filename + ".out >&2").c_str());
  return 0;
}

