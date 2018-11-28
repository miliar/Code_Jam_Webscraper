#include <iostream>
#include <algorithm>
#include <map>
#include <string>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <bitset>
#include <random>
#include <cassert>
#include <cstdio>
#include <cstring>
using namespace std;
#define rep(i,a,b) for(int i = (a); i < int(b); ++i)
#define rrep(i,a,b) for(int i = (b); i --> int(a);)
#define allof(v) v.begin(),v.end()
#define pb push_back
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int,int> pii;
typedef vector<bool> vb;
typedef long double ld;

void solve(){
	int n,k;
	cin >> n >> k;
	vector<ld> p(n);
	rep(i,0,n) cin >> p[i];
	sort(allof(p));
	ld ans = 0;
	rep(l,0,k+1){
		vector<ld> pp;
		rep(i,0,n)
			if(i < l || i >= n-(k-l))
				pp.pb(p[i]);
		assert(pp.size() == k);
		vector<ld> dp(k/2 + 1);
		dp[0] = 1;
		for(ld x : pp){
			rrep(i,0,dp.size())
				dp[i] = dp[i]*(1-x) + (i ? dp[i-1]*x : 0);
		}
		ans = max(ans, dp.back());
	}
	cout << ans << endl;
}

int main(){
	cout.precision(15);
	int T;
	cin >> T;
	rep(t,1,T+1){
		printf("Case #%d: ",t);
		solve();
	}
}