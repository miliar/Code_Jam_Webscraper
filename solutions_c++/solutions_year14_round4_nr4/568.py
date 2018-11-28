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
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <queue>
#include <cstring>
#include <limits>
using namespace std;

#define Loop(i,n) for (int i = 0; i < (int)(n); ++i)
#define Loopa(i,a,b) for (int i = (a); i <= (b); ++i)
#define Loopd(i,a,b) for (int i = (a); i >= (b); --i)
template <typename T, typename Q, typename S>
bool Bounded(const T& x, const Q& a, const S& b) { return a <= x && x <= b; }
#define db(x) #x << " = " << x
#define pdb(x) printf("#x = %d\n",x);
#define All(x) x.begin(),x.end()
template <typename T> int sz(const T& x) { return x.size(); }
template <typename T, typename Q>
bool mem(const T& s, const Q& x) { return s.find(x) != s.end(); }
typedef long double ld;
typedef long long int ll;
typedef vector<int> Vi;
typedef vector<ll> Vll;
typedef pair<int,int> Pii;
typedef vector<Vi> Adj;
typedef vector<bool> Vb;
#define CI(x) x::const_iterator
#define II(x) x::iterator
#define Car(x) (x).first
#define Cdr(x) (x).second
#define Caar(x) (x).first.first
#define Cdar(x) (x).first.second
#define Cadr(x) (x).second.first
#define Cddr(x) (x).second.second
template <typename T>
struct leq_by {
  const vector<T>* v;
  leq_by(const vector<T>& v) : v(&v) { }
  bool operator()(int i, int j) { return v->at(i) < v->at(j); }
};
template <typename T> void read(vector<T>& x) { Loop(i,sz(x)) cin >> x[i]; }
template <typename T> vector<T> readn(int n) { vector<T> x(n); Loop(i,n) cin >> x[i]; return x; }
template <typename T> void umin(T& x, const T& y) { x = min(x, y); }
template <typename T> void umax(T& x, const T& y) { x = max(x, y); }

bool debug = true;
#define dprintf debug && printf
void show(string s, Vi x) {
  if (!debug) return; cout << s << ": "; Loop(i,sz(x)) cout << " " << x[i]; cout << endl;
}

void solve_correct(int casenum) {
  dprintf("==================================================% 3d\n", casenum);



  printf("Case #%d: \n", casenum);
  fflush(NULL);
}

int intpow(int a, int b) {
  if (b == 0) return 1;
  if (b == 1) return a;
  if (b&1) return a * intpow(a*a, b/2);
  return intpow(a*a, b/2);
}

int evaltrie(const vector<string>& S) {
  assert(!S.empty());
  set<string> x;
  for (const string& s : S) {
    for (int k = 0; k <= s.size(); ++k) {
      // cout << s << ": " << s.substr(0, k) << endl;
      x.insert(s.substr(0, k));
    }
  }
  // cout << "evaltrie:"; for (string s : S) cout << " " << s; cout << " -> " << x.size() << endl;
  return x.size();
}

void solve(int casenum) {
  dprintf("==================================================% 3d\n", casenum);

  int M, N; cin >> M >> N;
  vector<string> S(M); Loop(i,M) cin >> S[i];

  Vi vals;
  for (int i = 0; i < intpow(N, M); ++i) {
    vector< vector<string> > T(N);
    int j = i;
    Loop(k, M) {
      T[j%N].push_back(S[k]);
      // cout << S[k] << " -> " << j%N << endl;
      j /= N;
    }
    bool valid = true;
    Loop(k, N) valid = valid && !T[k].empty();
    if (!valid) continue;
    int cost = 0;
    Loop(k,N) cost += evaltrie(T[k]);
    vals.push_back(cost);
  }
  // dprintf("Total number of combinations: %d\n", (int)vals.size());
  assert(!vals.empty());

  int worst_cost = *max_element(All(vals));
  int num_worst = count(All(vals), *max_element(All(vals)));

  printf("Case #%d: %d %d\n", casenum, worst_cost, num_worst);
  fflush(NULL);
}

int main(int argc, char** argv) {
  if (getenv("NODEBUG") != NULL) debug = false;
  int T; cin >> T;
  if (getenv("CORRECT") != NULL) {
    Loop(i,T) solve_correct(i+1);
  } else {
    Loop(i,T) solve(i+1);
  }
  return 0;
}

// Local variables:
// compile-command: "g++ -Wall -g -o D D.cc"
// End:
