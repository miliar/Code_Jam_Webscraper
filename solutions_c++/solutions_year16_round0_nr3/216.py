#pragma GCC optimize ("-O3")
#define _GLIBCXX_USE_CXX11_ABI 0
#include <bits/stdc++.h>

#include <boost/multiprecision/gmp.hpp>
#include <gmp.h>
#include <ecm.h>
#include <boost/multiprecision/miller_rabin.hpp>

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

template<int... I>
struct my_index_sequence {
  using type = my_index_sequence;
  static constexpr array<int, sizeof...(I)> value = { I... };
};

namespace my_index_sequence_detail {
  template<typename I, typename J> struct concat;
  template<int... I, int... J>
  struct concat<my_index_sequence<I...>, my_index_sequence<J...> > :
    my_index_sequence<I..., (sizeof...(I)+J)...> { };
  template<int N> struct make_index_sequence :
    concat<typename make_index_sequence<N/2>::type, typename make_index_sequence<N-N/2>::type>::type { };
  template <> struct make_index_sequence<0> : my_index_sequence<>{};
  template <> struct make_index_sequence<1> : my_index_sequence<0>{};
}

template<class... A>
using my_index_sequence_for = typename my_index_sequence_detail::make_index_sequence<sizeof...(A)>::type;

template<class T, int... I>
void print_tuple(ostream& s, T const& a, my_index_sequence<I...>){
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
  print_tuple(s, a, my_index_sequence_for<A...>{});
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

inline llu mult_mod(llu x, llu y, llu M) {
  llu z;
  asm("mul %[y]\n\t"
      "div %[M]"
      : "=&d"(z), "=a"(x)
      : "a"(x), [y] "r"(y), [M] "r"(M));
  return z;
}

lli ipow(lli a, lli n, lli M) {
  if(n == 0) return 1;
  lli x = ipow(mult_mod(a, a, M), n/2, M);
  return n%2 ? mult_mod(a, x, M) : x;
}

bool strong_probable_prime(lli n, lli a) {
  if(n == a) return true;
  int s = __builtin_ctz(n-1);
  lli d = (n-1) >> s;
  if(ipow(a, d, n) == 1) return true;
  FOR(r, s)
    if(ipow(a, d<<r, n) == n-1)
      return true;
  return false;
}

bool is_prime(lli n) {
  if(n != 2 && n % 2 == 0) return 0;
  if(n == 46856248255981) return 0;
  if(!strong_probable_prime(n, 2)) return 0;
  if(!strong_probable_prime(n, 3)) return 0;
  if(!strong_probable_prime(n, 7)) return 0;
  if(!strong_probable_prime(n, 61)) return 0;
  if(!strong_probable_prime(n, 24251)) return 0;
  return 1;
}

int main(int, char**){
  ecm_params ep; ecm_init(ep);

  ios::sync_with_stdio(0);

  using namespace boost::multiprecision;
  boost::random::mt19937 gen2(clock());

  cout << "Case #1:\n";
  int nr = 0;
  FORU(i, 1<<31, 1ll<<32ll) if((i&1) && (i&(1<<31))) {
    vector<mpz_int> fcs;
    FORU(b, 2, 10) {
      mpz_int n = 0;
      FORD(j, 31, 0) {
        n = b * n + ((i&(1<<j))?1:0);
      }
      if(miller_rabin_test(n, 25, gen2)) goto l_end;
    }
    FORU(b, 2, 10) {
      mpz_int n = 0;
      FORD(j, 31, 0) n = b*n + ((i&(1<<j))?1:0);

      mpz_int m = -1;
      ecm_factor(m.backend().data(), n.backend().data(), 1.0, ep);
      if(m == -1) goto l_end;
      fcs.pb(m);
    }
    cout << bitset<32>(i) << " ";
    for(auto j : fcs) cout << j << " ";
    cout << endl;
    nr += 1;
    if(nr == 500) return 0;
  l_end:;
  }

  return 0;
}
