#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <list>
#include <bitset>
#include <set>
#include <queue>
#include <stack>

using namespace std;

#define ll long long
#define ull unsigned long long

#define FOR(i, n) for(ll i = 0; i < (n); ++i)
#define FORU(i, j, k) for(ll i = j; i <= (k); ++i)
#define FORD(i, j, k) for(ll i = j; i >= (k); --i)

#define pf push_front
#define pb push_back

#define mp make_pair
#define F first
#define S second

// --- --- ---

ll solve(){
  ll n, x; cin >> n >> x;
  multiset<ll, greater<ll>> A;
  FOR(i, n) { ll y; cin >> y; A.insert(y); }
  ll r = 0;
  while(!A.empty()){
    auto it = A.begin();
    ll s = *it;
    A.erase(it);
    auto oit = A.lower_bound(x - s);
    if(oit != A.end()) A.erase(oit);
    r += 1;
  }
  return r;
}

int main(int, char**){
  ios::sync_with_stdio(false);
  ll nTest; cin >> nTest;
  FOR(t, nTest){
    cout << "Case #" << (t+1) << ": " << solve() << endl;
  }
  return 0;
}