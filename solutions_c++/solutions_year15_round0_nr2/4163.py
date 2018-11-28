#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
map<multiset<int>, int> dp;
int rec(multiset<int> s){
	auto it = s.rbegin();
	int x = *it;
	//cout<<x<<endl;
	if(x == 1 || x == 2 || x == 3) return x;
	if(dp.count(s) != 0) return dp[s];
	int res = x;
	s.erase((++it).base());
	multiset<int> k = s;
	if(x == 9) {k.insert(3); k.insert(6); res = min(res, 1 + rec(k)); k = s; k.insert(4); k.insert(5); res = min(res, 1 + rec(k));}			
	else{
			k.insert(x/2);
			if(x % 2) k.insert(x/2 + 1); else k.insert(x/2);
			res = min(res, 1 + rec(k));
		}
	
	return dp[s] = res;		

}
int main (int argc, char const* argv[])
{
	//ios_base::sync_with_stdio(false);
	//cin.tie(0);
	int t; cin>>t;
	for(int i = 0; i < t; ++i){
		dp.clear();
		ll n, d, sol = 0; multiset<int> s;
		cin>>n;
		int maxi = -1;
		for(int j = 0; j < n; ++j){
			int tmp; cin>>tmp;			
			s.insert(tmp);			
			maxi = max(maxi, tmp);
		}
		sol = min(maxi, rec(s));
		cout<<"Case #"<<(i+1)<<": "<<sol<<"\n";

	}
	return 0;
}
