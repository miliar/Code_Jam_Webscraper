#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll rev(ll i){
	string res = "";
	while(i > 0){
		res += to_string(i%10);
		i /= 10;
	}
	return atoll(res.c_str());
}
ll dp[1000010], n;
ll solve(ll i){
	//cout<<i<<endl;
	if(i == n) return 1;
	if(i > n) return 2e9;
	if(dp[i] != -1) return dp[i];
	ll x = rev(i);	
	if(x <= i) return dp[i] = 1 + solve(i+1);
	return dp[i] = 1 + min(solve(i+1), solve(x));
}
int main (int argc, char const* argv[])
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int t; cin>>t;
	for(int i = 0; i < t; ++i){
		memset(dp, -1, sizeof dp);
		ll sol = 0;  cin>>n;
		cout<<"Case #"<<(i+1)<<": "<<solve(1)<<"\n";
	}
	return 0;
}
