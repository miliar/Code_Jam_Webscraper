#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;
typedef long long ll;
#define sz(a)  int((a).size())
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define tr(i,c)  for(auto i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define found(s,e)  ((s).find(e)!=(s).end())

//#include "cout11.h"

ll rev(ll x){
	//cout << x << " ";
	vector<int> ds;
	while(x){
		ds.pb(x%10); x/=10;
	}
	//cout << ds;
	ll y = 0;
	tr(it,ds){
		y*=10; y+=(*it);
	}
	//cout << " " << y << endl;
	return y;
}

ll solve(ll n){
	vector<ll> dp(n+1);
	rep(i,n+1) dp[i]=i;
	for (ll i=1; i<n; ++i){
		ll x=dp[i];
		dp[i+1] = min(dp[i+1], x+1);
		ll r=rev(i);
		if (r <= n) {
			dp[r] = min(dp[r], x+1);
		}
	}
	return dp[n];
}

int main()
{
  int _T; cin >> _T; // 1-100
  for (int _t=1; _t<=_T; ++_t) {
    ll N; cin >> N; // 1e6,1e14
 answer:
    cout << "Case #" << _t << ": " << solve(N) << endl;
  }
}
