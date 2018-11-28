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

bool solve(int tc){
  cout << "Case #" << tc << ": ";
  int N, R, P, S;
  cin >> N >> R >> P >> S;

  map<char, multiset<string>> cur;
  rep(i,0,R) cur['R'].insert("R");
  rep(i,0,P) cur['P'].insert("P");
  rep(i,0,S) cur['S'].insert("S");
  rep(i,0,N) {
    map<char, multiset<string>> ncur;
    int rs = sz(cur['R']);
    int ps = sz(cur['P']);
    int ss = sz(cur['S']);
    if (max(rs, max(ps, ss)) > (rs + ps + ss) / 2) goto nope;

    // cout << rs << " " << ps << " " << ss << endl;
    int rpc = ((rs + ps + ss) - 2*ss)/2;
    int rsc = ((rs + ps + ss) - 2*ps)/2;
    int psc = ((rs + ps + ss) - 2*rs)/2;
    // cout << rpc << " " << rsc << " " << psc << endl;
    while (rpc + rsc + psc) {
      auto rstr = cur['R'].begin();
      auto pstr = cur['P'].begin();
      auto sstr = cur['S'].begin();
      string rps = !rpc ? "Z" : (min(*rstr, *pstr) + max(*rstr, *pstr));
      string pss = !psc ? "Z" : (min(*pstr, *sstr) + max(*pstr, *sstr));
      string rss = !rsc ? "Z" : (min(*rstr, *sstr) + max(*rstr, *sstr));
      if (rpc && rps <= pss && rps <= rss) {
        ncur['P'].insert(rps);
        cur['R'].erase(rstr);
        cur['P'].erase(pstr);
        rpc--;
      } else if (psc && pss <= rps && pss <= rss) {
        ncur['S'].insert(pss);
        cur['S'].erase(sstr);
        cur['P'].erase(pstr);
        psc--;
      } else if (rsc) {
        ncur['R'].insert(rss);
        cur['S'].erase(sstr);
        cur['R'].erase(rstr);
        rsc--;
      } else {
        goto nope;
      }
    }

    cur.swap(ncur);
  }
  cout << *(cur.begin()->second.begin()) << endl;
  return true;
nope:
  cout << "IMPOSSIBLE" << endl;
  return true;
}

int main() {
  cin.sync_with_stdio(false); cin.tie(NULL);
  int n = 1<<30;
  cin >> n;
  for(int i = 1; i <= n && solve(i); ++i);
}
