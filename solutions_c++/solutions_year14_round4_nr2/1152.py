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

const int MAX = 1005;
int bit[MAX+1], N;

int sum(int i) {
  int s = 0;
  while(i > 0) {
    s += bit[i];
    i -= i & -i;
  }
  return s;
}

void add(int i, int x) {
  while(i <= N) {
    bit[i] += x;
    i += i & -i;
  }
}

ll calc(vector<int> v) {
  reverse(all(v));
  ll ret = 0;
  memset(bit, 0, sizeof(bit));
  N = 1005;
  rep(i, v.size()) {
    ret += sum(v[i]+1);
    add(v[i]+1, 1);
  }
  return ret;
}

int solve() {
  int n;
  // input
  cin >> n;
  vector<int> v(n);
  rep(i, n) cin >> v[i];

  // zip
  set<int> st;
  rep(i, n) st.insert(v[i]);
  map<int, int> zip;
  int cnt = 0;
  repit(itr, st) {
    zip[*itr] = cnt;
    cnt++;
  }
  rep(i, n) v[i] = zip[v[i]];
  

  /*  rep(i, n) cout << v[i] << " ";
      cout << endl;*/

  ll ans = 10000000000000LL;

  // for small
  vector<int> pos(n);
  rep(i, n) pos[v[i]] = i;
  
  //  rep(i, n) cout << v[i] << " ";
  //  cout << endl;

  rep(S, 1<<n) {
    vector<int> v1, v2;
    rep(i, n) if((S>>i)&1) {
      v1.pb(v[i]);
    } else {
      v2.pb(v[i]);
    }
    sort(all(v1));
    sort(rall(v2));
    vector<int> tv;
    rep(i, v1.size()) tv.pb(v1[i]);
    rep(i, v2.size()) tv.pb(v2[i]);
    ll tmp = 0;

    memset(bit, 0, sizeof(bit));
    N = 20;
    rep(i, n) {
      tmp += sum(pos[tv[i]]+1);
      add(pos[tv[i]]+1, 1);
    }
    
    ans = min(ans, tmp);
  }
  
  // for large
  /*rep(i, n) {
    vector<int> v1;
    vector<int> v2;
    rep(j, i+1) v1.pb(v[j]);
    repd(j, n-1, i+1) v2.pb(v[j]);
    ans = min(ans, calc(v1) + calc(v2));
    }*/

  return ans;
}

int main() {
  int T;
  cin >> T;
  rep(i, T) {
    cout << "Case #" << i+1 << ": ";
    cout << solve() << endl;
  }
  return 0;
}
