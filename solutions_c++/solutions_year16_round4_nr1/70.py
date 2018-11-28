#pragma GCC optimize ("-O3")
#define _GLIBCXX_USE_CXX11_ABI 0
#include <bits/stdc++.h>

// #include <lemon/cbc.h>
// using namespace lemon;

// #include <boost/multiprecision/gmp.hpp>
// using namespace boost::multiprecision;

#define FOR(i, n)     for(lli i = 0; i < (lli)(n); ++i)
#define FORU(i, j, k) for(lli i = (j); i <= (lli)(k); ++i)
#define FORD(i, j, k) for(lli i = (j); i >= (lli)(k); --i)

#define DESTRUCT2(t, x, y)                      \
  auto x = get<0>(t);                           \
  auto y = get<1>(t);

#define DESTRUCT3(t, x, y, z)                   \
  auto x = get<0>(t);                           \
  auto y = get<1>(t);                           \
  auto z = get<2>(t);

#define DESTRUCT4(t, x, y, z, w)                \
  auto x = get<0>(t);                           \
  auto y = get<1>(t);                           \
  auto z = get<2>(t);                           \
  auto w = get<3>(t);

#define SQ(x) ((x)*(x))

#define all(x) begin(x), end(x)
#define rall(x) rbegin(x), rend(x)
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back

#define PE flush << "\033[2K\r"

using namespace std;
using lli   = long long int;
using llu   = long long unsigned;

using pii   = tuple<lli, lli>;
using piii  = tuple<lli, lli, lli>;
using piiii = tuple<lli, lli, lli, lli>;
using vi    = vector<lli>;
using vii   = vector<pii>;
using viii  = vector<piii>;
using vvi   = vector<vi>;
using vvii  = vector<vii>;
using vviii = vector<viii>;

template<class T>
using min_queue = priority_queue<T, vector<T>, greater<T> >;

template<class T>
using max_queue = priority_queue<T>;

template<class T, size_t... I>
void print_tuple(ostream& s, T const& a, index_sequence<I...>){
  using swallow = int[];
  (void)swallow{0, (void(s << (I == 0? "" : ", ") << get<I>(a)), 0)...};
}

template<class T>
ostream& print_collection(ostream& s, T const& a){
  s << '[';
  for(auto it = begin(a); it != end(a); ++it){
    s << *it;
    if(it != prev(end(a))) s << " ";
  }
  return s << ']';
}

template<class... A>
ostream& operator<<(ostream& s, tuple<A...> const& a){
  s << '(';
  print_tuple(s, a, index_sequence_for<A...>{});
  return s << ')';
}

template<class A, class B>
ostream& operator<<(ostream& s, pair<A, B> const& a){
  return s << "(" << get<0>(a) << ", " << get<1>(a) << ")";
}

template<class T, int I>
ostream& operator<<(ostream& s, array<T, I> const& a) { return print_collection(s, a); }
template<class T>
ostream& operator<<(ostream& s, vector<T> const& a) { return print_collection(s, a); }
template<class T, class U>
ostream& operator<<(ostream& s, multimap<T, U> const& a) { return print_collection(s, a); }
template<class T>
ostream& operator<<(ostream& s, multiset<T> const& a) { return print_collection(s, a); }
template<class T, class U>
ostream& operator<<(ostream& s, map<T, U> const& a) { return print_collection(s, a); }
template<class T>
ostream& operator<<(ostream& s, set<T> const& a) { return print_collection(s, a); }

namespace std {
  namespace {
    template <class T>
    inline void hash_combine(size_t& seed, T const& v) {
      seed ^= hash<T>()(v) + 0x9e3779b9 + (seed<<6) + (seed>>2);
    }
    template <class Tuple, size_t Index = tuple_size<Tuple>::value - 1>
      struct HashValueImpl {
        static void apply(size_t& seed, Tuple const& tuple) {
          HashValueImpl<Tuple, Index-1>::apply(seed, tuple);
          hash_combine(seed, get<Index>(tuple));
        }
      };
    template <class Tuple>
    struct HashValueImpl<Tuple, 0> {
      static void apply(size_t& seed, Tuple const& tuple) {
        hash_combine(seed, get<0>(tuple));
      }
    };
  }
  template <typename ... TT>
  struct hash<tuple<TT...>> {
    size_t operator()(tuple<TT...> const& tt) const {
      size_t seed = 0;
      HashValueImpl<tuple<TT...> >::apply(seed, tt);
      return seed;
    }
  };
}

//------------------------------------------------------------------------------

void solve(){
  lli n; cin >> n;
  lli a[3]; cin >> a[1] >> a[0] >> a[2];
  char *C = "PRS";
  assert((1ll<<n)==a[0]+a[1]+a[2]);
  vector<string> S;
  FOR(i, 3) {
    lli b[3]; FOR(i, 3) b[i] = a[i];
    function<tuple<bool, string>(lli, lli)> ok = [&](lli i, lli n) -> tuple<bool, string> {
      if(n == 0) {
        if(b[i] == 0) return mt(false, "");
        b[i] -= 1;
        string s; s += C[i]; return mt(true, s);
      }else{
        auto s1 = ok(i, n-1);
        auto s2 = ok((i+1)%3, n-1);
        if(get<0>(s1)&&get<0>(s2)) {
          if(get<1>(s1)<get<1>(s2)){
            return mt(true, get<1>(s1)+get<1>(s2));
          }else{
            return mt(true, get<1>(s2)+get<1>(s1));
          }
        }else{
          return mt(false, "");
        }
      }
    };
    auto s = ok(i, n);
    if(get<0>(s)) S.pb(get<1>(s));
  }
  sort(all(S));
  if(S.empty()) {
    cout << "IMPOSSIBLE" << endl;
  }else{
    cout << S[0] << endl;
  }
}

int main(int, char**){
  ios::sync_with_stdio(0);

  lli t; cin >> t;
  FOR(i, t) {
    cout << "Case #" << i+1 << ": ";
    solve();
  }

  return 0;
}
