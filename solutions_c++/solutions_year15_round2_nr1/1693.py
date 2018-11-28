#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
const int nmax = 1e6+5;
int dp[nmax],last[nmax];
int rev(int a){
	int ans = 0;
	while(a>0){
		ans*=10;
		ans+=a%10;
		a/=10;
	}
	return ans;
}
int small(){
	int n;
	cin >> n;
	for(int i = 0; i <= n; ++i){
		dp[i]=nmax;
	}
	dp[0]=0;
	for(int i = 0; i < n; ++i){
		dp[i+1]=min(dp[i+1],dp[i]+1);
		dp[rev(i)]=min(dp[rev(i)],dp[i]+1);
	}
	return dp[n];
}
int main(){
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int test = 1; test <= T; ++test){
		cout << "Case #" << test << ": ";
		cout << small() << '\n';
	}
}

