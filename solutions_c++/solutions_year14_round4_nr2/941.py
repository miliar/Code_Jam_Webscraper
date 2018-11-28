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
  ll n; cin >> n;
  vector<ll> A(n); FOR(i, n) cin >> A[i];
  vector<ll> I(n); FOR(i, n) I[i] = i;
  sort(I.begin(), I.end(), [&](ll const& a, ll const& b){
    return A[a] < A[b];
  });
  ll r = 0;
  set<ll> B, C;
  FOR(i, n){
    auto bit = B.lower_bound(I[i]);
    auto cit = C.lower_bound(I[i]);
    auto bcost = (I[i] - distance(C.begin(), cit) + distance(bit, B.end())) - B.size();
    auto ccost = n-1-C.size() - (I[i] - distance(C.begin(), cit) + distance(bit, B.end()));
    // cout << I[i] << " " << bcost << " " << ccost << " " << r << endl;
    if(bcost < ccost){
      r += bcost;
      B.insert(I[i]);
    }else{
      r += ccost;
      C.insert(I[i]);
    }
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