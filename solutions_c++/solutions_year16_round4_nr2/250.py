#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < int(b); ++i)
#define trav(a, v) for(auto& a : v)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
#define D(x) cerr << #x << " = " << x << endl

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpi;

template<typename T, typename U> static inline void smin(T &x, U y) {if(y < x) x = y; }
template<typename T, typename U> static inline void smax(T &x, U y){ if(y > x) x = y; }
template<typename T> istream& operator>>(istream& in, vector<T> &v) { rep(i,0,v.size()) in >> v[i]; return in; }
template<typename A, typename B> istream& operator>>(istream& in, pair<A, B> &p) { in >> p.first >> p.second; return in; }
template<typename T> ostream& operator<<(ostream& out, vector<T> &v) { if(v.size()) out << v[0]; rep(i,1,v.size()) out << ' ' << v[i]; return out; }
template<typename A, typename B> ostream& operator<<(ostream& out, pair<A, B> &p){ out << p.first << ' ' << p.second; return out; }

long double compute(vector<long double> P) {
  vector<long double> pps(sz(P) + 1);
  pps[0] = 1;
  trav(it, P) {
    vector<long double> pps2(sz(P) + 1);
    rep(i,0,sz(P)) {
      pps2[i] += (1 - it) * pps[i];
      pps2[i + 1] += it * pps[i];
    }
    pps.swap(pps2);
  }
  return pps[sz(P)/2];
}

bool solve(int i){
  cout << "Case #" << i << ": ";
  int N, K;
  cin >> N >> K;
  vector<long double> V(N);
  rep(i,0,N) {
    cin >> V[i];
  }
  sort(all(V));
  long double mx = 0;
  rep(i,0,K+1) {
    vector<long double> ans;
    rep(j,0,i) ans.push_back(V[j]);
    rep(j,0,K-i) ans.push_back(V[N - 1 - j]);
    mx = max(mx, compute(ans));
  }
  cout << fixed << setprecision(10);
  cout << mx << endl;
  return true;
}

int main() {
  cin.sync_with_stdio(false); cin.tie(NULL);
  int n = 1<<30;
  cin >> n;
  for(int i = 1; i <= n && solve(i); ++i);
}
