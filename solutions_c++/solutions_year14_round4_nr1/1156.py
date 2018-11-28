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

int solve() {
  int x, n;
  cin >> n >> x;
  vector<int> s(n);
  rep(i, n) cin >> s[i];
  sort(rall(s));
  int ans = 0;
  vector<int> v;
  rep(i, n) {
    bool ok = false;
    rep(j, v.size()) {
      if(v[j] + s[i] <= x) {
	ok = true;
	v[j] = 1000000;
	break;
      }
    }
    if(!ok) {
      v.pb(s[i]);
      ans++;
    }
  }
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
