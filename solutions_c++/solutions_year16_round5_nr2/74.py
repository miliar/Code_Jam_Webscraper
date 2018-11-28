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

template <class T>
inline void hash_combine(size_t& seed, T const& v) {
  seed ^= hash<T>()(v) + 0x9e3779b9 + (seed<<6) + (seed>>2);
}

namespace std {
  namespace {
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

// --- BEGIN SNIPPET AHO CORASICK ---

template<class U>
struct aho_corasick {

  struct node {
    unordered_map<lli, lli> nexts;
    lli back;
    unordered_set<lli> ends;
  };

  vector<node> T;

  aho_corasick(vector<U> const& W){
    T.pb(node());
    FOR(i, W.size()){
      lli n = 0;
      for(lli c : W[i]){
        if(T[n].nexts.count(c) == 0){
          T[n].nexts[c] = T.size();
          T.pb(node());
        }
        n = T[n].nexts[c];
      }
      T[n].ends.insert(i);
    }
    // ---
    queue<lli> q; q.push(0);
    T[0].back = -1;
    while(!q.empty()){
      lli n = q.front(); q.pop();
      // Remove this line if only the largest match at each position is needed
      if(T[n].back != -1) for(auto i : T[T[n].back].ends) T[n].ends.insert(i);
      // ---
      for(auto p : T[n].nexts){
        lli b = T[n].back;
        while(b != -1 && T[b].nexts.count(p.first) == 0)
          b = T[b].back;
        T[p.second].back = (b==-1)?0:T[b].nexts[p.first];
        q.push(p.second);
      }
    }
  }

  lli next(lli S, lli x){
    while(S != -1 && T[S].nexts.count(x) == 0) S = T[S].back;
    return (S==-1)?0:T[S].nexts[x];
  }

  vi states(U const& A) {
    lli S = 0;
    vi R(A.size());
    FOR(i, A.size()){
      S = next(S, A[i]);
      R[i] = S; // occurences at i are aho.T[R[i]].ends
    }
    return R;
  }

};

// --- END SNIPPET AHO CORASICK ---



void solve(){
  int n; cin >> n;
  int P[n]; FOR(i, n) cin >> P[i];
  vvi G(n); FOR(i, n) if(P[i]!=0) G[P[i]-1].pb(i);

  vi D(n, 1);

  vi I;
  { vi A;
    FOR(i, n) if(P[i] == 0) A.pb(i);
    while(!A.empty()) {
      int i = A.back(); A.pop_back();
      I.pb(i);
      for(int j : G[i]) {
        A.pb(j);
      }
    }
  }
  vi J(n); FOR(i, n) J[I[i]] = i;
  FORD(i, n-1, 0) if(P[I[i]]) D[P[I[i]]-1] += D[I[i]];

  string S; cin >> S;
  int m; cin >> m;
  vector<string> A(m); FOR(i, m) cin >> A[i];
  aho_corasick<string> AC(A);
  vi pos(n);
  const lli niter = 20000;
  int nr[m]; FOR(i, m) nr[i] = 0;
  FOR(i, niter) {
    vi A; int sl = 0;
    FOR(i, n) if(P[i] == 0) {
      A.pb(i);
      sl+= D[i];
    }
    string C;
    while(!A.empty()) {
      int j0 = rand()%sl;
      int cl = 0;
      FOR(k, A.size()) {
        cl += D[A[k]];
        if(cl>j0) {
          swap(A[k], A.back());
          break;
        }
      }
      int i = A.back(); A.pop_back();
      sl -= D[i];
      C.pb(S[i]);
      for(int j : G[i]) {
        A.pb(j); sl += D[j];
      }
    }

    // FOR(j, n) {
    //   lli from = 0, to = j;
    //   if(P[I[j]]) {
    //     from = pos[J[P[I[j]]-1]]+1;
    //   }
    //   pos[j] = from + rand()%(to-from+1);
    //   FOR(k, j) if(pos[k]>=pos[j]) pos[k] += 1;
    //   cout << pos << endl;
    // }
    // string C(n, 0);
    // FOR(i, n) C[pos[i]] = S[I[i]];
    // cout << C << endl;

    bool E[m]; FOR(i, m) E[i] = 0;
    vi R = AC.states(C);
    for(int i : R) for(int j : AC.T[i].ends) E[j] = 1;
    FOR(i, m) if(E[i]) nr[i] += 1;
  }
  FOR(i, m) cout << setprecision(5) << (double)nr[i]/(double)niter << " ";
  cout << endl;
}

int main(int, char**){
  srand(time(0));
  int t; cin >> t;
  FOR(i, t) {
    cout << "Case #" << (i+1) << ": ";
    solve();
  }
  return 0;
}
