#pragma GCC optimize ("-O3")
#define _GLIBCXX_USE_CXX11_ABI 0
#include <bits/stdc++.h>

#include <lemon/cbc.h>

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

// --- BEGIN SNIPPET MAX FLOW DINIC ---

struct MaxFlow {
  const lli infinity = numeric_limits<lli>::max();

  struct edge {
    edge(lli to_, lli c_) : to(to_), c(c_), f(0){ }
    lli to, c, f;
    edge* rev;
  };

  vector<vector<edge*>> G;

  MaxFlow(lli n = 0) : G(n){ }

  lli addNode() {
    G.eb();
    return G.size()-1;
  }

  edge* addEdge(lli a, lli b, lli c){
    edge* e1 = new edge(b, c);
    edge* e2 = new edge(a, 0);
    e1->rev = e2; e2->rev = e1;
    G[a].pb(e1); G[b].pb(e2);
    return e1;
  }

  lli flow(lli S, lli T){
    lli N = G.size();
    lli f = 0;
    vi D, W;
    while(1){
      // bfs
      D.assign(N, -1);
      queue<lli> Q; Q.push(S); D[S] = 0;
      while(!Q.empty()){
        lli i = Q.front(); Q.pop();
        for(edge *e : G[i]) if(e->c > e->f && D[e->to] == -1){
            D[e->to] = D[i] + 1;
            Q.push(e->to);
          }
      }
      if(D[T] == -1) return f;
      // dfs
      W.assign(N, 0);
      function<lli(lli, lli)> dfs = [&](lli i, lli f){
        if(i == T) return f;
        lli cf = 0;
        for(; W[i] < (lli)G[i].size(); W[i]++) {
          edge *e = G[i][W[i]];
          if(e->c > e->f && D[e->to] == D[i] + 1){
            lli df = dfs(e->to, min(f, e->c - e->f));
            if(df > 0){
              cf += df;
              f -= df;
              e->f += df;
              e->rev->f -= df;
            }
          }
        }
        return cf;
      };
      while(lli df = dfs(S, infinity)) f += df;
    }
  }
};

// --- END SNIPPET MAX FLOW DINIC ---


lli A[25][25];
lli B[25][25];

void solve(){
  lli n; cin >> n;
  FOR(i, n) FOR(j, n) {
    char c; cin >> c;
    A[i][j] = (c=='1')?1:0;
  }
  lli mn = 99999;
  FOR(i, 1<<(n*n)) {
    if(__builtin_popcountll(i) < mn) {
      FOR(a, n) FOR(b, n) {
        if(i&(1<<(n*a+b))){
          if(A[a][b]) goto l_end;
          B[a][b] = 1;
        } else B[a][b] = A[a][b];
      }
      lli i0 = i;
      FOR(i, n) {
        MaxFlow G(2+n+n);
        FOR(j, n) if(i != j) G.addEdge(0, 2+j, 1);
        FOR(j, n) if(B[i][j]) G.addEdge(2+n+j, 1, 1);
        FOR(i, n) FOR(j, n) if(B[i][j]) G.addEdge(2+i, 2+n+j, 1);
        lli f = G.flow(0, 1);
        lli f2 = 0; FOR(j, n) if(B[i][j]) f2 += 1;
        if(f == f2) goto l_end;
      }
      mn = min<lli>(mn, __builtin_popcountll(i));
    }
  l_end:;
  }
  cout << mn << endl;
}

// void solve(){
//   lli n; cin >> n;
//   FOR(i, n) FOR(j, n) {
//     char c; cin >> c;
//     A[i][j] = (c=='1')?1:0;
//   }
//   lli s = 0; FOR(i, n) FOR(j, n) s += A[i][j];
//   using namespace lemon;
//   using M = CbcMip;
//   M m;
//   M::Col V[25][25];
//   M::Col W[25][25][25];
//   auto addBinary = [&](){
//     M::Col c = m.addCol();
//     m.colLowerBound(c, 0);
//     m.colUpperBound(c, 1);
//     m.colType(c, M::INTEGER);
//     return c;
//   };
//   FOR(i, n) FOR(j, n) {
//     V[i][j] = addBinary();
//     if(A[i][j]) m.addRow(V[i][j] == 1);
//   }
//   FOR(i, n) {
//     M::Expr X[25];
//     M::Expr Y[25];
//     FOR(j, n) if(i != j) FOR(k, n) {
//         W[i][j][k] = addBinary();
//         m.addRow(W[i][j][k] <= V[j][k]);
//         m.addRow(W[i][j][k] <= V[i][k]);
//         X[j] += W[i][j][k];
//         Y[k] += W[i][j][k];
//       }
//     FOR(j, n) if(i != j) m.addRow(X[j] <= 1);
//     FOR(k, n) m.addRow(Y[k] <= 1);
//   }
//   { m.min();
//     M::Expr e; FOR(i, n) FOR(j, n) e += V[i][j];
//     FOR(i, n) FOR(j, n) if(i != j) FOR(k, n) e -= (1<<16) * W[i][j][k];
//     m.obj(e);
//   }
//   m.solve();
//   cout << m.solValue() << " " << (((lli)m.solValue())%(1<<16)+(1<<16))%(1<<16) << endl;
// }

int main(int, char**){
  ios::sync_with_stdio(0);

  lli t; cin >> t;
  FOR(i, t) {
    cout << "Case #" << i+1 << ": ";
    solve();
  }

  return 0;
}
