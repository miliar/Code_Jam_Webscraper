#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
const int nmax = 1005;
int dp[nmax][nmax];
int need_div(int a, int t){
	if(dp[a][t]!=-1)
		return dp[a][t];
	if(a<=t)
		return dp[a][t]=0;
	dp[a][t]=nmax;
	for(int i = 1; i < a; ++i)
		dp[a][t]=min(dp[a][t],need_div(i,t)+need_div(a-i,t)+1);
	return dp[a][t];
}
bool special(vector<int> a, int t, int s){
	for(int i = 0; i < a.size(); ++i){
		int cost = need_div(a[i],t);
		if(cost>s)
			return false;
		s-=cost;
	}
	return true;
}
bool solve(vector<int> a, int t){
	for(int s = 0; s < t; ++s)
		if(special(a,t-s,s))
			return true;
	return false;
}
int main(){
	for(int i = 0; i < nmax; ++i)
		for(int j = 0; j < nmax; ++j)
			dp[i][j]=-1;
	//cout << need_div(100,10) << '\n';
	//cout << need_div(50,10) << '\n';
	//cout << need_div(3,2) << '\n';
	int T;
	cin >> T;
	for(int test = 1; test <= T; ++test){
		int n;
		cin >> n;
		vector<int> a(n);
		for(int i = 0; i < n; ++i)
			cin >> a[i];
		int lo = 0, hi = 1000, mid;
		while(lo<hi){
			mid=(lo+hi)/2;
			if(solve(a,mid))
				hi=mid;
			else
				lo=mid+1;
		}
		cout << "Case #" << test << ": " << lo << '\n';
	}
}

