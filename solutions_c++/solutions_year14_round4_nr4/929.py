#include <algorithm>
#include <bitset>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

#define repi(i, a, b) for(int i = (a); i < (b); i++)
#define rep(i, a) repi(i, 0, a)
#define repd(i, a, b) for(int i = (a); i >= (b); i--)
#define repit(i, v) for(__typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)
#define reprit(i, v) for(__typeof((v).rbegin()) i = (v).rbegin(); i != (v).rend(); i++)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define UNIQUE(v) (v).erase(unique(all(v)), (v).end())
#define pb push_back
#define mp make_pair
#define PI acos(-1.0)
#define to_str(v) #v
using namespace std;
typedef long long ll;

template<class X>
ostream& operator<<(ostream& os, const vector<X> &v) {
  repit(itr, v) cout << *itr << " ";
  cout << " size : " << v.size();;
  return os;
}

int m, n;

int calcnum(vector<string> s) {
  set<string> st;
  //  st.insert("");
  rep(i, s.size()) {
    rep(j, s[i].size()) {
      st.insert(s[i].substr(0, j));
    }
  }
  return st.size();
}

int rec(vector<string> &v, int now, vector<vector<string> > s) {
  int ret = 0;
  if(now == m) {
    //rep(i, n) if(s[i].size() == 0) return 0;
    rep(i, n) ret += calcnum(s[i]);
    return ret;
  }
  
  rep(i, n) {
    vector<vector<string> > ts = s;
    ts[i].pb(v[now]);
    ret = max(ret, rec(v, now+1, ts));
  }
  return ret;
}

int num;
int rec2(vector<string> &v, int now, vector<vector<string> > s) {
  int ret = 0;
  if(now == m) {
    //rep(i, n) if(s[i].size() == 0) return 0;
    rep(i, n) ret += calcnum(s[i]);
    if(ret == num) {
      return 1;
    }else return 0;
  }

  rep(i, n) {
    vector<vector<string> > ts = s;
    ts[i].pb(v[now]);
    ret += rec2(v, now+1, ts);
  }
  return ret;
}

void solve() {
  // input
  cin >> m >> n;
  vector<string> v(m);
  rep(i, m) cin >> v[i];
  rep(i, m) v[i] += '#';

  // calc node number
  vector<vector<string> > s(n);
  num = rec(v, 0, s);
  int ans = rec2(v, 0, s);
  cout << num << " " << ans << endl;
  cerr << num << " " << ans << endl;
}

int main() {
  int T;
  cin >> T;
  rep(i, T) {
    cout << "Case #" << i+1 << ": ";
    solve();
  }
  return 0;
}
