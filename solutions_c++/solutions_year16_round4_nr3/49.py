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
  lli r, c; cin >> r >> c;
  char S[r][c]; FOR(i, r) FOR(j, c) S[i][j] = '.';
  lli nc = 2*(r+c);
  vi Q;
  lli to[nc];
  vi done(nc, 0);
  vi done2(nc, 0);
  FOR(i, r+c) {
    lli a, b; cin >> a >> b; a -= 1; b -= 1;
    if(b == (a+1)%nc) { done[a] = 1; done[b] = 1; Q.pb(a); }
    else if(a == (b+1)%nc) { done[a] = 1; done[b] = 1; Q.pb(b); }
    to[a] = b;
    to[b] = a;
  }
  lli ndone = 0;
  enum dir {
    UP, DOWN, LEFT, RIGHT
  };
  auto gpos = [&](lli i) -> pii{
    if(i<c) return mt(0,i);
    if(i<c+r) return mt(i-c,c-1);
    if(i<c+r+c) return mt(r-1,c-1-(i-r-c));
    return mt(r-1-(i-r-c-c),0);
  };
  auto gdir = [&](lli i){
    if(i<c) return DOWN;
    if(i<c+r) return LEFT;
    if(i<c+r+c) return UP;
    return RIGHT;
  };

  while(!Q.empty()) {
    lli i = Q.back(); Q.pop_back();
    //cerr << "# " << i+1 << " " << to[i]+1 << endl;
    ndone += 1;
    done2[i] = 1; done2[to[i]] = 1;

    pii pos = gpos(i);
    //cerr << i << " " << pos << endl;
    dir d = gdir(i);
    DESTRUCT2(pos, x, y);
    while(0<=x&&x<r&&0<=y&&y<c){
      //cerr << x << " " << y << endl;
      switch(d){
      case UP:
        if(S[x][y] == '.') S[x][y] = '\\';
        if(S[x][y] == '\\') {
          y -= 1; d = LEFT;
        }else{
          y += 1; d = RIGHT;
        }
        break;
      case DOWN:
        if(S[x][y] == '.') S[x][y] = '\\';
        if(S[x][y] == '/') {
          y -= 1; d = LEFT;
        }else{
          y += 1; d = RIGHT;
        }
        break;
      case LEFT:
        if(S[x][y] == '.') S[x][y] = '/';
        if(S[x][y] == '/') {
          x += 1; d = DOWN;
        }else{
          x -= 1; d = UP;
        }
        break;
      case RIGHT:
        if(S[x][y] == '.') S[x][y] = '/';
        if(S[x][y] == '\\') {
          x += 1; d = DOWN;
        }else{
          x -= 1; d = UP;
        }
        break;
      };
    }
    //cerr << x << " " << y << endl;

    lli dest = -1;
    if(x<0) dest = y;
    else if(y>=c) dest = c+x;
    else if(x>=r) dest = r+c+(c-1-y);
    else if(y<0) dest = c+r+c+(r-1-x);
    else assert(false);
    //cerr << i+1 << " " << dest+1 << " " << to[i]+1 << endl;
    if(dest != to[i]) {

      cout << "\nIMPOSSIBLE" << endl;
      return;
    }

    lli a = (i-1+nc)%nc, b = (to[i]+1)%nc;
    while(a!=i&&done2[a]) a = (a+nc-1)%nc;
    while(b!=i&&done2[b]) b = (b+1)%nc;
    if(to[a] == b && !done[a]) {
      Q.pb(a);
      done[a] = 1; done[b] = 1;
    }
  }
  if(ndone == r+c) {
    cout << "\n";
    FOR(i, r) FOR(j, c) if(S[i][j]=='.') S[i][j]='/';
    FOR(i, r) { FOR(j, c) cout << S[i][j]; cout << "\n"; }
    cout << flush;
  }else{



    cout << "\nIMPOSSIBLE" << endl;
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
